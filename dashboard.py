#!/usr/bin/env python

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    data = c.execute('''SELECT * FROM records''')

    x = []
    down = []
    up = []

    for d in data:
        x.append(d[0])
        down.append(d[1])
        up.append(d[2])

    return render_template('index.html', domain=x, down=down, up=up)


if __name__ == "__main__":
    app.debug = True
    app.run()
