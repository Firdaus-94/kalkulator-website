import os,sys,time,requests,json
from os import system
from time import sleep

system("clear")


number = input("masukan nomor : ")

headers = {
"Origin":"https://www.mapclub.com",
"Accept":"application/json, text/plain, */*",
"Accept-Language":"in-ID",
"Authorization":"BaerereyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOil3ZmMwZjhhYy1hYjYOLTRhYTktODI4MS0zMzc5ZGYyNjViMjQiLCJleHBpcmVkljoxNzc3NDc3NDYxMzY0LCJleHBpcmUiOjM2MDAslmV4cCI6MTc3NZQ3NzQ2MSwiaWF0ljoxNzc3NDczODYxLCJwbGF0Zm9ybSI6lldFQiJ9.3PakpQ3XjkZt699tjZ9wYMu290HJUjn1Rsko6z1coRvFopdKvrAX40cy8FfcwOS6RYscgLOopUNu8gxrAaiubQ",
"Client-Platform":"WEB",
"Client-Timestamp":"1777473963792",
"Content-Length":"39",
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
      post = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP",headers=headers,data=data)
      print (post)
