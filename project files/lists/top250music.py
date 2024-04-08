import requests
from lxml import etree
import pandas as pd

# 豆瓣音乐top250第一页
url = 'https://music.douban.com/top250?start=0'

# 防止反爬
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

# 使用列表获取10个页面的所有地址
urls=['https://music.douban.com/top250?start={}'.format(str(i*25)) for i in range(10)]

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
df = pd.DataFrame(columns=['序号','标题','详情链接','图片链接','歌手','发行时间','类型','介质','流派','评分','评价人数'])

count = 1
# 遍历10页
for url in urls:
    res = requests.get(url=url, headers=headers)
    html = etree.HTML(res.text)
    lis = html.xpath('//*[@id="content"]/div/div[1]/div/table')
    # 在一页内遍历25首音乐
    for li in lis:
        title = get_first_text(li.xpath('./tr/td[2]/div/a/text()'))
        src = get_first_text(li.xpath('./tr/td[2]/div/a/@href'))
        picture = get_first_text(li.xpath('./tr/td[1]/a/img/@src'))
        singer = get_first_text(get_first_text(li.xpath('./tr/td[2]/div/p[1]/text()')).split('/')) # 歌手是那一排第一个
        time = get_second_text(get_first_text(li.xpath('./tr/td[2]/div/p[1]/text()')).split('/')) # 发行时间是第二个
        type = get_thirdlast_text(get_first_text(li.xpath('./tr/td[2]/div/p[1]/text()')).split('/')) # 类型是倒数第三个
        medium = get_secondlast_text(get_first_text(li.xpath('./tr/td[2]/div/p[1]/text()')).split('/')) # 介质是倒数第二个
        school = get_last_text(get_first_text(li.xpath('./tr/td[2]/div/p[1]/text()')).split('/')) # 流派是最后一个
        score = get_first_text(li.xpath('./tr/td[2]/div/div/span[2]/text()'))
        comment = get_first_text(li.xpath('./tr/td[2]/div/div/span[3]/text()')).splitlines()[1].strip()[:-3] # 去掉前后空格和“人评价”，只留下数字
        print(count,title,src,picture,singer,time,type,medium,school,score,comment)
        df.loc[len(df.index)] = [count,title,src,picture,singer,time,type,medium,school,score,comment] # 填充表格
        count += 1 
 
# 输出excel表格 
df.to_excel('豆瓣音乐top250原始数据.xlsx',sheet_name='豆瓣音乐top250',na_rep='')