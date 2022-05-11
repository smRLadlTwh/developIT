from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import os
import board, favorites
import sign
from configs.config_local import CLIENT_ID, REDIRECT_URI

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
def index_page():
    return render_template('index.html')


# 로그인 페이지 반환
@app.route("/login")
def login_page():
    return render_template('login.html')


# 회원가입 반환
@app.route("/sign-up")
def sign_up_page():
    return render_template('sign-up.html')


# 프로필 페이지 반환
@app.route('/profile')
def profile_page():
    return render_template('profile.html')


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


# 페이지 내 header 부분 반환
@app.route("/header")
def header():
    return render_template('header.html')


# 페이지 내 footer 부분 반환
@app.route("/footer")
def footer():
    return render_template('footer.html')


# -------------------- API --------------------- #

# 게시글 업로드 API
@app.route("/api/board/write", methods=['POST'])
def board_write():
    response = board.board_write()
    return jsonify(response)


@app.route('/api/favorites', methods=['GET'])
def board_favorite():
    response = favorites.show_favorite()
    return jsonify(response)


# 게시글 전체 보여주기 API
@app.route("/api/board", methods=['GET'])
def board_entire_show():
    response = board.board_show()
    return jsonify(response)


# 로그인 API
@app.route('/api/login', methods=['POST'])
def sign_in():
    response = sign.sign_in()
    return jsonify(response)


# 회원가입 API
@app.route('/api/sign-up', methods=['POST'])
def sign_up():
    response = sign.sign_up()
    return jsonify(response)


# 이메일 중복 체크
@app.route('/api/email-duplicate check', methods=['POST'])
def email_duplicate_check():
    response = sign.email_duplicate_check()
    return jsonify(response)


@app.route('/oauth/url')
def oauth_url_api():
    return jsonify(
        kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
                        % (CLIENT_ID, REDIRECT_URI)
    )


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
