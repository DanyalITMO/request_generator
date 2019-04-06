import grequests
import time as tm
import random
import numpy as np
with open("filenames") as f:
    content = f.readlines()
content = [x.strip() for x in content]

urls = []
for name in content:
    if name[0] == "#":
        continue
    url = "http://127.0.0.1:80?path={}".format(name)
    urls.append(url)


pack_count = 3
pack_size = 300
multiply_urls = []
for i in range(0, pack_count * pack_size):
    multiply_urls.append(random.choice(urls))

multiply_urls_array = np.array(multiply_urls)
multiply_urls_array = multiply_urls_array.reshape(pack_count, pack_size)

multiply_urls = multiply_urls_array.tolist()

total_time = 0
for l in multiply_urls:
    rs = (grequests.get(u) for u in l)

    start_time = tm.time()
    for r in grequests.map(rs):
        print(r.status_code, r.content)
        total_time += int(r.content)

print("script executaion time in msec: ", (tm.time() - start_time) * 1000)
print("total time: ", total_time)
#нужно менять адреса для ip hash