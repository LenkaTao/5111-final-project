import pandas as pd


def random_film(film_list): #film_list is a dataframe
    a_film = film_list.sample(n=1)
    film_title = a_film.loc[:,'标题'].to_string(index=False, header=False)
    film_detail_link = a_film.loc[:,'详情链接'].to_string(index=False, header=False)
    film_pic_link = a_film.loc[:,'图片链接'].to_string(index=False, header=False)
    film_year = a_film.loc[:,'年份'].to_string(index=False, header=False)
    film_country = a_film.loc[:,'地区'].to_string(index=False, header=False)
    film_info = a_film.loc[:,'信息'].to_string(index=False, header=False)
    film_director = film_info.split('主演')[0].strip()[4:]
    film_actor = film_info.split('主演:')[1]
    if '\\' in film_actor:
        film_actor = acotr.split('/')[0]
    film_genere = a_film.loc[:,'类型'].to_string(index=False, header=False)
    film_score = a_film.loc[:,'评分'].to_string(index=False, header=False)
    film_people_watched = a_film.loc[:,'评价人数'].to_string(index=False, header=False)
    film_brief_intro = a_film.loc[:,'简介'].to_string(index=False, header=False)
    #返回搜索的视频平台超链接
    #tencentvideo_link = 'https://v.qq.com/x/search/?q='+ film_title
    #iqiyi_link = 'https://www.iq.com/search?query=' + film_title + '% &originInput=' + film_title
    #youku_link = 'https://so.youku.com/search_video/q_' + film_title + '?searchfrom=1'
    return film_title,film_detail_link,film_pic_link,film_year,\
    film_country,film_info,film_director,film_actor,\
    film_genere,film_score,film_people_watched,film_brief_intro

def random_book(book_list): #book_list is a dataframe
    a_book = book_list.sample(n=1)
    book_title = (a_book.loc[:,'标题']).to_string(index=False, header=False)
    book_detail_link = a_book.loc[:,'详情链接'].to_string(index=False, header=False)
    book_pic_link = a_book.loc[:,'图片链接'].to_string(index=False, header=False)
    book_author = a_book.loc[:,'作者'].to_string(index=False, header=False)
    book_publisher = a_book.loc[:,'出版社'].to_string(index=False, header=False)
    book_time = a_book.loc[:,'出版时间'].to_string(index=False, header=False)
    book_price = a_book.loc[:,'价格'].to_string(index=False, header=False)
    book_score = a_book.loc[:,'评分'].to_string(index=False, header=False)
    book_people_rated = a_book.loc[:,'评价人数'].to_string(index=False, header=False)
    book_brief_intro = a_book.loc[:,'简介'].to_string(index=False, header=False)
    return book_title,book_detail_link,book_pic_link,book_author,book_publisher,\
    book_time,book_price,book_score,book_people_rated,book_brief_intro

def random_music(music_list): #music_list is a dataframe
    a_music = music_list.sample(n=1)
    music_title = (a_music.loc[:,'标题']).to_string(index=False, header=False)
    music_detail_link = a_music.loc[:,'详情链接'].to_string(index=False, header=False)
    music_pic_link = a_music.loc[:,'图片链接'].to_string(index=False, header=False)
    music_singer = a_music.loc[:,'歌手'].to_string(index=False, header=False)
    music_time = a_music.loc[:,'发行时间'].to_string(index=False, header=False)
    music_genere = a_music.loc[:,'类型'].to_string(index=False, header=False)
    music_medium = a_music.loc[:,'介质'].to_string(index=False, header=False)
    music_type = a_music.loc[:,'流派'].to_string(index=False, header=False)
    music_score = a_music.loc[:,'评分'].to_string(index=False, header=False)
    music_people_rated = a_music.loc[:,'评价人数'].to_string(index=False, header=False)
    return music_title,music_detail_link,music_pic_link,music_singer,\
    music_time,music_genere,music_medium,music_type,music_score, music_people_rated

if __name__ == '__main__':
    #Test
    #random film
    film_title,film_detail_link,film_pic_link,film_year,film_country,\
    film_info,film_genere,film_score,film_people_watched,film_brief_intro,film_director,film_actor\
    = random_film(pd.read_excel('lists/top250films.xlsx'))
    print(f'{film_title}\n{film_detail_link}\n{film_director}\n{film_actor}')
    #random book
    a,b,c,d,e,f,g,h,i,j = random_book(pd.read_excel('lists/top250books.xlsx'))
    print(f'{a}\n{b}\n{c}\n{i}')
    #random music
    a,b,c,d,e,f,g,h,i,j = random_music(pd.read_excel('lists/top250music.xlsx'))
    print(f'{a}\n{b}\n{c}\n{i}')

    #类型数数
    film_type = pd.read_excel('lists/top250films.xlsx').loc[:,'类型']
    type_list = []
    for i in range(film_type.shape[0]):
        the_types = film_type.loc[i:].to_string(index=False, header=False).split()
        for j in range(len(the_types)):
            type_list.append(the_types[j])
    print(list(set(type_list)))