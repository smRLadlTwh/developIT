import datetime
import os
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


def statistics():
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d')
    today = time + ".*"
    like_search = re.compile(today, re.IGNORECASE)

    board_count = db.board.estimated_document_count({})
    user_count = db.user.estimated_document_count({})
    today_board_count = len(list(db.board.find({'board.created_at': like_search})))
    today_user_count = len(list(db.user.find({'user.created_at': like_search})))

    response = {
        'result': 'success',
        'time': time,
        'data': {
            'board_count': board_count,
            'user_count': user_count,
            'today_board_count': today_board_count,
            'today_user_count': today_user_count,
        },
        'status_code': 200
    }

    return response
