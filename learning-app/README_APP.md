# AZ-204 Learning App

A Flask-based web application for studying AZ-204: Developing Solutions for Microsoft Azure exam materials.

## Features

- **Topics**: Browse detailed study notes on all Azure services covered in the exam
- **Practice Questions**: Test your knowledge with practice questions organized by topic
- **Knowledge Checks**: Quick verification questions to test understanding
- **Hands-on Exercises**: Step-by-step practical exercises from Microsoft Learning
- **Learning Path**: Official Microsoft learning path materials
- **Exam Notes**: Exam strategies, tips, and important reminders
- **Smart Cross-linking**: Automatically links related resources (topics, questions, exercises)

## Setup

This project uses `uv` for Python package management. If you don't have `uv` installed:

```bash
# Install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

## Running the App

From the `learning-app` directory:

```bash
# Run with uv (recommended)
uv run python app.py

# Or activate the virtual environment and run
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python app.py
```

The app will be available at `http://localhost:5000`

## Development

```bash
# Add new dependencies
uv add package-name

# Update dependencies
uv sync
```

## Project Structure

```
learning-app/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── topics_list.html  # Topics listing
│   ├── topic_detail.html # Individual topic view
│   └── ...               # Other page templates
└── static/
    └── css/
        └── style.css     # Application styles
```

## Features Detail

### Smart Cross-linking

When viewing a topic, the app automatically finds and links to:
- Related practice questions
- Related knowledge checks
- Related exercises (keyword matching)
- Related learning path materials

### Markdown Rendering

All content is rendered from markdown files with support for:
- Code syntax highlighting
- Tables
- Task lists
- GitHub-flavored markdown

## Contributing

This app reads content from the parent directory structure:
- `/Topics/*.md` - Study notes
- `/Questions/*.md` - Practice questions
- `/Knowledge Check/*.md` - Knowledge verification
- `/Exercises/*/README.md` - Hands-on exercises
- `/Learning Path/*.md` - Microsoft learning materials

Add or update markdown files in these directories to add new content.

## License

See parent repository LICENSE.
