#!/usr/bin/env python3

import sqlite3
import pandas as pd

def count(file, user_id):
    sql_con = sqlite3.connect(file)
    try:
        sum_minutes = pd.read_sql(
                'SELECT sum(minutes) FROM data WHERE user_id == {}'.format(user_id),
                 sql_con).values
        sum_minutes = int(sum_minutes)
    except TypeError:
        return 0
    sql_con.close()
    return sum_minutes

if __name__ == '__main__':
    print(count('users_data.sqlite', 849000000))
