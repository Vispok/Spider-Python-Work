# LogSentry: Python-Based Log Analysis and Anomaly Detection

## Project Overview

LogSentry is a planned Python project that analyses computer system logs, summarizes activity, and flags potentially suspicious patterns for further investigation. The first version will use sample log data and transparent, rule-based checks. Machine learning may be explored in a later version.

**Current status:** Proposal and planning  
**Initial implementation:** Pending

## 1. Problem Statement

Computer systems can generate many log entries, making it difficult to review them manually. Important patterns—such as repeated failed login attempts within a short period—can be overlooked. LogSentry aims to make sample log data easier to inspect by organizing events, summarizing activity, and highlighting patterns that may need investigation.

## 2. Who Faces This Problem?

- System and network administrators
- Small organizations and businesses
- College computer labs and student project teams
- Learners who want to understand log analysis and basic cybersecurity

## 3. Why Is This Problem Important?

Logs can help people understand what happened on a system. Summarizing them and flagging unusual patterns can reduce manual review effort and help an administrator decide what to investigate. An alert is only a signal for review; it does not prove that an attack occurred.

## 4. Planned Features

### First version
- Read sample log entries from a text or CSV file.
- Validate and organize the records.
- Count successful and failed login events.
- Group failed attempts by IP address.
- Flag patterns that cross a configurable threshold.
- Print a summary report in the terminal.

### Possible later features
- Save events and results in SQLite or PostgreSQL.
- Expose analysis through a FastAPI backend.
- Generate charts and reports.
- Experiment with machine-learning anomaly detection on an appropriate dataset.
- Compare model results with rule-based alerts.

## 5. Possible Python / AI / ML Approach

1. Use Python variables, conditions, loops, functions, and data structures to process log entries.
2. Use file handling and Python's `csv` and `json` modules to read structured data.
3. Write simple, explainable rules to flag repeated failed login attempts.
4. Use pandas for larger datasets and exploratory data analysis.
5. Store records in a database and optionally create API endpoints with FastAPI.
6. Later, explore scikit-learn anomaly-detection methods and evaluate their results using suitable test data and metrics.

The first version will be rule-based. Machine learning is a future extension, not a feature that has already been implemented.

## 6. What I Need to Learn

- Python fundamentals and exception handling
- Strings, lists, dictionaries, sets, and functions
- File handling and CSV/JSON processing
- Basic networking and authentication-log concepts
- SQL and database fundamentals
- REST API basics and FastAPI
- Data analysis with pandas
- Machine learning fundamentals and model evaluation
- Testing, debugging, and Git/GitHub workflow

## 7. Development Plan

- [ ] Phase 1: Create a command-line program that reads sample logs.
- [ ] Phase 2: Add validation, summaries, and rule-based alerts.
- [ ] Phase 3: Add tests and improve error handling.
- [ ] Phase 4: Store records in a database and optionally add a FastAPI backend.
- [ ] Phase 5: Explore and evaluate a machine-learning approach.
- [ ] Phase 6: Document results and consider deployment.

## 8. Progress Checklist

- [x] Mini-project idea selected
- [x] Problem statement documented
- [x] Target users and importance identified
- [x] Possible Python/AI/ML approach described
- [x] Learning requirements listed
- [ ] Initial program implemented
- [ ] Tests and sample results added
- [ ] Database or API extension implemented
- [ ] Machine-learning extension evaluated, if appropriate

## 9. Limitations and Responsible Use

This project is for learning and demonstration. It will initially use synthetic or authorized sample logs only. It will not collect other people's network traffic or credentials. Rule-based alerts can produce false positives and miss suspicious activity, so results must be reviewed rather than treated as proof of an incident.

## 10. How to Run (After the First Version Is Implemented)

The exact command and input-file format will be documented once the initial program is created. For now, this repository section describes the project proposal and planned development.

## 11. Future Improvements

- Support additional log formats.
- Make detection thresholds configurable.
- Add clearer summaries and visualizations.
- Compare rule-based detection with machine-learning experiments.
- Add automated tests and deployment instructions.

---

**Note:** This README describes the planned project. Update the status and checklist as each feature is actually completed.
