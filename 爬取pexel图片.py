import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import time
from lxml import etree

def get_img_urls(url, scroll_iterations=50):
    # 创建 ChromeDriver
    chrome_service = ChromeService()
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(url)

    # 使用延迟等待确保页面加载完成
    driver.implicitly_wait(10)

    # 模拟鼠标滚动
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(scroll_iterations):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # 使用XPath表达式找到所有匹配的img元素
    img_elements = driver.find_elements(By.XPATH, '//div[@class="BreakpointGrid_column__CTepl"]//img')

    # 获取每个img元素的src属性
    img_urls = [img_element.get_attribute("src") for img_element in img_elements]
    driver.close()

    return img_urls

#构造下载图片的函数
def download_image(image_url, save_directory):
    try:
        # 发送HTTP GET请求到图像URL并以流的方式获取内容
        response = requests.get(image_url, stream=True)
        
        # 如果响应状态码为4xx或5xx，引发HTTPError以处理错误
        response.raise_for_status()

        # 获取指定目录中已存在的文件数量
        existing_files = len(os.listdir(save_directory))

        # 构造保存图像的路径，使用递增的数字作为文件名
        save_path = os.path.join(save_directory, f"{existing_files + 1}.jpg")

        # 以二进制写入模式打开文件，并将图像内容写入其中
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        # 打印成功的消息，包括保存的路径
        print(f"成功下载并保存图像到 {save_path}")

    except requests.exceptions.RequestException as e:
        # 处理请求过程中可能发生的任何异常
        print(f"下载图像时发生错误：{e}")

# 示例用法
kw = input('欢迎使用 pexels 图片搜索下载神器\n请输入搜索关键词(英文)：')
url = f'https://www.pexels.com/zh-cn/search/{kw}/'
image_urls = get_img_urls(url,scroll_iterations=50)
save_directory = 'd:\download\img'

for img_url in image_urls:
    download_image(img_url, save_directory)
