import uuid

from flask import jsonify, request, session
from datetime import datetime, timedelta
import jwt
import hashlib
from pymongo import MongoClient
import os

import app

if os.environ['env'] == 'prod':
    client = MongoClient(f'{os.environ["host"]}', 27017, username=f'{os.environ["user"]}',
                         password=f'{os.environ["password"]}')
    SECRET_KEY = os.environ["security"]
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)
    SECRET_KEY = config.security

db = client.developITdb


# 소셜 로그인
def social_sign_in(email):
    exists = bool(db.user.find_one({"user.e_mail": email}))
    if exists:
        user = db.user.find_one({'user.e_mail': email})
        payload = {
            'uuid': str(user['user']['uuid']),
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 6),  # 로그인 6시간 유지
            'type': 'social'
        }
        # 시크릿 키를 이용하여 암호화
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    else:
        return False


# 로그인
def sign_in():
    user_email = request.form['email']
    user_pw = request.form['pw']

    # 패스워드를 해시함수 이용하여 해시값을 만듦
    pw_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()
    user = db.user.find_one({'user.e_mail': user_email, 'user.password': pw_hash})

    if user is not None:
        payload = {
            'uuid': str(user['user']['uuid']),
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 6),  # 로그인 6시간 유지
            'type': 'general'
        }
        # 시크릿 키를 이용하여 암호화
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return {"result": "success", "status_code": 200, "token": token}
    else:
        return {"result": "fail", "status_code": 401, "error_message": 'BAD_CREDENTIAL'}


# 회원가입
def sign_up():
    if 'access_token' in session:
        user_email = app.user_kakao_email()
        user_pw = 'social'
    else:
        user_email = request.form['email']
        user_pw = request.form['password']
    name = request.form['name']
    phone_number = request.form['phone_number']
    phone_number_replace = phone_number.replace("-", "")

    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')

    password_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()
    user_uuid = str(uuid.uuid4())

    print('user_uuid = ' + user_uuid)
    doc = {
        'user': {
            "uuid": str(user_uuid),
            "e_mail": user_email,
            "password": password_hash,
            "name": name,
            "phone_number": phone_number_replace,
            "created_at": time
        }
    }
    print('------ user_insert ------')
    print(doc)
    db.user.insert_one(doc)

    if 'access_token' in session:
        payload = {
            'uuid': str(user_uuid),
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 6),  # 로그인 6시간 유지
            'type': 'social'
        }
        print('-----payload----')
        print(payload)
        # 시크릿 키를 이용하여 암호화
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        print('-----token----')
        print(token)
        return {'result': 'success', 'status_code': 201, "token": token}
    else:
        return {'result': 'success', 'status_code': 201}


# 이메일 중복 체크
def email_duplicate_check():
    user_email = request.form['email']
    exists = bool(db.user.find_one({"user.e_mail": user_email}))

    return {'result': 'success', 'exists': exists}
