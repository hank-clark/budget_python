import sqlite3
import pandas as pd

#import transactions that have been properly categorized from 'labeled.xlsx'
imported_transactions_df = pd.read_excel('./data/processed/labeled.xlsx', header=0)
imported_transactions_df = imported_transactions_df.drop(columns='Subcategory')


sql_connection = sqlite3.connect('./data/processed/transactions.db')
cursor = sql_connection.cursor()

cursor.execute(
    '''
    CREATE TEMP TABLE staging_table (
        account TEXT,
        date TEXT,
        description TEXT,
        debit REAL DEFAULT 0.00,
        credit REAL DEFAULT 0.00,
        subcategory_id INTEGER
    )
'''
)

imported_transactions_df.to_sql('staging_table', sql_connection, if_exists='append', index=False)

cursor.execute(
    '''
    INSERT OR IGNORE INTO transactions (account, date, description, debit, credit, subcategory_id)
    SELECT account, date, description, debit, credit, subcategory_id
    FROM staging_table
'''
)

sql_connection.commit()
sql_connection.close()