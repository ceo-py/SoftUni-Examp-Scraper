from selenium import webdriver
from selenium.webdriver.common.by import By
from requests_html import HTML
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.headless = False
PATH = r"D:\PyCharm\amazon items\chromedriver.exe"
url = "https://judge.softuni.org/Contests/Compete/Results/Simple/3477"
user_name = "mljam"
password = "123456yU"
driver = webdriver.Chrome(PATH, options=options)
driver.get(url)

username_find = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[2]/div/input')
username_find.send_keys(user_name)
password_find = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[3]/div/input')
password_find.send_keys(password)
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[5]/div/input')
submit_button.click()
html_data = driver.page_source
r_html = HTML(html=html_data)

examp_info = {}
def get_info_from_web():
    for contestant in range(1, 101):
        total_score = int(r_html.xpath(f'/html/body/div[2]/div/table/tbody/tr[{contestant}]/td[19]', first=True).text)
        examp_info["total_score"] = examp_info.get("total_score", [])
        examp_info["total_score"].append(total_score)
        for examp in range(4, 19):
            task_name = r_html.xpath(f'/html/body/div[2]/div/table/thead/tr/th[{examp}]', first=True).text
            task_score = r_html.xpath(f'/html/body/div[2]/div/table/tbody/tr[{contestant}]/td[{examp}]', first=True).text
            examp_info[task_name] = examp_info.get(task_name, [])
            if task_score.isdigit():
                examp_info[task_name].append(int(task_score))


get_info_from_web()
# print(examp_info)
# print(len(examp_info['total_score']))
#
# first_task = '/html/body/div[2]/div/table/thead/tr/th[4]'
# last_tank = '/html/body/div[2]/div/table/thead/tr/th[18]'
#
# first_contest_first_task = '/html/body/div[2]/div/table/tbody/tr[1]/td[4]'
# first_contest_last_task = '/html/body/div[2]/div/table/tbody/tr[1]/td[18]'
# first_contest_total_score = '/html/body/div[2]/div/table/tbody/tr[1]/td[19]'
#
# second_contest_first_task = '/html/body/div[2]/div/table/tbody/tr[2]/td[4]'
# second_contest_last_task = '/html/body/div[2]/div/table/tbody/tr[2]/td[18]'
# second_contest_total_score = '/html/body/div[2]/div/table/tbody/tr[2]/td[19]'
#

def write_json(data, filename="examp_info.json"):
    with open(filename, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=9)


with open("examp_info.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data["SoftUni"]["Info"]
    data_info.append(examp_info)

write_json(data)
