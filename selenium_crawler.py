from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

URL = 'https://www.google.com'

driver.get(URL)

element = driver.find_element_by_name('q')
element.send_keys('손흥민 연도별 공격 포인트')
element.submit()

element = driver.find_element_by_css_selector('#rso > div:nth-child(3) > div > div > div > div.yuRUbf > a')
element.click()

list_son = []
x_season = []
y_goal = []
y_assist = []

table = driver.find_elements_by_tag_name('table')
tbody = table[3].find_elements_by_tag_name('tbody')
tr_list= tbody[0].find_elements_by_tag_name('tr')
for tr in tr_list:
    tr_td_list = tr.find_elements_by_tag_name('td')
    for td in tr_td_list:
        list_son.append(td.text)

for i in range(99, 185, 17):
    x_season.append(list_son[i])
print(x_season)
for i in range(114, 200, 17):
    y_goal.append(list_son[i])
print(y_goal)
for i in range(115, 201, 17):
    y_assist.append(list_son[i])
print(y_assist)

x = np.arange(6)
y = np.arange(6)
y1 = [int(i) for i in y_goal]
y2 = [int(i) for i in y_assist]

plt.xticks(x, x_season)
plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)
plt.show()

















