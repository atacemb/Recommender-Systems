import os
from collections import Counter


def usernames():
    f1 = open("kullanicilar.txt", "w", encoding="utf-8")
    os.chdir('D:\data')
    DIR = os.listdir()
    print(DIR)
    for files in DIR:
        f = files
        keyfile = open(f, 'r', encoding="utf-8")
        for line in keyfile:
            if line.__contains__('<Author>'):
                user = line.replace('<Author>', '')
                print(user)
                f1.write(user)


def user_noise_remover():
    t = 0
    f = open('kullanicilar.txt', 'r', encoding="utf-8")
    f1 = open('updated.txt', 'w', encoding="utf-8")
    names1 = f.readlines()
    names1 = [x.replace('\n', '') for x in names1]

    ar1 = 'A TripAdvisor Member'
    ar2 = 'lass='
    while names1.__contains__(ar1):
        names1.remove(ar1)

    while names1.__contains__(ar2):
        names1.remove(ar2)

    for item in names1:
        f1.write("%s\n" % item)
    print(names1)


def user_counter():
    f = open('updated.txt', 'r', encoding="utf-8")
    f1 = open('counted.txt', 'w', encoding="utf-8")
    f2 = open('countedusername.txt', 'w', encoding="utf-8")
    users = f.readlines()
    users = [x.replace('\n', '') for x in users]
    user_set = set(users)
    nouv = len(user_set)
    print(users.__sizeof__())
    print(nouv)
    a = Counter(users)
    for k, v in a.most_common(
            961):  # most_common en çok bulunanları döndürüyor normalde ama parametresi olmadığından herşeyi dönüdürüyor şu anda
        if k.__contains__('.') or k.__contains__('<') or k.__contains__('/'):
            print(k)
        else:
            f1.write("{} {}\n".format(k, v))
            f2.write("{}\n".format(k))


def user_filing():
    os.chdir('D:\data')
    DIR = os.listdir()
    file = open('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\countedusername.txt', 'r', encoding="utf-8")
    users = file.readlines()
    users = [x.replace('\n', '') for x in users]
    for user in users:
        print(user)
        auser = "<Author>" + user
        filename = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user
        bfile = open(filename, 'w', encoding="utf-8")
        for f in DIR:
            keyfile = open(f, 'r', encoding="utf-8")
            for line in keyfile:

                if line.startswith(auser):
                    bfile.write(f + "\n")
                    bfile.write(line)
                    for x in range(12):
                        bline = next(keyfile)
                        bfile.write(bline)


def data_dup():
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    iter = 0
    for user in DIR:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user
        f = open(fname, 'r+', encoding="utf-8")
        d = f.readlines()
        d = [x.replace('\n', '') for x in d]
        f.seek(0)
        for i in d:
            if i == "<Author>%s" % user:
                iteri = iter
                hotel = "%s\n" % d[iteri - 1]
                f.write(hotel)
                for x in range(13):
                    if iteri < len(d):
                        ibe = d[iteri]
                        ibe = "%s\n" % ibe
                        f.write(ibe)
                        iteri += 1
            iter += 1
        iter = 0
        f.truncate()


def weighted_data():
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    for user in DIR:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata\\%s.txt' % user
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith('<Overall>'):
                    overall = line.replace('<Overall>', '')
                    overall = int(overall)
                if line.startswith(tag):
                    sayi = line.replace(tag, '')
                    sayi = int(sayi)
                    if sayi == -1:
                        value = value - 5
                    else:
                        sayi = overall - sayi
                        if abs(sayi) == 0:
                            value = value + 10
                        elif abs(sayi) == 1:
                            value = value + 7
                        elif abs(sayi) == 2:
                            value = value + 5
                        elif abs(sayi) == 3:
                            value = value + 3
                        elif abs(sayi) == 4:
                            value = value + 1
            f.write(tag)
            f.write(str(value))
            f.write('\n')
            value = 0


def normalization():
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    norm = []

    for user in DIR:
        print(user)
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata\\%s.txt' % user
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata\\%s.txt' % user
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    norm.append(ntag)
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    if max(norm) == min(norm):
                        ntag = 0
                    else:
                        ntag = (ntag - min(norm)) / (max(norm) - min(norm))

                    f.write(tag)
                    f.write(str(ntag))
                    f.write('\n')
        value = 0
        norm = []


def hotel_weighted():
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data')
    DIR = os.listdir()
    DIR = [x.replace('.dat', '') for x in DIR]
    for hotel in DIR:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data\\%s.dat' % hotel
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hdata\\%s.dat' % hotel
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith('<Overall>'):
                    overall = line.replace('<Overall>', '')
                    overall = int(overall)
                if line.startswith(tag):
                    sayi = line.replace(tag, '')
                    sayi = int(sayi)
                    if sayi == -1:
                        value = value - 5
                    else:
                        sayi = overall - sayi
                        if abs(sayi) == 0:
                            value = value + 10
                        elif abs(sayi) == 1:
                            value = value + 7
                        elif abs(sayi) == 2:
                            value = value + 5
                        elif abs(sayi) == 3:
                            value = value + 3
                        elif abs(sayi) == 4:
                            value = value + 1
            f.write(tag)
            f.write(str(value))
            f.write('\n')
            value = 0

def hotel_normalization():
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data')
    DIR = os.listdir()
    DIR = [x.replace('.dat', '') for x in DIR]
    norm = []

    for hotel in DIR:
        print(hotel)
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hdata\\%s.dat' % hotel
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hcdata\\%s.dat' % hotel
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    norm.append(ntag)
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    if max(norm) == min(norm):
                        ntag = 0
                    else:
                        ntag = (ntag - min(norm)) / (max(norm) - min(norm))

                    f.write(tag)
                    f.write(str(ntag))
                    f.write('\n')
        value = 0
        norm = []


def recommend_by_user():

    

hotel_normalization()