from selenium import webdriver
import time
import datetime
import pandas as pd

url = "https://hiskio.com/"
PATH = "D:\OneDrive\Development\Tools\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(url)

time.sleep(3)
# 先將網頁中"最新課程"的區塊找出來，此時latest_courses是webdriver object
latest_courses = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[5]/div/section[5]/div[3]/div/ul')

# 在最新課程這個區塊中的去搜尋課程名稱、老師、價格所儲存的欄位(在class的設定比較複雜時，我偏好使用xpath比較好找)
course_title_elements = latest_courses.find_elements_by_css_selector("h3")
instructor_elements = latest_courses.find_elements_by_xpath('//*[@id="__layout"]/div/div[5]/div/section[5]/div[3]/div/ul/li/a/div[1]/div[2]/div[2]/p[1]')
price_elements = latest_courses.find_elements_by_xpath('//*[@id="__layout"]/div/div[5]/div/section[5]/div[3]/div/ul/li/a/div[1]/div[2]/div[2]/p[2]')

# 用for loop 印出這些elements中所有的文字並存成3組list
course_titles = []
for course in course_title_elements:
    course_titles.append(course.text)
instructors = []
for instructor in instructor_elements:
    instructors.append(instructor.text)
prices = []
for price in price_elements:
    prices.append(price.text)

# 使用pandas DataFrame將結果輸出為易讀表格
latest_courses_info = pd.DataFrame({
    '課程名稱': course_titles,
    '老師名稱': instructors,
    '價格': prices
})
print(latest_courses_info)

# 存為csv檔，如果後續需要追蹤，可在檔名加上日期
date = datetime.date.today()
latest_courses_info.to_csv(f"{date}_hiskio最新課程.csv", encoding="utf_8_sig")
