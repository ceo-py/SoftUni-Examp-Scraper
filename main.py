from selenium import webdriver
from selenium.webdriver.common.by import By
from requests_html import HTML
from selenium.webdriver.chrome.options import Options
import json

## browser settings
options = Options()
options.headless = False
PATH = r"D:\PyCharm\amazon items\chromedriver.exe"
url = input("Enter URL FROM PAGE 1 : ")
driver = webdriver.Chrome(PATH, options=options)
driver.get(url)

user_name = "2qe22e2eqwe"
password = "q2eq2eqwewqe"

pages_to_search = int(input("Enter pages: "))
tasks_on_page = int(int(input("Enter task per page: ")))
ADDED_FIELD_FOR_TASK = 4

username_find = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[2]/div/input')
username_find.send_keys(user_name)
password_find = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[3]/div/input')
password_find.send_keys(password)
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/form/div[5]/div/input')
submit_button.click()
html_data = driver.page_source
r_html = HTML(html=html_data)
examp_info = {}


def get_info_from_web(examp_info, r_html):
    for contestant in range(1, 101):
        try:
            total_score = int(r_html.xpath(
                f'/html/body/div[2]/div/table/tbody/tr[{contestant}]/td[{tasks_on_page + ADDED_FIELD_FOR_TASK}]',
                first=True).text)
            examp_info["total_score"] = examp_info.get("total_score", [])
            examp_info["total_score"].append(total_score)
            for examp in range(4, tasks_on_page + ADDED_FIELD_FOR_TASK):
                task_name = r_html.xpath(f'/html/body/div[2]/div/table/thead/tr/th[{examp}]', first=True).text
                task_score = r_html.xpath(f'/html/body/div[2]/div/table/tbody/tr[{contestant}]/td[{examp}]',
                                          first=True).text
                examp_info[task_name] = examp_info.get(task_name, [])
                if task_score.isdigit():
                    examp_info[task_name].append(int(task_score))

        except:
            return


def load_next_url(pages_to_search):
    try:
        for page in range(2, pages_to_search + 1):
            driver.get(f"{url[:-1]}{page}")
            html_data = driver.page_source
            r_html = HTML(html=html_data)
            get_info_from_web(data_info, r_html)
    except:
        return


def write_json(data, filename="test.json"):
    with open(filename, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=9)


with open("test.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data
    get_info_from_web(data_info, r_html)
    load_next_url(pages_to_search)

write_json(data)
