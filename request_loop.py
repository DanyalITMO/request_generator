import grequests
import time as tm

with open("filenames") as f:
    content = f.readlines()
content = [x.strip() for x in content]

urls = []
for name in content:
    if name[0] == "#":
        continue
    url = "http://127.0.0.1:8080?path={}".format(name)
    urls.append(url)

rs = (grequests.get(u) for u in urls)

total_time = 0

start_time = tm.time()
for r in grequests.map(rs):
    print(r.status_code, r.content)
    total_time += int(r.content)

print("script executaion time in msec: ", (tm.time() - start_time) * 1000)
print("total time: ", total_time)