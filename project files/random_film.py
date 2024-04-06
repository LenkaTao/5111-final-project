import pandas as pd

def read_excel_to_df(file):
    return pd.read_excel(file)

def random_film(film_list): #film_list is a dataframe
    a_film = film_list.sample(n=1)
    film_title = a_film.loc[:,'标题']
    detail_link = a_film.loc[:,'详情链接']
    pic_link = a_film.loc[:,'图片链接']
    year = a_film.loc[:,'年份']
    country = a_film.loc[:,'地区']
    info = a_film.loc[:,'信息']
    genere = a_film.loc[:,'类型']
    score = a_film.loc[:,'评分']
    people_watched = a_film.loc[:,'评价人数']
    brief_intro = a_film.loc[:,'简介']
    return film_title,detail_link,pic_link,year,country,info,genere,score,people_watched,brief_intro

if __name__ == '__main__':
    # Test
    a,b,c,d,e,f,g,h,i,j = random_film(read_excel_to_df('top250films.xlsx'))
    print(a,b,j)
