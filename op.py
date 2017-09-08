#!/usr/bin/env python
# -*- coding: utf8 -*-
# print('hello,op!')
# quit()
import sys
import sqlite3


def setup_sqlite():
    print("sqlite function")
    dbname = 'op.db'
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    # executeメソッドでSQL文を実行する
    create_table = '''create table users (id int, name varchar(64),age int, gender varchar(32))'''
    c.execute(create_table)
    # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
    # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
    # タプルで渡す．
    sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    user = (1, 'Taro', 20, 'male')
    c.execute(sql, user)
    # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
    # executemanyメソッドを実行する
    insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    users = [
        (2, 'Shota', 54, 'male'),
        (3, 'Nana', 40, 'female'),
        (4, 'Tooru', 78, 'male'),
        (5, 'Saki', 31, 'female')
    ]
    c.executemany(insert_sql, users)
    conn.commit()
    select_sql = 'select * from users'
    for row in c.execute(select_sql):
        print(row)
    conn.close()


def main(cmd='default'):
    print('opcmd:%s' % (cmd))
    if cmd != "default":
        if cmd == "sqlite":
            setup_sqlite()


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 1:
        print("default")
        main()
    elif len(args) == 2:
        main(args[1])
    else:
        print("multi args no support")
        quit()




