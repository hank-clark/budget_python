import pandas as pd
from pathlib import Path


def return_header_row_number(file_path, target_column:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            if target_column in line:
                return idx
    return 0

def standardize_date(df):
    date_format_tuple = ('%m/%d/%Y', '%b-%d-%Y')
    
    for date_format in date_format_tuple:
        try:
            df['Date'] = pd.to_datetime(df['Date'], format=date_format).dt.strftime('%m/%d/%Y')
            break
        except:
            pass

    return df

def clean_credit_card_df(df):
    standardize_date(df)
    df.drop(columns=['Account Name', 'Transaction Type', 'Category', 'Subcategory', 'Hidden Transaction'], inplace=True)

    df['Debit'] = df['Amount (in $)'].clip(upper=0)
    df['Credit'] = df['Amount (in $)'].clip(lower=0)

    df.drop(columns=['Amount (in $)'], inplace=True)

def clean_bankcc_df(df):
    standardize_date(df)
    df.drop(columns=['Account Number', 'Account Type','Check #', 'Category', 'Memo'], inplace=True)
    df.fillna(0, inplace=True)

def clean_bank_checking_df(df):
    standardize_date(df)
    df.drop(columns=['Account Number', 'Account Type','Check #', 'Category', 'Memo'], inplace=True)
    df.fillna(0, inplace=True)


directory_path = Path("./data/raw")
df_dict = {}

for file_path in directory_path.glob('*.csv'):
    skip_row_count = return_header_row_number(file_path, 'Date')
    df_dict[file_path.stem] = pd.read_csv(file_path, skiprows=skip_row_count)

    headers = ['Date', 'Description']
    df_dict[file_path.stem] = df_dict[file_path.stem].dropna(subset=headers)