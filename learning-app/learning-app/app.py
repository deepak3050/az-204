#!/usr/bin/env python3
"""
AZ-204 Learning App
A Flask application to browse and study AZ-204 exam materials
"""

import os
import re
from pathlib import Path
from flask import Flask, render_template, abort
import markdown2

app = Flask(__name__)

# Base paths
# Go up three levels: learning-app/learning-app/app.py -> learning-app/learning-app -> learning-app -> az-204
BASE_DIR = Path(__file__).parent.parent.parent
TOPICS_DIR = BASE_DIR / "Topics"
QUESTIONS_DIR = BASE_DIR / "Questions"
EXERCISES_DIR = BASE_DIR / "Exercises"
KNOWLEDGE_CHECK_DIR = BASE_DIR / "Knowledge Check"
LEARNING_PATH_DIR = BASE_DIR / "Learning Path"


def get_markdown_files(directory):
    """Get all markdown files from a directory"""
    if not directory.exists():
        return []

    files = []
    for file_path in sorted(directory.glob("*.md")):
        if file_path.name != "README.md":
            files.append({
                'name': file_path.stem,
                'filename': file_path.name,
                'path': file_path
            })
    return files


def get_subdirectories(directory):
    """Get all subdirectories from a directory"""
    if not directory.exists():
        return []

    dirs = []
    for dir_path in sorted(directory.iterdir()):
        if dir_path.is_dir() and not dir_path.name.startswith('.'):
            readme_path = dir_path / "README.md"
            dirs.append({
                'name': dir_path.name,
                'path': dir_path,
                'has_readme': readme_path.exists()
            })
    return dirs


def render_markdown(content):
    """Render markdown content to HTML with code highlighting"""
    return markdown2.markdown(
        content,
        extras=[
            "fenced-code-blocks",
            "tables",
            "code-friendly",
            "cuddled-lists",
            "task_list",
            "strike",
            "header-ids"
        ]
    )


def find_related_content(topic_name):
    """Find related content across different directories"""
    related = {
        'questions': None,
        'knowledge_check': None,
        'exercises': [],
        'learning_path': None
    }

    # Check for questions
    questions_file = QUESTIONS_DIR / f"{topic_name}.md"
    if questions_file.exists():
        related['questions'] = topic_name

    # Check for knowledge check
    kc_file = KNOWLEDGE_CHECK_DIR / f"{topic_name}.md"
    if kc_file.exists():
        related['knowledge_check'] = topic_name

    # Check for learning path
    lp_file = LEARNING_PATH_DIR / f"{topic_name}.md"
    if lp_file.exists():
        related['learning_path'] = topic_name

    # Check for exercises (they're in subdirectories)
    if EXERCISES_DIR.exists():
        for exercise_dir in EXERCISES_DIR.iterdir():
            if exercise_dir.is_dir():
                # Simple keyword matching
                if any(word.lower() in exercise_dir.name.lower() for word in topic_name.split()):
                    related['exercises'].append(exercise_dir.name)

    return related


def fix_study_plan_links(html_content):
    """Convert markdown file links to app routes"""
    import re

    # Convert ./NOTES.md to /notes
    html_content = re.sub(
        r'href="\.?/NOTES\.md"',
        r'href="/notes"',
        html_content
    )

    # Remove Synopsis.md link (file doesn't exist) - convert to plain text
    html_content = re.sub(
        r'<a href="\.?/Synopsis\.md">Synopsis</a>',
        r'Synopsis',
        html_content
    )

    # Convert ./Topics/Something.md to /topic/Something
    html_content = re.sub(
        r'href="\.?/Topics/([^"]+)\.md"',
        r'href="/topic/\1"',
        html_content
    )

    # Convert ./Questions/Something.md to /questions/Something
    html_content = re.sub(
        r'href="\.?/Questions/([^"]+)\.md"',
        r'href="/questions/\1"',
        html_content
    )

    # Convert ./Knowledge Check/Something.md to /knowledge-check/Something
    html_content = re.sub(
        r'href="\.?/Knowledge%20Check/([^"]+)\.md"',
        r'href="/knowledge-check/\1"',
        html_content
    )
    html_content = re.sub(
        r'href="\.?/Knowledge Check/([^"]+)\.md"',
        r'href="/knowledge-check/\1"',
        html_content
    )

    # Convert ./Learning Path/Something.md to /learning-path/Something
    html_content = re.sub(
        r'href="\.?/Learning%20Path/([^"]+)\.md"',
        r'href="/learning-path/\1"',
        html_content
    )
    html_content = re.sub(
        r'href="\.?/Learning Path/([^"]+)\.md"',
        r'href="/learning-path/\1"',
        html_content
    )

    return html_content


@app.route('/')
def index():
    """Home page with overview of all resources"""
    topics = get_markdown_files(TOPICS_DIR)
    exercises = get_subdirectories(EXERCISES_DIR)

    # Get study plan if it exists
    study_plan_path = BASE_DIR / "Study Plan.md"
    study_plan = None
    if study_plan_path.exists():
        with open(study_plan_path, 'r', encoding='utf-8') as f:
            content = f.read()
            study_plan = render_markdown(content)
            # Fix links to use app routes instead of raw file paths
            study_plan = fix_study_plan_links(study_plan)

    return render_template(
        'index.html',
        topics=topics,
        exercises=exercises,
        study_plan=study_plan
    )


@app.route('/topics')
def topics_list():
    """List all topics"""
    topics = get_markdown_files(TOPICS_DIR)
    return render_template('topics_list.html', topics=topics)


@app.route('/topic/<path:topic_name>')
def topic_detail(topic_name):
    """Show topic detail"""
    topic_file = TOPICS_DIR / f"{topic_name}.md"

    if not topic_file.exists():
        abort(404)

    with open(topic_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)
    related = find_related_content(topic_name)

    return render_template(
        'topic_detail.html',
        topic_name=topic_name,
        content=html_content,
        related=related
    )


@app.route('/questions')
def questions_list():
    """List all question sets"""
    questions = get_markdown_files(QUESTIONS_DIR)
    return render_template('questions_list.html', questions=questions)


@app.route('/questions/<path:topic_name>')
def questions_detail(topic_name):
    """Show questions for a topic"""
    questions_file = QUESTIONS_DIR / f"{topic_name}.md"

    if not questions_file.exists():
        abort(404)

    with open(questions_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse questions (keep raw markdown for better formatting)
    html_content = render_markdown(content)

    return render_template(
        'questions_detail.html',
        topic_name=topic_name,
        content=html_content
    )


@app.route('/knowledge-check')
def knowledge_check_list():
    """List all knowledge checks"""
    checks = get_markdown_files(KNOWLEDGE_CHECK_DIR)
    return render_template('knowledge_check_list.html', checks=checks)


@app.route('/knowledge-check/<path:topic_name>')
def knowledge_check_detail(topic_name):
    """Show knowledge check for a topic"""
    kc_file = KNOWLEDGE_CHECK_DIR / f"{topic_name}.md"

    if not kc_file.exists():
        abort(404)

    with open(kc_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)

    return render_template(
        'knowledge_check_detail.html',
        topic_name=topic_name,
        content=html_content
    )


@app.route('/exercises')
def exercises_list():
    """List all exercises"""
    exercises = get_subdirectories(EXERCISES_DIR)
    return render_template('exercises_list.html', exercises=exercises)


@app.route('/exercise/<path:exercise_name>')
def exercise_detail(exercise_name):
    """Show exercise detail"""
    exercise_dir = EXERCISES_DIR / exercise_name
    readme_file = exercise_dir / "README.md"

    if not readme_file.exists():
        abort(404)

    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)

    # Get other files in the exercise directory
    other_files = []
    for file_path in sorted(exercise_dir.glob("*")):
        if file_path.is_file() and file_path.name != "README.md":
            other_files.append(file_path.name)

    return render_template(
        'exercise_detail.html',
        exercise_name=exercise_name,
        content=html_content,
        other_files=other_files
    )


@app.route('/learning-path')
def learning_path_list():
    """List all learning path materials"""
    materials = get_markdown_files(LEARNING_PATH_DIR)
    return render_template('learning_path_list.html', materials=materials)


@app.route('/learning-path/<path:topic_name>')
def learning_path_detail(topic_name):
    """Show learning path material"""
    lp_file = LEARNING_PATH_DIR / f"{topic_name}.md"

    if not lp_file.exists():
        abort(404)

    with open(lp_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)

    return render_template(
        'learning_path_detail.html',
        topic_name=topic_name,
        content=html_content
    )


@app.route('/notes')
def notes():
    """Show exam notes and strategies"""
    notes_file = BASE_DIR / "NOTES.md"

    if not notes_file.exists():
        abort(404)

    with open(notes_file, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)

    return render_template(
        'notes.html',
        content=html_content
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
