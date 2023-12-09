import requests
from datetime import datetime
from lxml import html
import csv
import time
from selenium import webdriver

#构造获取详情页的函数
def fetch_links(page_index):  
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query"
    params = {
        'timestamp': int(datetime.timestamp(datetime.now()) * 1000),
        'countryId': '',
        'cityId': '',
        'bgIds': '',
        'productId': '',
        'categoryId': '40001001,40001002,40001003,40001004,40001005,40001006',
        'parentCategoryId': '',
        'attrId': '1',
        'keyword': '',
        'pageIndex': page_index,
        'pageSize': 10,
        'language': 'zh-cn',
        'area': 'cn',
    }

    # 发送请求
    response = requests.get(base_url, params=params)

    # 处理响应
    if response.status_code == 200:
        data = response.json()
        links = [post['PostURL'] for post in data.get('Data', {}).get('Posts', [])]
        return links
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def get_detail_info(link):
    # 使用 ChromeDriver
    chrome_options = webdriver.ChromeOptions()

    # 在无头模式下运行，无需打开浏览器窗口
    chrome_options.add_argument('--headless')  

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    
    # 使用延迟等待确保页面加载完成（可以根据实际情况调整等待时间）
    time.sleep(2)

    # 获取网页源码
    page_source = driver.page_source

    # 使用 lxml 解析源码
    tree = html.fromstring(page_source)

    # 在这里可以使用 tree 来执行 XPath 查询等操作
    title = tree.xpath("//div[@class='job-text-wrapper']/span/text()")
    duty = tree.xpath("//div[@class='duty work-module']//li/text()")
    requirements = tree.xpath("//div[@class='requirement work-module']//li/text()")
    add_points = tree.xpath("//div[@class='work-module']//li/text()")
    
    #使用xpath语法提取需要的信息
    detail_info = {
        'title': title[0] if title else None,
        'duty': duty[0] if duty else None,
        'requirements': requirements[0] if requirements else None,
        'add_points': add_points[0] if add_points else None,
        "link": link
    }
    # 关闭浏览器
    driver.close()
    return detail_info
    
#定义一个空列表
all_details = []

#遍历详情页获取信息
for page_index in range(1, 3):
    links = fetch_links(page_index)
    if links:
        for link in links:
            detail_info = get_detail_info(link)
            print(detail_info)
            all_details.append(detail_info)
            
    print("正在打印第{}页".format(page_index))
    

field_names = ['title', 'duty', 'requirements', 'add_points', 'link']

# 将详细信息保存为 CSV 文件
with open('details.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    
    # 写入 CSV 文件头部
    writer.writeheader()
    
    # 写入详细信息
    writer.writerows(all_details)

print("Details saved to 'details.csv'")
