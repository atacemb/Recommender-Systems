import os
from collections import Counter


def usernames():  # kullanıcı listesi
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


def user_noise_remover():  # unique kullanıcı listesi
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


def user_counter():  # kullanıcı adı kullanılabilir olan kullanıcılar ve 5'den fazla yorum yapan kullanıcıları toplayan fonksiyon
    f = open('updated.txt', 'r', encoding="utf-8")  # kullanıcı adı geçerli olan kullanıcıların bulunduğu dosya
    f1 = open('counted.txt', 'w', encoding="utf-8")  # kullanıcıların kaç yorum yaptıklarıyla beraber yoplanacağı dosya
    f2 = open('countedusername.txt', 'w',
              encoding="utf-8")  # kullanıcıların yaptıkları yorum sayısına göre kullanıcı adların sıralanacağı dosya
    users = f.readlines()
    users = [x.replace('\n', '') for x in users]
    user_set = set(users)
    nouv = len(user_set)
    print(users.__sizeof__())
    print(nouv)
    a = Counter(users)
    for k, v in a.most_common(961):  # 5'den fazla yorum yapan kişiler döndürülür
        if k.__contains__('.') or k.__contains__('<') or k.__contains__(
                '/'):  # kullanıcı adlarında kullanılmaması gereken öğeleri içeren kullanıcılar elenir
            print(k)
        else:
            f1.write("{} {}\n".format(k, v))  # kullanıcı adı ve yaptığı yorum sayısını içeren format
            f2.write("{}\n".format(k))  # sadece kullanıcı adını içeren format


def user_filing():  # kullanıcıları yaptıkları yorumlarla beraber bir klasörde toplayan fonksiyon
    os.chdir('D:\data')
    DIR = os.listdir()
    file = open('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\countedusername.txt', 'r',
                encoding="utf-8")  # kullanılacak kullanıcı adlarını içeren dosya
    users = file.readlines()
    users = [x.replace('\n', '') for x in users]
    for user in users:
        print(user)
        auser = "<Author>" + user
        filename = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user  # kullanıcı klasörü lokasyonu
        bfile = open(filename, 'w', encoding="utf-8")
        for f in DIR:
            keyfile = open(f, 'r', encoding="utf-8")
            for line in keyfile:

                if line.startswith(auser):  # kullanıcı ismini bulduğunda if sorgusuna giriyoruz
                    bfile.write(f + "\n")  # otel ismi alınır
                    bfile.write(line)  # kullanıcı ismi alınır
                    for x in range(12):  # kullanıcının yaptığı geri kalan değerlendirmeler alınır (value, overall gibi)
                        bline = next(keyfile)
                        bfile.write(bline)  # oluşturulan kullanıcı klasörüne satırlarına değerlendirmeler eklenir


def data_dup():  # kullanıcı yorunlarını düzenleme ve duplicationları temizleme
    os.chdir(
        'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata')  # kullanıcı değerlendirmelerinin bulunduğu dosya
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


def weighted_data():  # kullanıcı değerlendirmelerini normalizasyona hazırlayan ağırlıklandırma fonksiyonu
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']  # ağırlıklandırılmasını istediğimiz özellikleri içeren liste
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    for user in DIR:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user  # ağırlıklandırılacak kullanıcı, kullanıcı klasöründen alınır
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata\\%s.txt' % user  # ağırlıklandırılmış kullanıcı, ağırlıklandırılmış klasöre koyulur
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith('<Overall>'):  # Overall'a gelindiğinde yeni bir değerlendirme sayılır
                    overall = line.replace('<Overall>', '')
                    overall = int(overall)  # Overall değeri saklanır
                if line.startswith(tag):
                    sayi = line.replace(tag, '')
                    sayi = int(sayi)
                    if sayi == -1:  # kullanıcı bir özelliği değerlendirmediğinde ağırlıklı puanından 5 düşülür
                        value = value - 5
                    else:
                        sayi = overall - sayi
                        if abs(
                                sayi) == 0:  # eğer özelliğin değeri overall değeri ile aynı ise ağırlıklı değere 10 eklenir
                            value = value + 10
                        elif abs(
                                sayi) == 1:  # eğer özelliğin değeri overall değeri arasındaki fark 1 ise ağırlıklı değere 7 eklenir
                            value = value + 7
                        elif abs(
                                sayi) == 2:  # eğer özelliğin değeri overall değeri arasındaki fark 2 ise ağırlıklı değere 5 eklenir
                            value = value + 5
                        elif abs(
                                sayi) == 3:  # eğer özelliğin değeri overall değeri arasındaki fark 3 ise ağırlıklı değere 3 eklenir
                            value = value + 3
                        elif abs(
                                sayi) == 4:  # eğer özelliğin değeri overall değeri arasındaki fark 4 ise ağırlıklı değere 1 eklenir
                            value = value + 1
            f.write(tag)
            f.write(str(value))
            f.write('\n')
            value = 0


def normalization():  # kullanıcının ağırlıklandırılmış verilerine min-max normalizasyonu yapan fonksiyon
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']  # ağırlıklandırılmasını istediğimiz özellikleri içeren liste
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    norm = []

    for user in DIR:
        print(user)
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\wdata\\%s.txt' % user  # ağırlıklı değerleri içeren klasör
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata\\%s.txt' % user  # normalize edilmiş değerleri içeren klasör
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith(tag):  # normalize edilecek tag bulunuyor
                    ntag = line.replace(tag, '')  # tag ismi kaldırılıyor
                    ntag = int(ntag)  # değer integer'a çevriliyor
                    norm.append(ntag)  # norm isimli listeye ekleniyor
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    if max(norm) == min(norm):
                        ntag = 0
                    else:
                        ntag = (ntag - min(norm)) / (max(norm) - min(norm))  # min-max normalizasyonu denklemi (değer-minimum)/(maximum-minimum)

                    f.write(tag)
                    f.write(str(ntag))
                    f.write('\n')  # normalize edilmiş data dosyaya eklenir
        value = 0
        norm = []


def hotel_weighted():  # otellere yapılmış yorumları normalizasyona hazırlayan ağırlıklandırma fonksiyonu
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']  # ağırlıklandırılmasını istediğimiz özellikleri içeren liste
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data')
    DIR = os.listdir()
    DIR = [x.replace('.dat', '') for x in DIR]
    for hotel in DIR:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data\\%s.dat' % hotel  # otel klasörü
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hdata\\%s.dat' % hotel  # ağırlıklı otel değerlerini içerecek klasör
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith('<Overall>'):  # Overall'a gelindiğinde yeni bir değerlendirme sayılır
                    overall = line.replace('<Overall>', '')
                    overall = int(overall)  # Overall değeri saklanıyor
                if line.startswith(tag):
                    sayi = line.replace(tag, '')
                    sayi = int(sayi)
                    if sayi == -1:
                        value = value - 5  # otelin bir özelliği değerlendirilmediğinde ağırlıklı puanından 5 düşülür
                    else:
                        sayi = overall - sayi
                        if abs(sayi) == 0:
                            value = value + 10  # eğer özelliğin değeri overall değeri ile aynı ise ağırlıklı değere 10 eklenir
                        elif abs(sayi) == 1:
                            value = value + 7  # eğer özelliğin değeri overall değeri arasındaki fark 1 ise ağırlıklı değere 7 eklenir
                        elif abs(sayi) == 2:
                            value = value + 5  # eğer özelliğin değeri overall değeri arasındaki fark 2 ise ağırlıklı değere 5 eklenir
                        elif abs(sayi) == 3:
                            value = value + 3  # eğer özelliğin değeri overall değeri arasındaki fark 3 ise ağırlıklı değere 3 eklenir
                        elif abs(sayi) == 4:
                            value = value + 1  # eğer özelliğin değeri overall değeri arasındaki fark 4 ise ağırlıklı değere 1 eklenir
            f.write(tag)
            f.write(str(value))
            f.write('\n')
            value = 0


def hotel_normalization():  # otel min-max normalizasyonu
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']  # normalize etmek istediğimiz özellikleri içeren liste
    value = 0
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\data')
    DIR = os.listdir()
    DIR = [x.replace('.dat', '') for x in DIR]
    norm = []

    for hotel in DIR:
        print(hotel)
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hdata\\%s.dat' % hotel  # ağırlıklı değerleri içeren klasör
        f = open(fname, 'r+', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hcdata\\%s.dat' % hotel  # normalize edilmiş değerleri içeren klasör
        f = open(fname, 'w+', encoding="utf-8")
        for tag in tags:
            for line in lines:
                if line.startswith(tag):  # normalize edilecek tag bulunur
                    ntag = line.replace(tag, '')  # tag ismi kaldırılır
                    ntag = int(ntag)  # değer integer'a çevrilir
                    norm.append(ntag)  # norm isimli listeye eklenir
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = int(ntag)
                    if max(norm) == min(norm):
                        ntag = 0
                    else:
                        ntag = (ntag - min(norm)) / (max(norm) - min(norm))  # min-max normalizasyonu denklemi (değer-minimum)/(maximum-minimum)

                    f.write(tag)
                    f.write(str(ntag))
                    f.write('\n')  # normalize edilmiş data dosyaya eklenir
        value = 0
        norm = []


def user_matris(user):  # user normalizasyon matrisi hazırlama
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']

    norm = []
    fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata\\%s.txt' % user
    f = open(fname, 'r+', encoding="utf-8")
    lines = f.readlines()
    lines = [x.replace('\n', '') for x in lines]
    for tag in tags:
        for line in lines:
            if line.startswith(tag):
                ntag = line.replace(tag, '')
                ntag = float(ntag)
                norm.append(ntag)
    return norm


def compare_user(matris, user):  # halihazırda olan kullanıcıyı diğer kullanıcılarla karşılaştıran fonksiyon
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>'] # karşılaştırılmasını istediğimiz özellikleri içeren liste
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata')  # normalize edilmiş değerleri içeren klasör
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    DIR.remove(user)
    fav = [i for i, value in enumerate(matris) if value == 1.0]  # normalize edilmiş değeri 1.0 olan özellikler favori özellikler olarak alınır

    u_list = []
    for user in DIR:
        toplam = 0.0
        norm = []
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata\\%s.txt' % user  # normalize edilmiş kullanıcı verisini içeren klasör
        f = open(fname, 'r', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        for tag in tags:
            for line in lines:
                if line.startswith(tag):   # tüm bu if sorgusunun içinde kullanıcı değelendirmeleri bir listede toplanır
                    ntag = line.replace(tag, '')
                    ntag = float(ntag)
                    norm.append(ntag)

        for i in fav:
            if norm[i] == 1.0:  # gelen kullanıcının favori değerinin karşılaştırdığımız kullanıcının favori değeriyle eşleşip eşleşmediğine bakılır
                for x in range(7):
                    temp = norm[x] - matris[x]  # eşleşme olduğunda diğer normalize edilmiş özelliklerin uzaklıkları bulunur
                    toplam = abs(temp) + toplam  # bulunan uzaklık uzaklıklar toplamına eklenir
                u_list.append('{},{}'.format(toplam, user))  # bulunan uzaklık toplamı kullanıcı adıyla birlikte geri döndürülür
                break
            else:
                pass
    return u_list


def compare_user0(matris):  # yeni user oluşturulduğunda userların karşılaştırılması
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata')
    DIR = os.listdir()
    DIR = [x.replace('.txt', '') for x in DIR]
    fav = [i for i, value in enumerate(matris) if value == 1.0]

    u_list = []
    for user in DIR:
        toplam = 0.0
        norm = []
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\cdata\\%s.txt' % user
        f = open(fname, 'r', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    ntag = line.replace(tag, '')
                    ntag = float(ntag)
                    norm.append(ntag)

        for i in fav:
            if norm[i] == 1.0:
                for x in range(7):
                    temp = norm[x] - matris[x]
                    toplam = abs(temp) + toplam
                u_list.append('{},{}'.format(toplam, user))
                break
            else:
                pass
    return u_list


def compare_hotel(matris):  # verilen otel ile kullanıcıyı karşılaştıran fonksiyon
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']  # karşılaştırılmasını istediğimiz özellikleri içeren liste
    os.chdir('C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hcdata')  # normalize edilmiş otel verisini içeren klasör
    DIR = os.listdir()
    DIR = [x.replace('.dat', '') for x in DIR]
    fav = [i for i, value in enumerate(matris) if value == 1.0]  # normalize edilmiş değeri 1.0 olan özellikleri en iyi özellikler olarak alınır

    h_list = []
    for hotel in DIR:
        toplam = 0.0
        norm = []
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\hcdata\\%s.dat' % hotel  # normalize edilmiş otel verisini içeren klasör
        f = open(fname, 'r', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        for tag in tags:
            for line in lines:
                if line.startswith(tag):   # tüm bu if sorgusunun içinde otel değelendirmeleri bir listede toplanır
                    ntag = line.replace(tag, '')
                    ntag = float(ntag)
                    norm.append(ntag)

        for i in fav:
            if norm[i] == 1.0:  # gelen kullanıcının favori değerinin karşılaştırdığımız otelin en iyi değeriyle eşleşip eşleşmediğine bakılır
                for x in range(7):
                    temp = norm[x] - matris[x]  # eşleşme olduğunda diğer normalize edilmiş özelliklerin uzaklıkları bulunur
                    toplam = abs(temp) + toplam  # bulunan uzaklık uzaklıklar toplamına eklenir
                h_list.append('{},{}'.format(toplam, hotel))  # bulunan uzaklık toplamı otel adıyla birlikte geri döndürülür
                break
            else:
                pass
    return h_list


def get_result(matris):  # yakınlık matrisi gönderildiğinde kullanıcı nicki veya hotel ismi alma
    user = []
    temp = ['']
    for i in range(3):
        temp = matris[i].split(",")
        user.append(temp[1])
    return user


def get_recommendation(users, fav):  # belirlenen kullanıcıların değerlendirmelerine bakılarak otel önerme işleminin gerçekleşmesi
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>', '<Overall>']  # önerilecek oteller için bakılacak özellikler listesi
    ntag = ''
    data = []
    x = 0
    indice = 0
    top = []
    hotels = []
    son = []
    for user in users:
        fname = 'C:\\Users\\Atacem\\PycharmProjects\\pythonProject\\userdata\\%s.txt' % user  # kullanıcı değerlendirmelerinin bulunduğu klasör
        f = open(fname, 'r', encoding="utf-8")
        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        for tag in tags:
            for line in lines:
                if line.startswith(tag):
                    if ntag == '':
                        temp = line.replace(tag, '')
                        ntag = temp

                    else:
                        temp = line.replace(tag, '')
                        ntag = '{},{}'.format(ntag, temp)
            data.append(ntag)  # buraya kadar olan bölümde kullanıcının tüm değerlendirmeleri bir listede toplanır, formatlaması <etiket,değer> şeklindedir
            ntag = ''
        for line in lines:
            if line.startswith('hotel'):
                hotels.append(line)  # kullanıcının yorum yaptığı oteller bir listede toplanır
    print(data)
    print(data.__len__())
    for d in data:
        tempdata = d.split(',')  # kullanıcı değerlendirmeleri işlemler için hazır hale getirilir, her bir döngüde bir değerlendirme üzerinde işlem yapılır
        for i in range(tempdata.__len__()):
            temp = tempdata[i]
            ind = indice + i

            if x % 8 == 0: # 8 tane özellik içerisinde hangi özellikte olduğumuzu belirleyen if sorgusu

                if fav.__contains__(x % 8):
                    toplam = (int(temp) * 5)  # kullanıcının favori özelliğinde isek bu özellik 5 ile çarpılarak ağırlıklandırılır

                elif x % 8 == 7:
                    toplam = (int(temp) * 5)  # overall özelliğinde isek bu özellik de favori özellik gibi 5 ile çarpılarak ağırlıklandırılır

                else:
                    toplam = int(temp)  # diğer özellikler direk ağırlıklandırmaya katılır

            else:
                if fav.__contains__(x % 8):
                    toplam = top[ind] + (int(temp) * 5)  # kullanıcının favori özelliğinde isek bu özellik 5 ile çarpılarak ağırlıklandırılır

                elif x % 8 == 7:
                    toplam = top[ind] + (int(temp) * 5)  # overall özelliğinde isek bu özellik de favori özellik gibi 5 ile çarpılarak ağırlıklandırılır

                else:
                    toplam = top[ind] + int(temp)  # diğer özellikler direk ağırlıklandırmaya katılır

            if x % 8 == 0:
                top.append(toplam)  # değerlendirmelerin toplamlarının tutulduğu listeye eklenir

            else:
                top[ind] = toplam  # değerlendirmelerin toplamlarının tutulduğu listeye eklenir

        x = x + 1
        if x % 8 == 0:
            indice = indice + len(tempdata)
    print(len(top))
    print(hotels)
    print(len(hotels))
    for i in range(hotels.__len__()):
        temp = '{},{}'.format(int(top[i]), hotels[i])  # oteller ve ağırlıklı toplamları bir liste biçiminde döndürülür, format <toplam,otel> şeklindedir
        son.append(temp)
    return son


def comparer(rec):  # dizilim için yapılmış utility fonksiyonu
    compare = []
    for r in rec:
        temp = r.split(',')
        compare.append(int(temp[0]))
    return compare


print('Kullanıcı oluşturmak için 0 halihazırda olan kullanıcı ile devam etmek için 1 yazınız')
x = int(input())

if x == 1:
    print('Kullanıcı adı: ')
    u = input()
    rechotels = []
    dup = []
    fav = [i for i, value in enumerate(user_matris(u)) if value == 1.0]  # favori kriterlerin alınması
    users = sorted(compare_user(user_matris(u), u))[:3]  # en yakın 3 user
    hotels = sorted(compare_hotel(user_matris(u)))[:3]  # en yakın 3 user
    print(users)
    print(hotels)
    print(get_result(users))
    print(get_result(hotels))
    rec = get_recommendation(get_result(users), fav)
    print(rec)
    recommender = sorted(comparer(rec), reverse=True)[:3]
    print(recommender)
    for i in range(3):
        for r in rec:
            if r.startswith(str(recommender[i])) and not dup.__contains__(r) and len(rechotels) < 3:
                dup.append(r)
                temp = r.split(',')
                rechotels.append(temp[1])

    print(rechotels + get_result(hotels))
if x == 0:
    ar = []
    tags = ['<Value>', '<Rooms>', '<Location>', '<Cleanliness>', '<Check in / front desk>', '<Service>',
            '<Business service>']
    for i in range(7):
        print(tags[i] + ' degerini giriniz (0-1 arası float eğerler girilmelidir)')
        a = float(input())
        if a > 1.0 or a < 0.0:
            print('yanlış değer girildi')
            exit()
        else:
            ar.append(a)

    rechotels = []
    dup = []
    fav = [i for i, value in enumerate(ar) if value == 1.0]
    users = sorted(compare_user0(ar))[:3]
    hotels = sorted(compare_hotel(ar))[:3]
    print(users)
    print(hotels)
    print(get_result(users))
    print(get_result(hotels))
    rec = get_recommendation(get_result(users), fav)
    print(rec)
    recommender = sorted(comparer(rec), reverse=True)[:3]
    print(recommender)
    for i in range(3):
        for r in rec:
            if r.startswith(str(recommender[i])) and not dup.__contains__(r) and len(rechotels) < 3:
                dup.append(r)
                temp = r.split(',')
                rechotels.append(temp[1])

    print(rechotels + get_result(hotels))
