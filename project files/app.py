from flask import Flask, url_for, redirect, render_template, request
from random_film import random_film, random_book, random_music
import pandas as pd

app = Flask(__name__)

@app.route('/RandomMovie') #点击random film
def randomfilm():
    film_title,film_detail_link,film_pic_link,film_year,film_country,\
    film_info,film_director, film_actor, film_genere,film_score,film_people_watched,film_brief_intro = random_film(pd.read_excel('lists/top250films.xlsx'))
    return render_template('movie outcome.html',
                           film_title = film_title,film_detail_link = film_detail_link,film_pic_link = film_pic_link, film_year = film_year,\
                           film_country = film_country, film_info = film_info, film_director = film_director, film_actor = film_actor, film_genere = film_genere,\
                           film_score = film_score, film_people_watched = film_people_watched, film_brief_intro = film_brief_intro
                            )

@app.route('/randombook') #点击random book
def randombook():
    book_title,book_detail_link,book_pic_link,book_author,book_publisher,
    book_time,book_price,book_score,book_people_rated,book_brief_intro = random_book(pd.read_excel('lists/top250books.xlsx'))
    return render_template('home.html',
                           book_title = book_title,book_detail_link = book_detail_link,book_pic_link = book_pic_link,\
                           book_author = book_author,book_publisher = book_publisher,book_time = book_time, book_price = book_price,\
                           book_score = book_score,book_people_rated = book_people_rated,book_brief_intro = book_brief_intro
                            )

@app.route('/randommusic') #点击random music
def randommusic():
    music_title,music_detail_link,music_pic_link,music_singer,music_time,
    music_genere,music_medium,music_type,music_score, music_people_rated = random_music(pd.read_excel('lists/top250music.xlsx'))
    return render_template('home.html',
                           music_title = music_title,music_detail_link = music_detail_link,music_pic_link = music_pic_link,\
                           music_singer = music_singer,music_time = music_time,music_genere = music_genere,music_medium = music_medium,\
                           music_type = music_type,music_score = music_score, people_rated = music_people_rated
                            )

@app.route('/') #如果网址只有一个/，会自动跳转到***/home
def index():
    return redirect(url_for('home'))

@app.route('/home') #如果是***/home，就返回home.html,也就是主页
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)