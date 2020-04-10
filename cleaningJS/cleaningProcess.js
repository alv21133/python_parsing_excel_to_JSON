var fs = require("fs");
let jsonData = require("./pengujianOtomotif.json");
let sparatorJson = require("./sparator.json");
let i = 0;
let ii = 1;

var sasoriObject = [];
var bidangObject = [];
var metodeObject = [];
var positionObejct = [];
let valuePertama = "";
let globalkey = "";
let metodeKey = "";
let bidangKey = "";
let DataArray = {};
var noAkre = "";
console.log(bidangKey);

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
    bidangPengukuran = key["BIDANG PENGUJIAN"];
    bahanUji = key["BAHAN ATAU PRODUK YANG DIUJI"];
    jenisUji = key["JENIS PENGUJIAN ATAU SIFAT-SIFAT YANG DIUKUR"];
    metodeUji = key["METODE PENGUJIAN, TEKNIK YANG DIGUNAKAN"];
    keterangan = key["KETERANGAN"];

    // mapping fisrt value
    // if (globalkey != noAkre) {
    //   let bidanngArray = {};
    //   bidanngArray.Bidang = bidangPengukuran;
    //   bidanngArray.perusahaan = nameLab;
    //   bidangObject.push(bidanngArray);
    //   valuePertama = bidangPengukuran;
    // }

    function dataPengukuran() {
      i += 1;
      let myArray = {};
      myArray.jenisPengujian = jenisUji;
      myArray.MetodePengujian = metodeUji;
      metodeObject.push(myArray);
    }
    dataPengukuran();
    sparatorJson.forEach((value) => {
      if (i == value["posisipembeda"]) {
        let myArray = {};
        myArray.Bidang = bidangPengukuran;
        myArray.bahanYangdiUji = bahanUji;
        myArray.MetodePengujian = metodeObject;
        bidangObject.push(myArray);
        metodeObject = [];
      }
    });

    // MAIN DATA FOR JSON
    if (keterangan == "--") {
      console.log(ii);

      DataArray.nomorAkreditasi = noAkre;
      DataArray.namaLaboratorium = nameLab;
      DataArray.alamat = alamat;
      DataArray.propinsi = propinsi;
      DataArray.negara = negara;
      DataArray.telepon = telp;
      DataArray.email = email;
      DataArray.lingkup = lingkup;
      DataArray.BidangPengujian = bidangObject;
      sasoriObject.push(DataArray);
      bidangObject = [];
      DataArray = {};

      ii += 1;
    }

    // if (bidangKey != bidangPengukuran) {
    //   if (valuePertama != bidangPengukuran) {
    //     let bidanngArray = {};
    //     bidanngArray.Bidang = bidangPengukuran;
    //     bidanngArray.perusahaan = nameLab;
    //     bidangObject.push(bidanngArray);
    //   }
    // }

    // if (i > 4) {
    //   if (bidangKey != bahanUji) {
    //     positionArray = {};
    //     positionArray.posisipembeda = i-1;
    //     positionArray.namaBahan = bahanUji;
    //     positionArray.nomer = noAkre;
    //     positionArray.nameLab = nameLab;
    //     positionObejct.push(positionArray);
    //     let myArray = {};
    //     myArray.Bidang = bidangPengukuran;
    //     myArray.bahanYangdiUji = bahanUji;
    //     myArray.MetodePengujian = metodeObject;
    //     bidangObject.push(myArray);
    //     metodeObject = [];
    //   }
    // }

    // if (i > 6) {
    //   dataPengukuran();
    // }
    // if (bidangKey != bahanUji) {
    //   let myArray = {};
    //   myArray.Bidang = bidangPengukuran;
    //   myArray.bahanYangdiUji = bahanUji;
    //   myArray.MetodePengujian = metodeObject;
    //   bidangObject.push(myArray);
    //   metodeObject = [];
    // }
    bidangKey = bahanUji;
    metodeKey = metodeUji;
    globalkey = noAkre;
  });
}

mapping();
fs.writeFileSync("cleaningStep2.json", JSON.stringify(sasoriObject));
