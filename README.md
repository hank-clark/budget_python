## Goal
Create a personal budget system for combining spending statement from multiple different sources into a single combined and standardized format.

## Project Principles
1. Lightweight. This should be a system that has relatively few moving parts.
2. Data Integrity. I want to ensure no duplicate entries of transactions, system being able to handle multiple formats from different sources.

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
