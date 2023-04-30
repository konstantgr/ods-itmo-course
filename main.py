import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
from pathlib import Path
from preprocessing.message import Message, messages_to_dataframe


def plot_timeseries(df):
    df['time'] = pd.to_datetime(df['time'])

    # Group the DataFrame by 3-hour periods and count the number of occurrences
    counts = df.groupby(pd.Grouper(key='time', freq='200H')).size()

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    counts.plot(ax=ax, kind='line')
    ax.set_xlabel('Date with 3-hour Periods')
    ax.set_ylabel('Number of Actions')
    ax.set_title('3-Hour Activity Time Series')
    plt.show()


if __name__ == '__main__':
    data_path = Path('data/result.json')
    with data_path.open('r') as f:
        data = json.load(f)

    messages = [Message(m) for m in data['messages'][:]]
    df = messages_to_dataframe(messages)
    plot_timeseries(df)
