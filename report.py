import numpy as np
import pandas as pd

def calc_correct_responses():
    df['Status'] = np.where(df["correct_answer"] == df["Predictions"], True, False)
    correct = df.Status.sum()
    incorrect = df.shape[0] - correct
    return correct, incorrect

def calc_score_for_topic():
    topics = df['topic'].unique()
    topic_scores = {}
    for topic in topics:
        dt = df[df['topic'] == topic]
        topic_scores[topic] = [dt.Status.sum(), dt.shape[0]]
    return topic_scores

def percentage(correct):
    percent = np.round((correct/df.shape[0])*100, 2)
    return percent

def percentage_for_topic(topic_scores):
    percentage_topic = {}
    for topic in topic_scores:
        percentage_topic[topic] = np.round((topic_scores[topic][0]/topic_scores[topic][1])*100, 2)
    return percentage_topic

df = pd.read_csv('Data\\answers-multipage.csv')
df['Predictions'] = [2,1,3,4,3,4,1,1,1,2,3,2,2,3,4]
correct, incorrect = calc_correct_responses()
topic_scores = calc_score_for_topic()
percent = percentage(correct)
percentage_topic = percentage_for_topic(topic_scores)

