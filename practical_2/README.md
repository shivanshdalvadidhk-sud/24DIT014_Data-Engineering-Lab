# Practical 2: Data Sources and Data Generation

## Overview

This project implements an automated source data profiling and validation pipeline using Python. It demonstrates how structured, semi-structured, and unstructured data can be ingested, profiled, validated, and stored before loading into a target database.

The implementation focuses on identifying data quality issues, automatically discovering schemas, quarantining invalid records, and maintaining execution logs.

---

## Objectives

- Generate synthetic customer data using Faker.
- Profile incoming datasets automatically.
- Discover data schemas.
- Detect missing and invalid values.
- Validate incoming data.
- Quarantine malformed records.
- Parse nested JSON data.
- Process configuration files.
- Store validated data into SQLite.
- Generate execution logs.

---

## Technologies Used

- Python 3.x
- Jupyter Notebook
- Pandas
- Faker
- SQLite
- JSON
- Logging Module

---

## Project Structure

```text
practical_2/
│
├── DE_practical_2.ipynb
├── README.md
├── customer.db
│
├── Data/
│   ├── customers.csv
│   ├── api_logs.json
│   ├── config.txt
│   └── quarantine.csv
│
└── Logs/
    └── ingestion.log
```

---

## Workflow

1. Generate synthetic customer records.
2. Save customer dataset to CSV.
3. Introduce data quality issues.
4. Load and profile the dataset.
5. Discover schema automatically.
6. Validate data types and missing values.
7. Detect invalid records.
8. Quarantine malformed records.
9. Generate execution logs.
10. Create nested JSON API data.
11. Parse JSON into tabular format.
12. Read and validate configuration files.
13. Store clean data in SQLite.
14. Generate a validation summary.

---

## Validation Checks

- Missing Primary Key
- Missing Email Address
- Invalid Age Format
- Schema Validation
- Data Type Validation
- Null Value Detection
- JSON Structure Validation

---

## Input Files

| File | Description |
|------|-------------|
| customers.csv | Synthetic customer dataset |
| api_logs.json | Nested API transaction data |
| config.txt | Configuration file |

---

## Output Files

| File | Description |
|------|-------------|
| quarantine.csv | Invalid records |
| customer.db | SQLite database |
| ingestion.log | Execution log |
| report.md | Validation report |

---

## Features

- Synthetic data generation
- Automated schema discovery
- Data profiling
- Data validation
- Quarantine mechanism
- SQLite integration
- Logging support
- JSON normalization

---

## Learning Outcomes

After completing this practical, the following concepts were learned:

- Data Profiling
- Schema Discovery
- Data Validation
- Data Quality Enforcement
- JSON Processing
- SQLite Database Operations
- Logging and Monitoring
- Source Data Analysis

---

## Conclusion

This practical demonstrates a complete data ingestion and validation workflow. It shows how multiple source data formats can be analyzed, validated, and cleaned before being stored in a database. The implementation improves data reliability by identifying malformed records early in the ingestion process.
