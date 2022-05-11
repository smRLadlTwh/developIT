import boto3
from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort
import datetime
import json
import jwt
import os
import uuid
from werkzeug.utils import secure_filename
import re

from pymongo import MongoClient

if os.environ['env'] == 'prod':
    client = MongoClient(f'{os.environ["host"]}', 27017, username=f'{os.environ["user"]}',
                         password=f'{os.environ["password"]}')
    SECRET_KEY = os.environ["security"]
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)
    SECRET_KEY = config.security

db = client.developITdb


# 게시물을 등록하는 API
def board_write():
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')
    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        if user_info is None:
            abort(404, '회원 정보가 존재하지 않습니다.')

        board = []
        if user_info.get('boards') is not None:
            board = user_info['boards']
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')

        board_uuid = str(uuid.uuid4())

        # 유저로부터 받은 데이터
        title = request.form["title"]
        content = request.form["content"]
        cost = request.form["cost"]

        doc = {
            "uuid": board_uuid,
            "title": title,
            "content": content,
            "cost": cost,
            "created_at": time,
        }

        file_path = "default_image.jpeg"

        if 'image' in request.files:
            file = request.files["image"]
            filename = secure_filename(file.filename)
            extension = filename.split(".")[-1]
            file_path = f"{time}.{extension}"
            doc["image_url"] = file_path

            s3 = boto3.client('s3', aws_access_key_id=config.aws_access_key,
                              aws_secret_access_key=config.aws_secret_key)
            s3.put_object(
                ACL="public-read",
                Bucket="devit-bucket",
                Body=file,
                Key=file_path,
                ContentType=file.content_type)

        board.append(doc)

        db.user.update_one({'user.uuid': str(payload["uuid"])}, {'$set': {'boards': board}})

        doc = {
            'user': {
                "uuid": str(user_info['user']['uuid']),
                "e_mail": user_info['user']['e_mail'],
                "password": user_info['user']['password'],
                "name": user_info['user']['name'],
                "created_at": user_info['user']['created_at'],
                'phone_number': user_info['user']['phone_number'],
            },
            'board': {
                "uuid": board_uuid,
                "title": title,
                "content": content,
                "cost": cost,
                "created_at": time,
                'image_url': file_path,
            }
        }

        db.board.insert_one(doc)

        return {"result": "success", "status_code": 201}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}
    except jwt.exceptions.DecodeError:
        return {"result": "success", "status_code": 400, "error_message": 'INVALID_TOKEN'}


# 게시물 전체 보여주기
def board_show():
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')
    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})
        if user_info is None:
            abort(404, '회원 정보가 존재하지 않습니다.')

        if request.args.get('page') is not None and request.args.get('page') != 'null':
            page = int(request.args.get('page'))
        else:
            page = 1
        if request.args.get('pageSize') is not None:
            page_size = int(request.args.get('pageSize'))
        else:
            page_size = 5

        # 검색어가 있는 경우
        if request.args.get('search') is not None or request.args.get('search') == '':
            search = ".*" + request.args.get('search') + ".*"
            like_search = re.compile(search, re.IGNORECASE)
            boards = list(
                db.board.find({"$or": [{'board.title': like_search}, {'board.content': like_search}]},
                              {'_id': False}).sort('board.created_at', -1).skip((page - 1) * page_size).limit(
                    page_size))
            count = len(list(
                db.board.find({"$or": [{'board.title': like_search}, {'board.content': like_search}]},
                              {'_id': False}).sort('board.created_at', -1)))
        # 검색어가 없는 경우
        else:
            boards = list(
                db.board.find({}, {'_id': False}).sort('board.created_at', -1).skip((page - 1) * page_size).limit(
                    page_size))
            count = len(list(
                db.board.find({}, {'_id': False}).sort('board.created_at', -1)))

        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')

        response = {
            'result': 'success',
            'time': time,
            'total': count,
            'data': {
                'boards': boards
            },
            'status_code': 201
        }

        return response
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}
    except jwt.exceptions.DecodeError:
        return {"result": "success", "status_code": 400, "error_message": 'INVALID_TOKEN'}
