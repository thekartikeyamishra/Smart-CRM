import pandas as pd
import os

DATA_PATH = "data/customers.csv"


def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        return pd.DataFrame(columns=["Customer ID", "Name", "Contact", "Purchase History", "Notes"])


def save_data(df):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    df.to_csv(DATA_PATH, index=False)


def add_customer(df, customer):
    return df.append(customer, ignore_index=True)


def delete_customer(df, customer_id):
    return df[df["Customer ID"] != customer_id]
