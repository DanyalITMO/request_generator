import os

def generateRandomFile(size):
    # path = os.getcwd() + "/" + str(size)
    path = "/media/mugutdinov/2ba6d383-45de-4938-b251-ccbb54093c2c1/random/" + str(size)
    print(path)
    with open(path, 'wb') as fout:
        fout.write(os.urandom(size))

k = 1000
kb = k
mb = k * kb
gb = k * mb
for i in range(1, 10):
    generateRandomFile(i * mb)