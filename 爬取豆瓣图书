import csv
import requests
from lxml import etree



HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',}

#定义获取书籍详情页面url的函数
def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    html_element = etree.HTML(response.text)
    detail_urls = html_element.xpath("//h2[@class='clearfix']//a/@href")
    return detail_urls



#定义获取书籍详细信息的函数
def get_detail_info(detail_url):
    response = requests.get(url=detail_url,headers=HEADERS)
    text = etree.HTML(response.content)
    #[ ] 用于访问数据结构中的元素。当你使用 [0] 时，表示访问数据结构（如列表、元组、字符串等）中的第一个元素。在这里，[0] 表示取得列表中的第一个元素，不使用则返回列表["文字"]，使用则返回 文字
    book_name = text.xpath("//h1/span/text()")
    author = text.xpath("//*[@id='info']/span[1]/a/text()")
    rating = text.xpath("//div[@id='interest_sectl']//strong/text()")

    # 确保列表非空后再访问第一个元素
    book_name = book_name[0] if book_name else ''
    author = author[0] if author else ''
    rating = rating[0] if rating else ''


    book_info = {
        "书籍名称":book_name,
        "作者":author,
        "评分":rating,
    }
    return(book_info)

# 先定义 CSV 文件的字段
fieldnames = ["书籍名称", "作者", "评分"]
# 初始化一个列表，用于保存所有的 book_info
all_book_info = []

for page in range(1, 12):
    page_url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={page}'
    detail_urls = get_detail_urls(page_url)
    
    for detail_url in detail_urls:
        book_info = get_detail_info(detail_url)
        all_book_info.append(book_info)
        print(book_info)

# 打开 CSV 文件并写入所有的 book_info
with open('book_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入标题
    writer.writeheader()

    # 写入所有数据行
    writer.writerows(all_book_info)
    
    
