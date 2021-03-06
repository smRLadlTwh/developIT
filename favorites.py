from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort
import datetime
import json
import jwt
import os
import uuid
from bson.json_util import dumps

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


# 즐겨찾기 목록 불러오는 API
def write_favorite(par):
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')

    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        # 게시글 아이디 받아옴
        board_uuid = str(par)

        # 게시글 정보들 받아옴 -> 즐겨찾기에 등록하기 위함
        board = db.board.find_one({"board.uuid": board_uuid})
        print("board : ", board)

        # 즐겨찾기에 들어갈 정보들
        favorite_uuid = str(uuid.uuid4())
        image_url = board['board']['image_url']
        title = board['board']['title']
        cost = board['board']['cost']
        writer_name = board['user']['name']
        now = datetime.datetime.now()
        create_at = now.strftime('%Y-%m-%d %H:%M:%S')

        doc = {
            "uuid": favorite_uuid,
            "board_uuid": board_uuid,
            "image_url": image_url,
            "title": title,
            "cost": cost,
            "writer_name": writer_name,
            "create_at": create_at,
        }

        favorite = []
        if user_info.get('favorites') is not None:
            favorite = user_info['favorites']

        favorite.append(doc)

        print("favorite :", favorite)

        db.user.update_one({'user.uuid': str(payload["uuid"])}, {'$set': {'favorites': favorite}})

        return {"result": "success", "status_code": 201}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}


# 즐겨찾기 삭제 API
def delete_favorite(par):
    token = request.cookies.get('token')

    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')

    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        # 게시글 아이디 받아옴
        board_uuid = str(par)

        # 업데이트 될 즐겨찾기 목록
        new_favorite = []

        # 전체 즐겨찾기 정보들 받아옴 -> 즐겨찾기에 해제하기 위함
        total_favorite = user_info['favorites']

        # 해제하려는 게시글을 제외하고는 새로운 리스트에 추가
        for favorite in total_favorite:
            if favorite['board_uuid'] != board_uuid:
                new_favorite.append(favorite)

        #추가한 리스트로 favorites 리스트 업데이트
        db.user.update_one({'user.uuid': str(payload["uuid"])}, {'$set': {'favorites': new_favorite}})

        return {"result": "success", "status_code": 201}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}

# 즐겨찾기 목록 불러오는 API
def show_favorite():
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')

    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        return {'data': dumps(user_info)}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}
