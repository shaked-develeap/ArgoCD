import os
from sys import stdout
from time import sleep
import datetime

# MESSAGE="lala land is great!"
MESSAGE=os.environ['MESSAGE']

# def write_out(outfile_path):


i=1
outfile_path="/var/log/python.log"

print(f"starting logging to {outfile_path} file")
while True:
    with open(outfile_path, 'a') as outfile:
        stdout.write(f"{datetime.datetime.now():%Y-%m-%d %H:%m:%S} -- {MESSAGE}\n")
        outfile.write(f"{datetime.datetime.now():%Y-%m-%d %H:%m:%S} -- {MESSAGE}\n")
    i+=1
    sleep(2)
