import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#Load the most recent rows sorted by datetime
def load_latest_data(db_path: str, table_name: str, limit: int=1000) -> pd.DataFrame:
    """Load the most recent number of rows based on limit and sorted by datetime"""

    conn = sqlite3.connect(db_path)
    query = f"""
        SELECT * FROM {table_name}
        ORDER BY datetime DESC
        LIMIT {limit}
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # sort chronologically
    df = df.sort_values(by='datetime')
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

# Plots prices and labels high and low points
def plot_with_extrema(df: pd.DataFrame):
    """Plot close price and label highest and lowest points"""

    plt.figure(figsize=(14,6))

