#!/usr/bin/env python

import sys
import sqlite3
import random
from datetime import datetime as dt
from datetime import timedelta as td


# How many days of data to simulate
DAYS = 10

# How many records are generated each day
RECORDS = 5


def main():
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS records(
            datetime INTEGER,
            down FLOAT
            up FLOAT,
    """)

    conn.commit()

    today = dt.today()

    stepsize = 24 / RECORDS

    for i in range(DAYS):
        date = today - td(days=1)
        for i in range(RECORDS):
            date.hour = 0 + i * stepsize
            date.minute = (stepsize - int(stepsize)) * 60
            date.second = 0
            print(date)
            #c.execute('''INSERT INTO records VALUES(?, ?, ?)''')


if __name__ == '__main__':
    sys.exit(main())
