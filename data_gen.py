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
            down REAL,
            up REAL)
    """)

    conn.commit()

    today = dt.today()

    stepsize = 24 / RECORDS

    data = []
    for i in range(DAYS):
        offset = today - td(days=i)
        for j in range(RECORDS):
            day = int('%04i%02i%02i%02i%02i%02i' % (offset.year, offset.month, offset.day,
                int(0 + j * stepsize), (stepsize - int(stepsize)) * 60, 00))
            if i == 0 and j == 0:
                down = random.randint(10, 100)
                up = random.randint(1, 20)
            else:
                down = data[-1][1] + random.randint(-1, 1)
                up = data[-1][2] + random.randint(-1, 1)

                if down < 10:
                    down = 10
                if up < 0:
                    up = 0

            data.append((day, down, up))

    c.executemany('''
        INSERT INTO records
        VALUES (?, ?, ?)
    ''', data)

    conn.commit()


if __name__ == '__main__':
    sys.exit(main())
