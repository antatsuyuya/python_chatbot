import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    """
        **** ここを実装します（基礎課題） ****

        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """

#1. はてブのホットエントリーページのHTMLを取得する
#2. BeautifulSoupでHTMLを読み込む
#3. 記事一覧を取得する
    with urlopen("https://b.hatena.ne.jp/") as res:
        html = res.read().decode("utf-8") #バイナリ⇒utf-8に変更
    soup=BeautifulSoup(html,"html.parser")
    # titles =soup.select("a.js-keyboard-openable")
    # titles = [t.string for t in titles] #h2タイトル文字列を抜き出す

    articles = soup.find_all(class_="entrylist-contents-title")

# with open('mydata.json', mode='wt', encoding='utf-8') as file:
#   json.dump(object, file, ensure_ascii=False, indent=2)

#4. ランダムに1件取得する
    import random
    article = random.choice(articles)

    for a in article.select("a"):
        titles = a.get('title')
        # print(titles)
        urls = a.get('href')
        # print(urls)

    # from pprint import pprint
    # print(titles)
    # print(urls)

#5. 以下の形式で返却する.
    return json.dumps({
        "content" : titles,
        "link" : urls
    })

# @app.route("/api/xxxx")
# def api_xxxx():
#     """
#         **** ここを実装します（発展課題） ****
#         ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
#         ・お天気APIなども良いかも
#         ・関数名は適宜変更してください
#     """
#     pass

# if __name__ == "__main__":
#     app.run(debug=True, port=5004)
