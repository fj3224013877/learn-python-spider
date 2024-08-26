
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time


# 构造函数获取歌手信息
def get_artists(url):
    # 使用 Chrome 浏览器
    driver = webdriver.Chrome()
    # 打开 url
    driver.get(url)
    # 等待3s
    time.sleep(3)
    # 一共下滑70次，下滑一次停顿0.5s
    for i in range(70):
        # 将滚动条下滑到页面底部
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        # 等待0.5s
        time.sleep(0.5)
    # 获取网页的 html
    web_date = driver.page_source
    # 使用 BeautifulSoup 解析 html
    soup = BeautifulSoup(web_date, 'lxml')

    # 获取歌手信息
    artists = soup.find_all('a', class_='singer_list_txt__link js_singer')
    for artist in artists:
        # 获取歌手名字
        artist_name = artist.string
        # 获取歌手id
        artist_id = artist['href'].replace('/n/ryqq/singer/', '').strip()
        try:
            # 将歌手id和名字写入 csv 文件
            writer.writerow((artist_id, artist_name))
        except Exception as msg:
            # 如果写入失败，打印错误信息
            print(msg)

    # 关闭浏览器
    driver.quit()


# 文件存储的位置
csvfile = open("C:/Users/123/Desktop/python/qq.csv", 'a', encoding='utf-8')
# csv.writer()函数返回的是一个writer对象
writer = csv.writer(csvfile)
# 写入表头
writer.writerow(('artist_id', 'artist_name'))
# 获取歌手信息的 url
url = "https://y.qq.com/n/ryqq/singer_list?index=-100&genre=-100&sex=-100&area=-100"
# 调用构造函数
get_artists(url)
