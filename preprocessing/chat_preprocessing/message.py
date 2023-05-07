from datetime import datetime
from typing import List

import pandas as pd


class Message:
    def __init__(self, json_message: dict):
        self.date = self.get_date(json_message)
        self.text = self.get_text(json_message)

    @staticmethod
    def get_date(message: dict) -> datetime:
        date = message.get('date')
        date_format = '%Y-%m-%dT%H:%M:%S'
        return datetime.strptime(date, date_format)

    @staticmethod
    def get_text(message: dict) -> str:
        text = message.get('text')
        return text if isinstance(text, str) else text[0]


def messages_to_dataframe(messages: List[Message]) -> pd.DataFrame:
    return pd.DataFrame({'time': [m.date for m in messages], 'message': [m.text for m in messages]})
