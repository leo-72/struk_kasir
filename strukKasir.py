# CREATED BY NADHIF Leopard27
# PROGRAM MEMBUAT STRUK KASIR

import os
import datetime

print("\n")
codebon="0432"
bon="555-28123Y58"
kasir=str(input("Masukkan Nama Pegawai\t: "))
nomor=int(input("Nomor Telepon ex:62...\t: "))
pulsa=int(input("Masukkan Nominal Pulsa\t: "))
addPulsa=2000
print("Harga Barang adalah\t:", pulsa+addPulsa)
totItem=int(input("Masukkan Total Item\t: "))
uang=int(input("Masukkkan Uang Customer\t: "))
codePulsa="EVE TSEL AAP 10"
plu="420903"
jumlah=(pulsa+addPulsa)*totItem
kembalian=uang-jumlah
tnw=datetime.datetime.now()
tanggal="%s-%s-%s" % (tnw.day, tnw.month, tnw.year)
waktu="%s:%s:%s" % (tnw.hour, tnw.minute, tnw.second)
versiondate="V.2020.11.2"
codeVoucher="1"
ref="64827948"
serialNum="02188100001970646201"

if uang >= jumlah:
    print("\n")
    print("Bon {}-{} Kasir : {}".format(codebon, bon, kasir))
    print("=======================================")
    print("{}  {} \t {} \t {}".format(codePulsa, totItem, pulsa+addPulsa, jumlah))
    print("---------------------------------------")
    print("Total item \t {} \t \t {}".format(totItem, jumlah))
    print("Tunai \t \t \t \t {}".format(jumlah))
    print("Kembalian \t \t \t {}".format(kembalian))
    print("=======================================")
    print("Tgl. {}  {}  {}".format(tanggal, waktu, versiondate))
    print("---------------------------------------")
    print("Bukti Transfer Voucher")
    print("Plu \t : {} {} K".format(plu, codePulsa))
    print("No Bon \t : {} ".format(bon))
    print("Kode Voucher \t : {}".format(codeVoucher))
    print("Nomor Telepon \t : {}".format(nomor))
    print("---------------------------------------")
    print("No. Ref : {}".format(ref))
    print("No. Bon : {}-{}".format(codebon, bon))
    print("Tanggal : {} {}".format(tanggal, waktu))
    print("Item \t: ({}){} K".format(plu, codePulsa))
    print("MSISDN \t: {}".format(nomor))
    print("Denom \t: {}".format(pulsa))
    print("Serial \t: {}".format(serialNum))
    print("Status \t: SUKSES")
    print("---------------------------------------")
    print(""" """)
    print("""
    Untuk keluhan/gangguan hubungi
            0812-1010-6188
              Terimakasih
    """)
    print("---------------------------------------")
    print("---------------------------------------")
    print("Kritik&Saran:1500959, SMS: 0817111234")
    print("\n")

elif uang < jumlah:
    print("\n")
    print("Bon {}-{} Kasir : {}".format(codebon, bon, kasir))
    print("=======================================")
    print("{}  {} \t {} \t {}".format(codePulsa, totItem, pulsa+addPulsa, jumlah))
    print("---------------------------------------")
    print("Total item \t {} \t \t {}".format(totItem, jumlah))
    print("Tunai \t \t \t \t {}".format(jumlah))
    print("Kembalian \t \t \t {}".format(kembalian))
    print("=======================================")
    print("Tgl. {}  {}  {}".format(tanggal, waktu, versiondate))
    print("---------------------------------------")
    print("Bukti Transfer Voucher")
    print("Plu \t : {} {} K".format(plu, codePulsa))
    print("No Bon \t : {} ".format(bon))
    print("Kode Voucher \t : {}".format(codeVoucher))
    print("Nomor Telepon \t : {}".format(nomor))
    print("---------------------------------------")
    print("No. Ref : {}".format(ref))
    print("No. Bon : {}-{}".format(codebon, bon))
    print("Tanggal : {} {}".format(tanggal, waktu))
    print("Item \t: ({}){} K".format(plu, codePulsa))
    print("MSISDN \t: {}".format(nomor))
    print("Denom \t: {}".format(pulsa))
    print("Serial \t: {}".format(serialNum))
    print("Status \t: GAGAL")
    print("---------------------------------------")
    print(""" """)
    print("""
    Untuk keluhan/gangguan hubungi
            0812-1010-6188
              Terimakasih
    """)
    print("---------------------------------------")
    print("---------------------------------------")
    print("Kritik&Saran:1500959, SMS: 0817111234")
    print("\n")
    