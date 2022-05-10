from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import os
import board
import sign

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


# 게시글 업로드 페이지 반환
@app.route("/board-upload")
def board_upload_page():
    return render_template('board-upload.html')


# 게시글 성공 시 게시글 성공 페이지 반환
@app.route("/board/write/success")
def board_upload_success_page():
    return render_template('board-upload-success.html')


# 게시글 실패 시 게시글 실패 페이지 반환
@app.route("/board/write/fail")
def board_upload_fail_page():
    return render_template('board-upload-fail.html')


# -------------------- API --------------------- #

# 게시글 업로드 API
@app.route("/api/board/write", methods=['POST'])
def board_write():
    response = board.board_write()
    return jsonify(response)


# 로그인 API
@app.route('/api/login', methods=['POST'])
def sign_in():
    response = sign.sign_in()
    return jsonify(response)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)