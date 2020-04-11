import mysql.connector
import json
from datetime import datetime
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootkit",
    database="smartlab"
)


print("> genjutsu importing file...")
jsonFile = open("cleaningStep3.json", "r", encoding="utf-8-sig")
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
    print("get id propinsi....")
    berlaku = datetime.strptime(
        x['masaBerlaku'], "%d/%m/%Y").strftime("%Y-%m-%d")
    # =============================insertLab to database ready================
    # newLab = mydb.cursor()
    # sqlLab = "INSERT INTO Laboratories(accreditationNumber,name,address,provinceId, telephone,email,validUntil,is17025,labType, objectScope,createdBy , createdAt , updatedAt) values (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s)"
    # data = (x['nomorAkreditasi'], x['namaLaboratorium'], x['alamat'], idProp,
    #         x['telepon'], x['email'], berlaku, "Ya", "Pengujian", x['lingkup'], "1", datetime.now(), datetime.now())
    # newLab.execute(sqlLab,  data)
    # mydb.commit();
    #print("insert new lab done...")
    # ==================================insertbidang ============================
    for z in x['BidangPengujian']:
        getBidang = mydb.cursor()
        sql = "SELECT name FROM TestingFields WHERE name = %s "
        where = z['Bidang']
        getBidang.execute(sql, (where, ))
        resultBidang = getBidang.fetchall()
        print(len(resultBidang))
    sys.exit()
