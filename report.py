import numpy as np
import pandas as pd

def calc_correct_responses(df):
    return len(df), len(df[df.correct_answer == df.student_answer]), len(df[df.correct_answer != df.student_answer])

def calc_score_for_topic(df):
    topics = df['topic'].unique()
    topic_scores = []
    for topic in topics:
        topic_df = df[df.topic == topic]
        # list of topic, correct, wrong, total answers in topic
        topic_scores.append([topic, len(topic_df[topic_df.correct_answer == topic_df.student_answer]), len(topic_df[topic_df.correct_answer != topic_df.student_answer]), len(topic_df)])
        print(topic_scores)
    return topic_scores

def incorrct_question(df):
    incorrect_questios = df[df.correct_answer != df.student_answer]
    return incorrect_questios
