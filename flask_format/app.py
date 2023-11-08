from flask import Flask, render_template, request, session, redirect,flash, url_for

app = Flask(__name__)


# 編集ゾーンーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
##ここでルートのURLが指定された時に実行される
@app.route('/')
def index():
    ##index.htmlがレンダリングされる
    return render_template("index.html")

# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if __name__ == '__main__':
    app.run()


