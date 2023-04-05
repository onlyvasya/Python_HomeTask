def ritm(condition, object):
    return len(set(map(condition, object)))==1
stih = 'пара-ра-рам рам-па-папам па-ра-па-да'
stih_split = stih.split()
if ritm(lambda x: sum(1 for i in x if i in 'уеыаоэяиюё'),stih_split):
    print("Парам пам-пам")
else:
    print("Пам парам")    