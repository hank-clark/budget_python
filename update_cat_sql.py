import pandas as pd
import sqlite3

sql_connection = sqlite3.connect('./data/processed/budget.db')
cursor = sql_connection.cursor()

category_df = pd.read_excel('./data/processed/categories_and_subcategories.xlsx', sheet_name='categories')
subcat_df = pd.read_excel('./data/processed/categories_and_subcategories.xlsx', sheet_name='subcategories')


cursor.execute(
    '''
    CREATE TEMP TABLE cat_staging_table (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT
    )
'''
)

cursor.execute(
    '''
    CREATE TEMP TABLE subcat_staging_table (
        subcategory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subcategory_name TEXT,
        category_id INTEGER
    )
'''
)

category_df.to_sql('cat_staging_table', sql_connection, if_exists='append', index=False)
subcat_df.to_sql('subcat_staging_table', sql_connection, if_exists='append', index=False)

cursor.execute(
    '''
    INSERT OR IGNORE INTO categories (category_id, category_name)
    SELECT category_id, category_name
    FROM cat_staging_table
'''
)

cursor.execute(
    '''
    INSERT OR IGNORE INTO subcategories (subcategory_id, subcategory_name, category_id)
    SELECT subcategory_id, subcategory_name, category_id
    FROM subcat_staging_table
'''
)

sql_connection.commit()
sql_connection.close()