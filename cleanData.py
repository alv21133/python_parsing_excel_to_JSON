import json
from json import JSONEncoder
import numpy as np
import ast

print("> genjutsu importing file...")
jsonFile = open("Testing_rev1.json", "r", encoding="utf-8-sig")
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
    def __init__(self,  no, alamat, name, telp, email, lingkup):
        self.Akreditasi = no
        self.masa_berlaku_akreditasi = email
        self.nama_Lab = name
        self.alamat = alamat
        self.telepon = telp
        self.lingkup = lingkup


class MainData:
    def __init__(self, alladdress):
        self.semuaAlamat = alladdress


#print(json.dumps(testingData, indent=8, ensure_ascii=False))
# alamat
tempheadList = []
headList = []
mainList = []
alamat = []
i = 1
key = "default"
for kk in testingData["OTO"]:
    temp = kk["ALAMAT "]
    noAkreditasi = kk["NO. AKREDITASI"]
    name = kk["NAMA LABORATORIUM"]
    telp = kk["TELEPON"]
    berlaku = kk["MASA BERLAKU AKREDITASI"]
    lingkup = kk["LINGKUP"]

    if key != temp:
        tempheadList.append(
            merge(noAkreditasi, temp, name, telp, berlaku, lingkup))
        print(name, i)
        i += 1
        key = temp
# remove duplicate


filterData = list(set(tempheadList))

# namabah induk json
# koko = {}
# koko["jajal"] = filterData


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def replace(kk):
    kk.replace("\n", "")
    return kk


# make array on object
mainList.append(MainData(tempheadList))
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
