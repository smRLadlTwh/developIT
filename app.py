from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import os
import board, favorites

app = Flask(__name__)

if os.environ['env'] == 'prod':
    from configs import config_prod as config

    client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)

db = client.developITdb


# -------------------- 페이지 반환 --------------------- #
# 게시글 페이지 반환
@app.route("/board")
def board_page():
    return render_template('board.html')


# 메인 페이지 반환
@app.route("/")
def index():
    return render_template('index.html')

# 프로필 페이지 반환
@app.route('/profile')
def profile():
    return render_template('profile.html')


# -------------------- API --------------------- #

# 게시글 업로드 API
@app.route("/api/board/write", methods=['POST'])
def board_write():
    response = board.board_write()
    return jsonify(response)

@app.route('/api/favorites', methods=['GET'])
def board_entire_show():
    response = favorites.show_favorite()
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
