# Personal Finance ETL & Aggregation Engine

A lightweight Python-based ETL pipeline that ingests, cleans, normalizes, and aggregates transaction data from diverse financial institution statements into a centralized SQLite database.

## Key Features & Design Principles

* **Robust Data Pipeline:** Extracts raw statement data from heterogeneous CSV files and standardizes schemas for unified querying.
* **Data Integrity & Deduplication:** Prevents duplicate entries through robust schema validation and transactional loading.
* **Minimalist & Lightweight:** Built using core Python libraries without unnecessary dependencies to ensure low overhead and easy local execution.
* **Relational Schema:** Features a normalized database model linking transactions to dynamic, two-tier spending categories.

## System Architecture & Data Flow

```
budget_python/
|-- data/
|    |-- raw/
|    |    /-- dataset.csv
|    |    /-- dataset2.csv
|    |-- processed/
|    |    /-- labeled.xlsx
|-- parser.py
|-- create_sql.py
|-- import_sql.py    
```
### Execution Workflow

1. **Ingestion (`parser.py`):** Scans `data/raw/` for raw institution statements. Dynamically detects header locations by identifying key columns (`Date`) and loads records into structured Pandas DataFrames.
2. **Database Initialization (`create_sql.py`):** Configures the local SQLite database and instantiates relational tables with proper primary and foreign key constraints.
3. **Categorization & Staging:** Processes raw transactions through a standardized categorization pipeline (staged via `data/processed/labeled.xlsx`).
4. **ETL Load (`import_sql.py`):** Ingests transformed, categorized transactions directly into the primary SQLite database.

## Database Design

The relational model utilizes a master transaction log coupled with a two-tier hierarchy (`categories` and `subcategories`) to support flexible reporting and granularity.


<img width="672" height="582" alt="prototype Budget SQL diagram" src="https://github.com/user-attachments/assets/04642111-6bb0-4689-8cfc-4421e125c445" />

## Tech Stack

* **Language:** Python 3.12.2
* **Data Transformation:** Pandas
* **Database Engine:** SQLite3


## Roadmap & Future Enhancements

- [ ] **Automated Categorization Engine:** Implement machine learning / heuristic rules (regex/TF-IDF) to auto-tag transactions upon ingestion.
- [ ] **Adaptive Parsing:** Expand parsing layer support for varying bank schemas, custom date formats, and non-standard delimiter layouts.
- [ ] **Analytics Dashboard:** Integrate Streamlit or Metabase for visual budget tracking and spending analysis.