from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from controller import Oauth
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


# 카카오 회원가입 반환
@app.route("/social-sign-up")
def social_sign_up_page():
    return render_template('social-sign-up.html')


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


@app.route('/api/favorite', methods=['GET'])
def board_favorite():
    response = favorites.show_favorite()
    return jsonify(response)


@app.route('/api/favorite/write', methods=['POST'])
def board_favorite_write():
    par = request.form['board_id']
    print("par : " + par)
    response = favorites.write_favorite(par)
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


# -------------------- 카카오 --------------------- #

# 카카오 서버로 로그인 요청
@app.route('/oauth/url')
def oauth_url_api():
    return jsonify(
        kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code"
                        % (CLIENT_ID, REDIRECT_URI)
    )


# 아예 redirect url을 /oauth로 줘서 여기로 redirect해주는구먼

# 카카오 서버로 유저 정보 요청
@app.route("/oauth")
def oauth_api():
    code = str(request.args.get('code'))  # 응답 신호 획득
    oauth = Oauth()  # 토큰들을 담는 객체 생성
    auth_info = oauth.auth(code)  # 토큰들 획득 및 저장
    print(auth_info)

    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    print(user)

    # session['token'] = auth_info['access_token']
    # 로그아웃에 사용될 세션 값 = 쿠키값

    # 로직: user안에 내가 입력한 정보(이름,번화번호)가 있으면 board로 redirect시켜주고 없을때는 추가정보입력하도록 social sign up으로 redirect해주기
    return redirect('http://localhost:5000/social-sign-up')  # 서비스 홈페이지로 redirect


@app.route("/oauth/userinfo", methods=['POST'])
def oauth_userinfo_api():
    access_token = request.get_json()['access_token']
    result = Oauth().userinfo("Bearer " + access_token)
    return jsonify(result)


def token_user_info(access_token):
    user_info = Oauth().userinfo("Bearer " + access_token)
    return user_info


# # 로그아웃 호출입. 세션 값 있으면 지우고 로그인 페이지로 렌더링
# @app.route("/oauth/logout")
# def logout():
#
#     # 카카오 로그아웃 요청 url
#     kakao_oauth_url = f"https://kauth.kakao.com/oauth/logout?client_id=" \
#                       f"{CLIENT_ID}&logout_redirect_uri={SIGNOUT_REDIRECT_URI}"
#
#
#     # 로그아웃 검사 로직
#     if session.get('token'):
#         session.clear()
#         value = {"status": 200, "result": "success"}
#     else:
#         value = {"status": 404, "result": "fail"}
#
#     return redirect('http://localhost:5000/board')

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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
