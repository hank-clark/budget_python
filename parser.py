import pandas as pd
from pathlib import Path


def return_header_row_number(file_path, target_column:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            if target_column in line:
                return idx
    return 0

def standardize_date(df):
    date_format_tuple = ('%m/%d/%Y', '%b-%d-%Y', '%Y-%m-%d')
    
    for date_format in date_format_tuple:
        try:
            df['Date'] = pd.to_datetime(df['Date'], format=date_format).dt.strftime('%Y-%m-%d')
            break
        except:
            pass
            #add in future error handling for mismatching date format

    return df

def reorder_columns(df):
    return df.reindex(columns=['Account', 'Date', 'Description', 'Debit', 'Credit'])

def clean_credit_card_df(df):
    standardize_date(df)
    df['Account'] = df['Account Name']
    df.drop(columns=['Account Name', 'Transaction Type', 'Category', 'Subcategory', 'Hidden Transaction'], inplace=True)

    df['Debit'] = df['Amount (in $)'].clip(upper=0)
    df['Credit'] = df['Amount (in $)'].clip(lower=0)

    df.drop(columns=['Amount (in $)'], inplace=True)
    return reorder_columns(df)

def clean_bankcc_df(df):
    standardize_date(df)
    df.drop(columns=['Account Number', 'Account Type','Check #', 'Category', 'Memo'], inplace=True)
    df.fillna(0, inplace=True)
    return reorder_columns(df)

def clean_bank_checking_df(df):
    standardize_date(df)
    df.drop(columns=['Account Number', 'Account Type','Check #', 'Category', 'Memo'], inplace=True)
    df.fillna(0, inplace=True)

    return reorder_columns(df)


directory_path = Path('./data/raw')
df_dict = {}

for file_path in directory_path.glob('*.csv'):
    skip_row_count = return_header_row_number(file_path, 'Date')
    df_dict[file_path.stem] = pd.read_csv(file_path, skiprows=skip_row_count)

    keep_headers = ['Date', 'Description']
    df_dict[file_path.stem] = df_dict[file_path.stem].dropna(subset=keep_headers)

for key in df_dict:
    if df_dict[key].columns.to_list() == ['Date', 'Description', 'Amount (in $)', 'Account Name', 'Transaction Type', 'Category', 'Subcategory', 'Hidden Transaction']:
        df_dict[key] = clean_credit_card_df(df_dict[key])
    elif (df_dict[key].columns.to_list() == ['Date', 'Account', 'Account Number', 'Account Type', 'Description', 'Check #', 'Category', 'Memo', 'Credit', 'Debit']) and ((df_dict[key]['Account'] == 'Visa Credit Card').all()):
            df_dict[key] = clean_bankcc_df(df_dict[key])
    else: df_dict[key] = clean_bank_checking_df(df_dict[key])

concatted_df = pd.concat(df_dict.values(), ignore_index=True)
concatted_df.to_excel('./data/processed/concatted.xlsx', index=False)