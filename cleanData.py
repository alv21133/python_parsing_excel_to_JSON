import json
from json import JSONEncoder
import numpy as np
import ast

print("> genjutsu importing file...")
jsonFile = open("pengujianFinal.json", "r", encoding="utf-8-sig")
testingData = json.load(jsonFile)
jsonFile.close()
print("> genjutsu making JSON...")


class address:
    def __init__(self,  address):
        self.Alamat = address


class noAkre:
    def __init__(self,  no):
        self.Akreditasi = no


class merge:
    def __init__(self,  no, alamat, name, telp, berlaku, lingkup, email, propinsi, negara, bidangUji):
        self.akreditasi = no
        self.masa_berlaku_akreditasi = berlaku
        self.nama_Lab = name
        self.alamat = alamat
        self.telepon = telp
        self.propinsi = propinsi
        self.negara = negara
        self.email = email
        self.lingkup = lingkup
        self.bidangUji = bidangUji


class makeBidang:
    def __init__(self, bidang):
        self.namaBidang = bidang


class MainData:
    def __init__(self, nama,  bidang):
        self.Perusahaan = nama
        self.bidang = bidang


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def custom_replace(kk):
    kk.replace("\\", "")
    return kk


#print(json.dumps(testingData, indent=8, ensure_ascii=False))
# alamat
tempheadList = []
headList = []
mainList = []
bidangPengujian = []
i = 1
ii = 1
key = "default"
keyBidang = "mekanik"
for kk in testingData["OTO"]:
    temp = kk["ALAMAT "]
    noAkreditasi = kk["NO. AKREDITASI"]
    name = kk["NAMA LABORATORIUM"]
    telp = kk["TELEPON"]
    berlaku = kk["MASA BERLAKU AKREDITASI"]
    lingkup = kk["LINGKUP"]
    email = kk["EMAIL"]
    propinsi = kk["PROPINSI"]
    negara = kk["NEGARA"]
    bidangObjek = kk["BIDANG PENGUJIAN"]

    if temp != key:
        print("Perusahaan: ", ii, name)
        print("jumlah bidang =", len(bidangPengujian))

        headList.append(merge(noAkreditasi, temp, name, telp, berlaku,
                              lingkup, email, propinsi, negara, bidangPengujian))

        ii += 1
        bidangPengujian.clear()

    if keyBidang != bidangObjek:
        bidangPengujian.append(makeBidang(bidangObjek))
        keyBidang = bidangObjek
        print("dalam List", i)
        i += 1
    key = temp
    # primary data ok
    # if key != temp:
    #     tempheadList.append(
    #         merge(noAkreditasi, temp, name, telp, berlaku, lingkup, email, propinsi, negara, bidangPengujian))
    #     i += 1
    #     key = temp
# remove duplicate


filterData = list(set(headList))

# namabah induk json
# koko = {}
# koko["jajal"] = filterData

# make array on object
# mainList.append(MainData(tempheadList))
# map(lambda x: replace(x), mainList)
# make serialible json
makeJSON = MyEncoder().encode(filterData)
# print(type(makeJSON))
# write file json
# afterModify = json.dumps(testingData["OTO"][0])
newFile = open("tryClean.json", "w", encoding="utf-8-sig")
print(">> genjutsu  making file .....")
makeJSON = ast.literal_eval(makeJSON)
json.dump(makeJSON, newFile, indent=4,  ensure_ascii=False)
# newFile.write(makeJSON)
newFile.close()
print(">>> done..")
# kurang memuat json format dari array
