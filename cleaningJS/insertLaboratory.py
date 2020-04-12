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

print("> genjutsu importing file...")
jsonFile = open("pengujianOtomotif.json", "r", encoding="utf-8-sig")
testingData = json.load(jsonFile)
jsonFile.close()
i = 1
for x in testingData['OTO']:

    # =======================idlab==========================
    getIdLab = mydb.cursor()
    sql = "SELECT id FROM Laboratories WHERE accreditationNumber = %s "
    where = x['NO. AKREDITASI']
    getIdLab.execute(sql, (where, ))
    resultIdLab = getIdLab.fetchall()
    temp = ','.join(str(v) for v in resultIdLab[0])
    clear_id_lab = temp.replace("(", "")
    clear_id_lab = clear_id_lab.replace(",", "")
    clear_id_lab = clear_id_lab.replace(")", "")
    # =======================idBIdang==========================
    getIdBidang = mydb.cursor()
    sql = "SELECT id FROM TestingFields WHERE name = %s "
    where = x['BIDANG PENGUJIAN']
    getIdBidang.execute(sql, (where, ))
    resultIdBidang = getIdBidang.fetchall()
    temp = ','.join(str(v) for v in resultIdBidang[0])
    clear_id_Bidang = temp.replace("(", "")
    clear_id_Bidang = clear_id_Bidang.replace(",", "")
    clear_id_Bidang = clear_id_Bidang.replace(")", "")
    # =======================idBahanYangDIuji==========================
    getIdBahan = mydb.cursor()
    sql = "SELECT id FROM TestingMaterials WHERE name = %s "
    where = x['BAHAN ATAU PRODUK YANG DIUJI']
    getIdBahan.execute(sql, (where, ))
    resultIdBahan = getIdBahan.fetchall()
    temp = ','.join(str(v) for v in resultIdBahan[0])
    clear_id_Bahan = temp.replace("(", "")
    clear_id_Bahan = clear_id_Bahan.replace(",", "")
    clear_id_Bahan = clear_id_Bahan.replace(")", "")
    # =======================idTipePengujian==========================
    getIdjenisUji = mydb.cursor()
    sql = "SELECT id FROM TestingTypes WHERE name = %s "
    where = x['JENIS PENGUJIAN ATAU SIFAT-SIFAT YANG DIUKUR']
    getIdjenisUji.execute(sql, (where, ))
    resultIdjenisUji = getIdjenisUji.fetchall()
    temp = ','.join(str(v) for v in resultIdjenisUji[0])
    clear_id_jenisUji = temp.replace("(", "")
    clear_id_jenisUji = clear_id_jenisUji.replace(",", "")
    clear_id_jenisUji = clear_id_jenisUji.replace(")", "")
    # =======================idMetodePengujian==========================
    getIdMetodeUji = mydb.cursor()
    sql = "SELECT id FROM TestingMethods WHERE name = %s "
    where = x['METODE PENGUJIAN, TEKNIK YANG DIGUNAKAN']
    getIdMetodeUji.execute(sql, (where, ))
    resultIdMetodeUji = getIdMetodeUji.fetchall()
    temp = ','.join(str(v) for v in resultIdMetodeUji[0])
    clear_id_MetodeUji = temp.replace("(", "")
    clear_id_MetodeUji = clear_id_MetodeUji.replace(",", "")
    clear_id_MetodeUji = clear_id_MetodeUji.replace(")", "")
    print(clear_id_Bidang, clear_id_Bahan, clear_id_jenisUji,
          clear_id_MetodeUji, clear_id_lab)
    # ===================inser into db data pengukuran===================
    insert_to_db = mydb.cursor()
    sql = "INSERT INTO TestingLaboratories  (testingFieldId,testingMaterialId,testingTypeId,testingMethod,labId,createdAt,updatedAt) values(%s , %s , %s, %s, %s, %s, %s)"
    where = clear_id_Bidang, clear_id_Bahan, clear_id_jenisUji, clear_id_MetodeUji, clear_id_lab, datetime.now(), datetime.now()
    insert_to_db.execute(sql, where)
    mydb.commit()

    print("data ke ", i)
