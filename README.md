# Developer Portfolio Summary

A small Python script that prints a structured developer portfolio summary.

## Features

- Stores project details in a list of dictionaries.
- Displays each project's problem, solution, tools, result, and code link.
- Sorts projects alphabetically by project type.
- Reports the total number of projects.
- Builds a combined, alphabetically sorted technology stack.

## Requirements

- Python 3.8 or newer

The script uses only the Python standard library.

## Run the Script

From this directory, run:

```bash
python PORTFOLIO.PY
```

The output includes the four portfolio projects, ordered by type, followed by the total project count and technology stack.

## Project Data

Each project includes these fields:

- `title`: Project name
- `problem`: Problem addressed
- `solution`: Implemented solution
- `tools`: Technologies used
- `result`: Project outcome
- `github`: Code repository link
- `type`: Project category used for sorting

To add another project, add a dictionary with the same fields to `projects` in `PORTFOLIO.PY`.
