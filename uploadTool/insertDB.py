import mysql.connector
import json
from datetime import datetime
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootkit",
    database="smartlab2"
)
i = 1
print("> genjutsu importing file...")
jsonFile = open("cleaningStep4.json", "r", encoding="utf-8-sig")
testingData = json.load(jsonFile)
jsonFile.close()
for x in testingData:
    # get id for propinsi
    IdPropinsi = mydb.cursor()
    sql = "SELECT id FROM Provinces WHERE name LIKE %s "
    where = x['propinsi'].upper(),
    IdPropinsi.execute(sql, where)
    resultPropinsi = IdPropinsi.fetchall()
    hasil = ','.join(str(v) for v in resultPropinsi)
    idProp = hasil.replace('(', "")
    idProp = idProp.replace(')', "")
    idProp = idProp.replace(',', "")
    print("get id propinsi....", x['propinsi'])
    berlaku = datetime.strptime(
        x['masaBerlaku'], "%d/%m/%Y").strftime("%Y-%m-%d")
    # =============================insertLab to database ready================
    newLab = mydb.cursor()
    sqlLab = "INSERT INTO Laboratories(accreditationNumber,name,address,provinceId, telephone,email,validUntil,is17025,labType, objectScope,createdBy , createdAt , updatedAt) values (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s)"
    data = (x['nomorAkreditasi'], x['namaLaboratorium'], x['alamat'], idProp,
            x['telepon'], x['email'], berlaku, "Ya", "Pengujian", x['lingkup'], "1", datetime.now(), datetime.now())
    newLab.execute(sqlLab,  data)
    mydb.commit()
    print(i, "================================insert new lab done...============================")
    i += 1
    # ==================================insertbidang ============================
    for z in x['BidangPengujian']:
        getBidang = mydb.cursor()
        sql = "SELECT name FROM TestingFields WHERE name = %s "
        where = z['Bidang']
        getBidang.execute(sql, (where, ))
        resultBidang = getBidang.fetchall()
        if len(resultBidang) < 1:
            getBidang = mydb.cursor()
            sql = "INSERT INTO TestingFields (name,createdAt, updatedAt) values(%s , %s , %s)"
            where = z['Bidang'], datetime.now(), datetime.now()
            getBidang.execute(sql, where)
            mydb.commit()
        # ==================================insertBahanYangDiUji============================
        bahanUji = mydb.cursor()
        sql = "SELECT name FROM TestingMaterials WHERE name = %s "
        where = z['bahanYangdiUji']
        bahanUji.execute(sql, (where, ))
        resultBahan = bahanUji.fetchall()
        if len(resultBahan) < 1:
            bahanUji = mydb.cursor()
            sql = "INSERT INTO TestingMaterials  (name,createdAt, updatedAt) values(%s , %s , %s)"
            where = z['bahanYangdiUji'], datetime.now(), datetime.now()
            bahanUji.execute(sql, where)
            mydb.commit()

        print("Looping...........")
        for cc in z['MetodePengujian']:
            # # # ==================================insertJenis pengujian ============================
            jenisUji = mydb.cursor()
            sql = "SELECT name FROM TestingTypes WHERE name = %s "
            where = cc['jenisPengujian']
            jenisUji.execute(sql, (where, ))
            resultJenisUji = jenisUji.fetchall()
            if len(resultJenisUji) < 1:
                jenisUji = mydb.cursor()
                sql = "INSERT INTO TestingTypes  (name,createdAt, updatedAt) values(%s , %s , %s)"
                where = cc['jenisPengujian'], datetime.now(
                ), datetime.now()
                jenisUji.execute(sql, where)
                mydb.commit()
                print("jenisPengujian  =>  Commited .....")
            # # ==================================Metode pengujian ============================
            metodePengujian = mydb.cursor()
            sql = "SELECT name FROM TestingMethods WHERE name = %s "
            where = cc['MetodePengujian']
            metodePengujian.execute(sql, (where, ))
            resultMetodePenguijan = metodePengujian.fetchall()
            if len(resultMetodePenguijan) < 1:
                metodePengujian = mydb.cursor()
                sql = "INSERT INTO TestingMethods  (name,createdAt, updatedAt) values(%s , %s , %s)"
                where = cc['MetodePengujian'], datetime.now(
                ), datetime.now()
                metodePengujian.execute(sql, where)
                mydb.commit()
                print(cc['MetodePengujian'], "=> comitted....")


print("Good joob... all JOb finished sasori.inc")
