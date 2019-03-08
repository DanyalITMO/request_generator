import urllib.request as ur
from urllib.error import *
import http.client as l7client
import sys

def getRequest(url):
    conn = ur.urlopen(url)
    try:
        data = conn.read()
    except l7client.RemoteDisconnected:
        print("can not connect")
        sys.exit()

    print(conn.status)
    if conn.status == 200:
        print(data)
        return int(data);

with open("filenames") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total_time = 0
for name in content:
    if name[0] == "#":
        continue
    url = "http://127.0.0.1:8080?path={}".format(name)
    time = getRequest(url)
    print(time)
    total_time += time

print("total execution time in msec ", total_time)

