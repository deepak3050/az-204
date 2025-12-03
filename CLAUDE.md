# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a study guide repository for the **AZ-204: Developing Solutions for Microsoft Azure** certification exam. It contains:
- Study materials organized by Azure service topics in `/Topics/`
- Practice questions in `/Questions/`
- A React Router (formerly Remix) quiz application in `/quiz-app/` deployed at https://az-204.vercel.app/
- Hands-on exercises from Microsoft Learning paths in `/Exercises/`

## Quiz App Architecture

The quiz app (`/quiz-app/`) is a React Router v7 application with the following key components:

### Build System
- **Framework**: React Router v7 (formerly Remix) with Vite
- **TypeScript**: Full TypeScript support with strict mode enabled
- **Styling**: Tailwind CSS v4
- **Code Quality**: Biome for linting/formatting, Prettier for markdown

### Development Commands

```bash
# Quiz app (run from /quiz-app/ directory)
npm run dev          # Start dev server (auto-runs seed script)
npm run build        # Production build (auto-runs seed script)
npm start            # Run production server
npm run seed         # Generate quiz database from markdown files
npm run check        # Run linting and type checking
npm run format       # Format code with Biome and Prettier
npm run typecheck    # Type check only
```

### Data Flow Architecture

The quiz app uses a unique build-time data generation pattern:

1. **Seed Script** (`scripts/seed.mjs`):
   - Runs automatically before dev/build via prebuild/predev hooks
   - Parses markdown files from `/Topics/` and `/Questions/` directories
   - Generates `app/db.ts` containing all quiz questions as a TypeScript array
   - Each question gets a unique hash-based ID for stable URL routing

2. **Question Data Model** (`app/types/QAPair.ts`):
   - Questions support both single and multiple correct answers
   - Code syntax highlighting via `hasCode` flag
   - Topics are extracted from source markdown filenames

3. **Quiz Logic** (`app/lib/qa.ts`):
   - Implements smart question selection with weighted randomization
   - Questions answered correctly have decreasing probability of reappearing
   - Supports topic filtering and question shuffling
   - Answer options are randomized on each render

4. **Routing Pattern**:
   - Main route: `app/routes/$id.tsx` handles individual questions
   - Uses React Router loader/action pattern for data fetching
   - Question state persisted via URL query params (`?id=...&topic=...`)
   - Answered questions tracked in URL for session continuity

### Content Organization

**Topics vs Questions**: The repository has two parallel markdown structures:
- `/Topics/*.md`: Detailed study notes on Azure services (e.g., "App Service.md", "Functions.md")
- `/Questions/*.md`: Quiz questions for each topic, parsed by seed script

**Markdown Format for Questions** (in `/Questions/`):
```markdown
Question: [Question text]

- [ ] Option 1
- [x] Correct option
- [ ] Option 3

Answer: [Explanation]

---
```

Multiple `[x]` marks indicate multiple correct answers.

## Content Guidelines

When working with study materials or quiz questions:

1. **No Exam Dumps**: Never add actual exam questions or proprietary content (see CONTRIBUTING.md)
2. **Emoji Conventions**: The repository uses specific emojis with technical meanings:
   - ⭐: Recommended
   - ❌: Not recommended/Not supported
   - ⏺️: Default option
   - 🏷️: Cheap/Cost-effective
   - 💲: Expensive
   - ⚡: Fast/Low latency
   - 🐌: Slow/High latency
   - 💎: Premium tier only
   - 🏋️: Heavy workload/Transaction-intensive
   - 🧊: Immutable
   - 🔑: Microsoft Managed Keys
   - 🗝️: User Managed Keys

3. **Study Resources**: When adding content, reference official Microsoft Learn documentation (patterns in README.md)

## Project Structure

```
/Topics/              # Detailed study notes per Azure service
/Questions/           # Quiz questions matching topic names
/Exercises/           # Microsoft hands-on lab exercises
/Learning Path/       # Microsoft Learning Path content
/quiz-app/
  /app/
    /routes/          # React Router file-based routes
    /components/      # React components (AnswerOptions, RichMarkdown, etc.)
    /lib/             # Core logic (qa.ts for question selection)
    /types/           # TypeScript type definitions
  /scripts/
    seed.mjs          # Build-time data generation from markdown
  /db.ts             # Auto-generated quiz database (do not edit manually)
```

## Important Notes

- The `/quiz-app/app/db.ts` file is **auto-generated** by the seed script - never edit it directly
- When adding new questions, add them to `/Questions/*.md` following the markdown format
- When adding new topics, create matching files in both `/Topics/` and `/Questions/`
- The quiz app uses path aliases: `~/` maps to `app/` directory (configured in tsconfig.json)
- TypeScript is configured with strict mode and no emit (Vite handles compilation)
