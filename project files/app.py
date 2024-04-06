from flask import Flask, url_for, redirect, render_template, request
from random_film import read_excel_to_df,random_film

app = Flask(__name__)

@app.route('/randomfilm')
def randomfilm():
    film_title,detail_link,pic_link,year,country,\
    info,genere,score,people_watched,brief_intro = random_film(read_excel_to_df('top250films.xlsx'))
    return render_template('randomfilm.html',\
                           film_title = film_title,detail_link = detail_link,pic_link = pic_link, year = year,\
                           country = country, info = info, genere = genere, score = score,\
                           people_watched = people_watched, brief_intro = brief_intro
                            )

@app.route('/') #如果网址只有一个/，会自动跳转到***/home
def index():
    return redirect(url_for('home'))

@app.route('/home') #如果是***/home，就返回home.html,也就是主页
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()