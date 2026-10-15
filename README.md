# Python Fundamentals & Mini-Project Proposal

**Program:** THDC-IHET Python / AI-ML Preparation  
**Student:** Replace with your name  
**Branch/Year:** B.Tech CSE  
**Repository purpose:** Practice Python fundamentals, algorithms, Git/GitHub, and propose a mini-project.

## 1. What this repository contains

- `python_practice/main.py`: variables, data types, conditions, loops, functions, data structures, and a simple practice problem.
- `python_practice/search_sort.py`: linear search, binary search, and bubble sort.
- `PROGRESS.md`: setup and assignment checklist.

## 2. How to run

Install Python 3, then open a terminal in this repository and run:

```bash
python --version
python python_practice/main.py
python python_practice/search_sort.py
```

On some systems, use `python3` instead of `python`. On Windows, `py` may also work.

## 3. Mini-project proposal

### Title: CampusFix — Campus Issue Reporting and Prioritization

**Problem statement:** Students may report campus issues such as broken lights, water leakage, damaged furniture, or network outages through scattered messages. Reports can be missed, duplicated, or handled without a clear priority.

**Who faces the problem?** Students, hostel residents, maintenance staff, and campus administrators.

**Why it matters:** A central record can make reports easier to track, help staff identify urgent problems, and make the status of each report more transparent.

**Proposed Python approach:**
1. Build a command-line prototype that accepts an issue category, location, description, and urgency.
2. Store reports in a CSV file or SQLite database.
3. Assign an initial priority using clear rules, for example safety-related issues before cosmetic issues.
4. Add search and filtering by category, location, status, and priority.
5. Later, explore text classification to categorize descriptions. Use a labelled dataset and evaluate the model before relying on its predictions.

**Possible AI/ML extension:** Train a text classifier to suggest issue categories from descriptions. Initially, use rule-based priority logic; do not claim it is machine learning until a model is actually trained and evaluated.

**What I need to learn:**
- Python functions, lists, dictionaries, and file handling
- CSV or SQLite
- Exception handling and input validation
- Basic testing
- Text preprocessing and classification concepts for the optional AI/ML extension
- Git branches, commits, and README documentation

**Minimum viable version:** A terminal-based program to create, list, search, and update campus issue reports.

## 4. Current learning

Update this section honestly as you work:
- Learned/practiced: [write topics you actually ran]
- Currently working on: [topic]
- Next: [topic]

## 5. Limitations and next steps

This is a proposal, not a completed campus deployment. The first version will use sample data and a local file/database. Any real deployment would require user permissions, privacy safeguards, and agreement from campus administrators.
