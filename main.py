import json 
import fileinput
import wget
import os

if os.path.exists("list.json"):
  os.remove("list.json")
else:
  print("Dosya mevcut değil, yeniden indiriliyor.")

url = '<URL>'
filename = wget.download(url)

with open('list.json') as f:
  data = json.load(f)

  #print(data)

#print(data['list'])
#print(str(data))
file = open('IP_Listesi.txt', 'w+')
file.write(str(data["list"]))

with open('IP_Listesi.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(',', '\n')
filedata = filedata.replace('\'', ' ')
filedata = filedata.replace('[', ' ')
filedata = filedata.replace(']', ' ')


with open('IP_Listesi.txt', 'w') as file:
  file.write(filedata)


file.close()