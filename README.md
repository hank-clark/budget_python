## Goal
Create a personal budget system for combining spending statement from multiple different sources into a single combined and standardized format.

## Project Principles
1. Lightweight. This should be a system that has relatively few moving parts.
2. Data Integrity. I want to ensure no duplicate entries of transactions, system being able to handle multiple formats from different sources.

## Data Pipeline
1. In main directory have a 'data' folder that contains folders called 'processed' and 'raw'
2. 'raw' should contain the CSV files that are exported from your source of transactions.
3. Running parser.py should import all the CSVs into a dictionary of pandas DataFrames. This will search your CSV files for the first instance of 'Date' and know that is the header rows.
4. After running parser.py, running create_sql.py should create the sqlite DB and tables.
5. **This step is where data categorization will be implemented.** I manually cleaned data this time in labeled.xlsx just for easier testing. This categorization can be implemented later.
6. After data categorization is complete, processed transactions from labeled.xlsx will be imported into my sqlite DB with import_sql.py.

### Data Folder Outline
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

## Tools Utilized
- Python for data extraction, transformation
- SQLite for database to be a simple, self hosted format

## SQL Database Diagram
I want to implement a way to help with categorization of transactions. I've included the rudimentary relational database diagram.

- my transactions table will be the 'master' list of transactions
- subcategory table will be used for mapping the subcategory to correct category
- category table is for storing my categories

<img width="672" height="582" alt="prototype Budget SQL diagram" src="https://github.com/user-attachments/assets/04642111-6bb0-4689-8cfc-4421e125c445" />

# Future Add-ons
1. Automated categorization of transactions
2. Future proofing for transaction data from different sources (ex: data from different bank or credit card company that is structured different)
3. Budget visualization dashboard
