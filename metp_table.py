import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

with open("basic202108.json", "r", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data

students_info = {"6.00": 0,
                 "5.00+": 0,
                 "4.00+": 0,
                 "3.00+": 0,
                 "2.00": 0,
                 "Not attempt any task": 0}


def student_scores():
    for score in sorted(data_info['total_score']):
        if score == 600:
            students_info["6.00"] += 1
        elif score >= 500:
            students_info["5.00+"] += 1
        elif score >= 400:
            students_info["4.00+"] += 1
        elif score >= 300:
            students_info["3.00+"] += 1
        elif score == 0:
            students_info["Not attempt any task"] += 1
        elif score < 300:
            students_info["2.00"] += 1



student_scores()
num_high_score = []


def max_score_students():
    for task_name, task_scores in data_info.items():
        num_high_score.append(
            {'task name': task_name, 'maximum score': task_scores.count(100), 'contestants': len(data_info[task_name])})
    num_high_score.sort(key=lambda x: -x['maximum score'])




hardest_task_list = []


def hardest_task():
    for task_name, task_scores in sorted(data_info.items(), key=lambda x: (sum(x[1]) / len(x[1]))):
        hardest_task_list.append(
            {'task name': task_name, "average score": f"{(sum(task_scores) / len(task_scores)):.2f}",
             'contestants': len(task_scores)})
    hardest_task_list.sort(key=lambda x: x['average score'])


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return f"{pct:.2f}% ({absolute})"


def draw_student_pie():
    # Draw Plot
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

    data = list(students_info.values())
    categories = students_info.keys()
    explode = [0.1, 0, 0, 0, 0, 0]

    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"),
                                      colors=plt.cm.Dark2.colors,
                                      startangle=140,
                                      explode=explode)

    # Decoration
    ax.legend(wedges, categories, title="Scores", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title(f"Total Contestants : {len(data_info['total_score'])}")
    plt.show()


draw_student_pie()
del data_info['total_score']
max_score_students()


def draw_top_result_task():
    # Prepare Data
    df = pd.DataFrame(num_high_score)

    # Draw plot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    ax.vlines(x=df.index, ymin=0, ymax=df["maximum score"], color='firebrick', alpha=0.7, linewidth=2)
    ax.scatter(x=df.index, y=df["maximum score"], s=75, color='firebrick', alpha=0.7)

    # Title, Label, Ticks and Ylim
    ax.set_title('Contestants with maximum score per task!!', fontdict={'size': 22})
    ax.set_ylabel('Contestants', fontdict={'size': 17})
    ax.set_xticks(df.index)
    ax.set_xticklabels(df['task name'].str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size': 12})
    # ax.set_ylim(0, 30)

    # Annotate
    for row in df.itertuples():
        ax.text(row.Index, row._2, s=round(row._2, 0), horizontalalignment='center', verticalalignment='bottom',
                fontsize=17)

    plt.show()


draw_top_result_task()

hardest_task()
def draw_hardest_task():
    # Prepare Data
    df = pd.DataFrame(hardest_task_list)

    # Draw plot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    ax.vlines(x=df.index, ymin=0, ymax=df["average score"], color='firebrick', alpha=0.7, linewidth=2)
    ax.scatter(x=df.index, y=df["average score"], s=75, color='firebrick', alpha=0.7)

    # Title, Label, Ticks and Ylim
    ax.set_title('Average score per task 100 is maximum', fontdict={'size': 22})
    ax.set_ylabel('Score', fontdict={'size': 17})
    ax.set_xticks(df.index)
    ax.set_xticklabels(df['task name'].str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size': 12})
    # ax.set_ylim(0, 30)

    # Annotate
    for row in df.itertuples():
        ax.text(row.Index, row._2, s=round(float(row._2), 2), horizontalalignment='center', verticalalignment='bottom',
                fontsize=17)

    plt.show()

draw_hardest_task()