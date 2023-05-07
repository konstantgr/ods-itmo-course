# Conflicts Recognition in Chat

The working environment is a crucial aspect that determines employee satisfaction. Conflict situations can arise due to
political differences, leading to strained relationships within the team and even resulting in someone losing their job.
Work chats are one of the places where conflicts can be provoked. This project aims to prevent such conflicts by using
the emotional context of the text to identify problematic chats.

My plan is to develop a tool that can help managers detect potential problems in chats in a timely manner by analyzing
the emotional color of the time series. The ideal situation is to have a permanent, non-negative emotional color in a
chat. For instance, a chat where photos of cats are frequently posted would have a positive emotional color, while a
chat that discusses important organizational issues would typically have a neutral emotional color.

By using this tool, companies can improve the overall working atmosphere and promote better employee satisfaction by
reducing conflict situations in the workplace.

## Data

As a data will be used several chat histories on the russian and english languages from the open source group chats.
Also, a separate source, I will use
comments below posts in the Telegram channels. Before using the emotion

## Emotion Detection

The base for the emotion recognition will be
pretrained [T5 model](https://huggingface.co/mrm8488/t5-base-finetuned-emotion).
Before using, this model will be fine-tuned using MELD dataset, which connects conversations and emotions.

## Anomaly Detection

Formally, the problem can be assumed as a looking for anomalies in the time-series. In our case, the anomaly will be a
sharp deterioration of the emotional context in the chat - that is, the theoretical formation of a conflict.
We can set
the task in two ways:

1. To predict the moment before the anomaly begins.
2. To predict with a high degree of confidence when the conflict is already underway.

So far, I'm more inclined to the second option, since for the first one you need
to carefully pre-create a selection.To solve a simple problem, you can use several approaches: either analyze time
series using statistical methods, or first perform clustering of the time series in order to more accurately determine
the features of the cluster of interest.

## Visualization

For visualization, a [streamlit](https://streamlit.io) webpage will be used, which will broadcast the "mood" time series
in chats.

## Structure of The Project
```bash
├── README.md
├── anomaly_detection
│   ├── __init__.py
│   ├── clusterisation.py
│   ├── metrics.py
│   └── statistical_heuristics.py
├── emotion_detection
│   ├── __init__.py
│   ├── datamodules.py
│   ├── model.py
│   └── text_to_emotion.py
├── poetry.lock
├── preprocessing
│   ├── __init__.py
│   ├── chat_preprocessing
│   │   ├── __init__.py
│   │   ├── chat_preprocessing.py
│   │   └── message.py
│   └── text_preprocessing
│       ├── __init__.py
│       ├── embedding.py
│       └── translation.py
├── pyproject.toml
└── streamlit_app
    ├── app.py
    ├── create_charts.py
    └── visualisation_utils.py
```
