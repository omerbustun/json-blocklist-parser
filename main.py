import json 
import fileinput
import wget
import os

if os.path.exists("list.json"):
  os.remove("list.json")
  print("Old list found and deleted")
  print("Downloading new list")
else:
  print("List not found, downloading new list")

url = 'https://raw.githubusercontent.com/MISP/misp-warninglists/main/lists/vpn-ipv4/list.json'
filename = wget.download(url)

with open('list.json') as f:
  data = json.load(f)

file = open('IP_List.txt', 'w+')
file.write(str(data["list"]))
print("TXT file created")

with open('IP_List.txt', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(',', '\n')
filedata = filedata.replace('\'', ' ')
filedata = filedata.replace('[', ' ')
filedata = filedata.replace(']', ' ')
print("\nOperators removed")

with open('IP_List.txt', 'w') as file:
  file.write(filedata)
print("Output file created")

file.close()

