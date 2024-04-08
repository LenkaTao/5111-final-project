import requests
from lxml import etree
import pandas as pd

# 豆瓣电影top250第一页
url = 'https://movie.douban.com/top250?start=0&filter='

# 防止反爬
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

# 使用列表获取10个页面的所有地址
urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i*25)) for i in range(10)]

# 获取列表第x个元素
# strip：处理两端空格
# try except：如果列表为空，返回空值
def get_first_text(list): # 列表第一个
    try:
        return list[0].strip()
    except:
        return ""
def get_second_text(list): # 列表第二个
    try:
        return list[1].strip()
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
df = pd.DataFrame(columns=['序号','标题','详情链接','图片链接','年份','地区','类型','信息','评分','评价人数','简介'])

count = 1
# 遍历10页
for url in urls:
    res = requests.get(url=url, headers=headers)
    html = etree.HTML(res.text)
    lis = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    # 在一页内遍历25部电影
    for li in lis:
        title = get_first_text(li.xpath('./div/div[2]/div[1]/a/span[1]/text()'))
        src = get_first_text(li.xpath('./div/div[2]/div[1]/a/@href'))
        picture = get_first_text(li.xpath('./div/div[1]/a/img/@src'))
        year = get_first_text(get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')).split('/'))[:4] # 只取前四位数字
        district =get_secondlast_text(get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')).split('/')) # 部分电影会有好几个年份，但地区一定是倒数第二个
        movie_type = get_last_text(get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')).split('/')) # 类型一定是最后一个
        info = get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()'))
        score = get_first_text(li.xpath('./div/div[2]/div[2]/div/span[2]/text()'))
        comment = get_first_text(li.xpath('./div/div[2]/div[2]/div/span[4]/text()'))[:-3] # 去掉“人评价”，只留下数字
        summary = get_first_text(li.xpath('./div/div[2]/div[2]/p[2]/span/text()'))
        print(count,title,src,picture,year,district,movie_type,info,score,comment,summary)
        df.loc[len(df.index)] = [count,title,src,picture,year,district,movie_type,info,score,comment,summary] # 填充表格
        count += 1 
 
# 输出excel表格 
df.to_excel('豆瓣电影top250原始数据.xlsx',sheet_name='豆瓣电影top250',na_rep='')