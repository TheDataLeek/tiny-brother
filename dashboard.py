#!/usr/bin/env python

from flask import Flask, render_template
import sqlite3
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    data_stream = c.execute('''SELECT * FROM records''')

    x    = []
    down = []
    up   = []
    data = []

    for d in data_stream:
        x.append(d[0])
        down.append(d[1])
        up.append(d[2])
        data.append([format_datetime(d[0]), d[1], d[2]])

    img = test_now()

    return render_template('index.html', domain=x, down=down, up=up, data=data, img=img)


def format_datetime(raw_date):
    date = str(raw_date)
    string = '%i-%i-%i %i:%i:%i' % (int(date[0:4]), int(date[4:6]),
            int(date[6:8]), int(date[8:10]), int(date[10:12]), int(date[12:14]))
    return string

def test_now():
    process = subprocess.Popen(['speedtest-cli', '--share'], stdout=subprocess.PIPE)




if __name__ == "__main__":
    app.debug = True
    app.run()
