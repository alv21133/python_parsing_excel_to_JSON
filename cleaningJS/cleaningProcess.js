var fs = require("fs");
let jsonData = require("./pengujianOtomotif.json");
let i = 1;

var sasoriObject = [];
var bidangObject = [];
var metodeObject = [];
var bidangObjectold = [];
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

    // MAIN DATA FOR JSON
    if (keterangan == "--") {
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
      i++;
      bidangObject = [];
      DataArray = {};
    }

    // if (bidangKey != bidangPengukuran) {
    //   if (valuePertama != bidangPengukuran) {
    //     let bidanngArray = {};
    //     bidanngArray.Bidang = bidangPengukuran;
    //     bidanngArray.perusahaan = nameLab;
    //     bidangObject.push(bidanngArray);
    //   }
    // }

    function dataPengukuran() {
      let myArray = {};
      myArray.jenisPengujian = jenisUji;
      myArray.MetodePengujian = metodeUji;
      metodeObject.push(myArray);
    }

    if (i <= 6) {
      console.log(i);
      if ((i = 6)) {
        if (bidangKey != bahanUji) {
          let myArray = {};
          myArray.Bidang = bidangPengukuran;
          myArray.bahanYangdiUji = bahanUji;
          myArray.MetodePengujian = metodeObject;
          bidangObject.push(myArray);
          metodeObject = [];
        }
      }
    } else {
      if (bidangKey != bahanUji) {
        let myArray = {};
        myArray.Bidang = bidangPengukuran;
        myArray.bahanYangdiUji = bahanUji;
        myArray.MetodePengujian = metodeObject;
        bidangObject.push(myArray);
        metodeObject = [];
      }
    }

    dataPengukuran();
    bidangKey = bahanUji;
    metodeKey = metodeUji;
    globalkey = noAkre;
    i++;
  });
}

mapping();
console.log(sasoriObject[0]);
fs.writeFileSync("result2.json", JSON.stringify(sasoriObject));
