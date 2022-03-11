import os
from sys import stdout
from time import sleep
import datetime
from flask import Flask, render_template          


# MESSAGE="lala land is great!"
MESSAGE=os.environ['MESSAGE']

app = Flask(__name__)             
@app.route('/')
def home():
    with open(outfile_path, 'a') as outfile:
        stdout.write(f"{datetime.datetime.now():%d-%m-%Y %H:%m:%S} -- {MESSAGE}\n")
        outfile.write(f"{datetime.datetime.now():%d-%m-%Y %H:%m:%S} -- {MESSAGE}\n")
        outfile.close
    with open(outfile_path, 'r') as outfile:
        text = outfile.read()
        return render_template('message.html', message=text)


outfile_path="/var/log/python.log"
# outfile_path="python.log"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')