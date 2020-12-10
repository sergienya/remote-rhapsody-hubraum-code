
import shelve
import datetime
import time
import sys
sys.path.append('../impl/')
from srg_utils import get_user_id, is_same_date

db_path = '../db.txt'

def clear_db():
    context = ""
    user_id = get_user_id(context)  # "1234" #TODO: get user_id
    print(user_id)

    with shelve.open(db_path, writeback=True) as db:
        del db[user_id]

def add_records():
    context = ""
    user_id = get_user_id(context)  # "1234" #TODO: get user_id
    print(user_id)

    user_data = {
        "date": {'month': 12, 'day': 10},
        "data": [
            {'cat': 'projekt hubraum', 'sum_time': 7380},
            {'cat': 'mein nächstes projekt', 'sum_time': 937}
        ]
    }

    with shelve.open(db_path, writeback=True) as db:
        db[user_id] = user_data

def show_records():
    with shelve.open(db_path) as db:
        for x in db:
            print(x)
            print(db[x])

#clear_db()
#add_records()
show_records()
