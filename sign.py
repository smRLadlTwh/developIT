from flask import jsonify, request
from datetime import datetime, timedelta
import jwt
import hashlib
from pymongo import MongoClient
import os

if os.environ['env'] == 'prod':
    from configs import config_prod as config

    client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)

db = client.developITdb

SECRET_KEY = config.security


def sign_in():
    user_id = request.form['id']
    user_pw = request.form['pw']

    # 패스워드를 해시함수 이용하여 해시값을 만듦
    pw_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()
    user = db.user.find_one({'user.id': user_id, 'user.password': pw_hash})

    if user is not None:
        payload = {
            'uuid': str(user['user']['uuid']),
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 6)  # 로그인 6시간 유지
        }
        # 시크릿 키를 이용하여 암호화
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return {"result": "success", "status_code": 200, "token": token}
    else:
        return {"result": "fail", "status_code": 401, "error_message": 'BAD_CREDENTIAL'}
