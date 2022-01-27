db = pymysql.connect(host='localhost',
                             user='yemeginadi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
yemekk= db.cursor()

yemek = yemekk.execute('INSERT INTO kullanicilar VALUES()',())
db.commit()

print(str(yemekk) + " yemek eklendi")

sonuc = yemekk.execute('UPDATE kullanicilar SET yas = %s WHERE id = %s',())
db.commit()

print(str(yemekk) + " yemek güncellendi")

sonuc = baglanti.execute('DELETE FROM kullanicilar WHERE id = %s',(1,))
db.commit()

print(str(yemekk) + " yemek silindi")
