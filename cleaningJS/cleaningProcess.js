let jsonData = require("./pengujianFinal.json");
let i = 1;

var sasoriObject = [];
var bidangObject = [];
let globalkey = "";
let bidangKey = "";
var noAkre = "";
function mapping() {
  jsonData["OTO"].forEach((key) => {
    noAkre = key["NO. AKREDITASI"];
    nameLab = key["NAMA LABORATORIUM"];
    alamat = key["ALAMAT "];
    propinsi = key["PROPINSI"];
    negara = key["NEGARA"];
    telp = key["TELEPON"];
    email = key["EMAIL"];
    lingkup = key["LINGKUP"];
    let DataArray = {};
    if (globalkey != noAkre) {
      DataArray.nomorAkreditasi = noAkre;
      DataArray.namaLaboratorium = nameLab;
      DataArray.alamat = alamat;
      DataArray.propinsi = propinsi;
      DataArray.negara = negara;
      DataArray.telepon = telp;
      DataArray.email = email;
      DataArray.lingkup = lingkup;
      DataArray.BidangPengukuran = JSON.stringify(bidangObject)
      sasoriObject.push(DataArray);
      i++;
      bidangObject = [];
      console.log(i);
    }
    if (bidangKey != key["BIDANG PENGUJIAN"]) {
      let bidanngArray = {};
      bidanngArray.Bidang = key["BIDANG PENGUJIAN"];
      bidangObject.push(bidanngArray);
    }
    bidangKey = key["BIDANG PENGUJIAN"];
    globalkey = key["NO. AKREDITASI"];
  });
}

mapping();
console.log(sasoriObject);
