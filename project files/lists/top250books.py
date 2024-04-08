import requests
from lxml import etree
import pandas as pd

# 豆瓣图书top250第一页
url = 'https://book.douban.com/top250?start=25'

# 防止反爬
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

# 使用列表获取10个页面的所有地址
urls=['https://book.douban.com/top250?start={}'.format(str(i*25)) for i in range(10)]

# 获取列表第x个元素
# strip：处理两端空格
# try except：如果列表为空，返回空值
def get_first_text(list): # 列表第一个
    try:
        return list[0].strip()
    except:
        return ""
def get_thirdlast_text(list): # 列表倒数第三个
    try:
        return list[-3].strip()
    except:
        return ""
def get_secondlast_text(list): # 列表倒数第二个
    try:
        return list[-2].strip()
    except:
        return ""
def get_last_text(list):  # 列表倒数第一个
    try:
        return list[-1].strip()
    except:
        return ""

# 列标签
df = pd.DataFrame(columns=['序号','标题','详情链接','图片链接','作者','出版社','出版时间','价格','评分','评价人数','简介'])

count = 1
# 遍历10页
for url in urls:
    res = requests.get(url=url, headers=headers)
    html = etree.HTML(res.text)
    lis = html.xpath('//*[@id="content"]/div/div[1]/div/table')
    # 在一页内遍历25本图书
    for li in lis:
        title = get_first_text(li.xpath('./tr/td[2]/div[1]/a/text()'))
        src = get_first_text(li.xpath('./tr/td[2]/div[1]/a/@href'))
        picture = get_first_text(li.xpath('./tr/td[1]/a/img/@src'))
        author = get_first_text(get_first_text(li.xpath('./tr/td[2]/p[1]/text()')).split('/')) # 作者是第一个
        press = get_thirdlast_text(get_first_text(li.xpath('./tr/td[2]/p[1]/text()')).split('/')) # 出版社是倒数第三个
        time = get_secondlast_text(get_first_text(li.xpath('./tr/td[2]/p[1]/text()')).split('/')) # 出版时间是倒数第一个
        price = get_last_text(get_first_text(li.xpath('./tr/td[2]/p[1]/text()')).split('/'))[:-1] # 价格是最后一个,去掉“元”，只留数字
        score = get_first_text(li.xpath('./tr/td[2]/div[2]/span[2]/text()'))
        comment = get_first_text(li.xpath('./tr/td[2]/div[2]/span[3]/text()')).splitlines()[1].strip()[:-3] # 去掉前后空格和“人评价”，只留数字
        summary = get_first_text(li.xpath('./tr/td[2]/p[2]/span/text()'))
        print(count,title,src,picture,author,press,time,price,score,comment,summary)
        df.loc[len(df.index)] = [count,title,src,picture,author,press,time,price,score,comment,summary] # 填充表格
        count += 1 
 
# 输出excel表格 
df.to_excel('豆瓣图书top250原始数据.xlsx',sheet_name='豆瓣图书top250',na_rep='')

   