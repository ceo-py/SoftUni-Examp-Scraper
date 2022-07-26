import json

with open("basic_23_24_july_2022.json", "r", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data


def task_frequency(data_info):
    print("\nHardest task : \n")
    for task_name, task_scores in sorted(data_info.items(), key=lambda x: (sum(x[1]) / len(x[1]))):
        if task_name != 'total_score':
            print(f"{task_name} average score {(sum(task_scores) / len(task_scores)):.2f} "
                  f"/ 100, with {len(task_scores)} contestants attempt the task!")


def task_with_max_score(data_info):
    print("\nTask with highest score: \n")
    num_high_score = {}
    for task_name, task_scores in data_info.items():
        if task_name != 'total_score':
            num_high_score[task_name] = num_high_score.get(task_name, 0)
            for score in task_scores:
                if score == 100:
                    num_high_score[task_name] += 1
    for task_name, task_score in sorted(num_high_score.items(), key= lambda x: -x[1]):
        print(f"{task_name} has {task_score} contestants with maximum score out of {len(data_info[task_name])} attempted the task!")





students_info = {"6.00": 0,
                 "5.00+": 0,
                 "4.00+": 0,
                 "3.00+": 0,
                 "2.00": 0,
                 "Not attempt any task": 0}

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

total_contestants = len(data_info['total_score'])
print(f"Total Contestants : {total_contestants}")
print("\nContestants Scores :\n")
for score, number_people in students_info.items():
    print(f"{score} - {number_people} / {total_contestants}, {((number_people / total_contestants) * 100):.2f}%")


print(f"\n{((sum(list(students_info.values())[:3])/ total_contestants)*100):.2f}% passed the test, Congrats !!!")
task_frequency(data_info)
task_with_max_score(data_info)

