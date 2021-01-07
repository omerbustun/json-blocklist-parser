import json 
import fileinput
import wget
import os

if os.path.exists("list.json"):
  os.remove("list.json")
  print("Eski dosya mevcut, siliniyor...")
  print("Yeni dosya indiriliyor...")
else:
  print("Dosya mevcut değil, indiriliyor...")

url = 'https://raw.githubusercontent.com/MISP/misp-warninglists/main/lists/vpn-ipv4/list.json'
filename = wget.download(url)

with open('list.json') as f:
  data = json.load(f)

file = open('IP_Listesi.txt', 'w+')
file.write(str(data["list"]))
print("TXT dosyası oluşturuldu...")

with open('IP_Listesi.txt', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(',', '\n')
filedata = filedata.replace('\'', ' ')
filedata = filedata.replace('[', ' ')
filedata = filedata.replace(']', ' ')
print("\nOperatorler temizlendi...")

with open('IP_Listesi.txt', 'w') as file:
  file.write(filedata)
print("Çıktı oluşturuldu...")

file.close()

