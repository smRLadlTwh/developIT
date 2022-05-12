import datetime
import os
import re
import calendar

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
    time = now.strftime('%Y-%m')
    y = int(now.strftime('%Y'))
    m = int(now.strftime('%m'))
    day = int(now.strftime('%d')) - 4

    board = []
    user = []
    label = []

    count = 0
    i = 0
    while count < 5:
        search_day = int(day) + i
        # 달이 바뀌는 경우
        if search_day == int(calendar.monthrange(y, m)[1]) + 1:
            search_day = 1
            day = 1
            i = 0
            m = int(now.strftime('%m')) + 1
            # 년이 바뀌는 경우
            if m == 13:
                y = int(now.strftime('%Y')) + 1
                m = 1

            if m < 10:
                time = str(y) + '-0' + str(m)
            else:
                time = str(y) + '-' + str(m)

        # 1의 자리 숫자인 경우 0을 붙임 ex 8 -> 08
        if search_day < 10:
            search_day = '0' + str(search_day)
        search_time = time + '-' + str(search_day)
        print(search_time)
        today = search_time + ".*"
        like_search = re.compile(today, re.IGNORECASE)
        board_count = len(list(db.board.find({'board.created_at': like_search})))
        user_count = len(list(db.user.find({'user.created_at': like_search})))

        board.append(board_count)
        user.append(user_count)
        label.append(search_time)
        i = i + 1
        count = count + 1

    response = {
        'result': 'success',
        'time': time + '-' + str(day),
        'data': {
            'board': board,
            'user': user,
            'label': label,
        },
        'status_code': 200
    }

    return response
