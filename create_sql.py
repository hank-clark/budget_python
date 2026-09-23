import sqlite3

sql_connection = sqlite3.connect('./data/processed/transactions.db')

try:
        
    cursor = sql_connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')

    create_tables_query = '''
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS subcategories (
        subcategory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subcategory_name TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT,
        debit REAL DEFAULT 0.00,
        credit REAL DEFAULT 0.00,
        subcategory_id INTEGER,
        FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id) ON DELETE SET NULL,

        UNIQUE (account, date, description, debit, credit)
    );
    '''

    cursor.executescript(create_tables_query)
    sql_connection.commit()

except sqlite3.Error as e:
    print(f'An error occurred: {e}')