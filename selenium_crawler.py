from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

URL = 'https://www.google.com'

driver.get(URL)

element = driver.find_element_by_name('q')
element.send_keys('손흥민 연도별 공격 포인트')
element.submit()

element = driver.find_element_by_css_selector('#rso > div:nth-child(3) > div > div > div > div.yuRUbf > a')
element.click()
