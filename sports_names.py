import requests
from bs4 import BeautifulSoup
import urllib

# str=['cricket','badminton','tennis','archery','kabaddi','icehockey24','hockey']

file = open("1.txt","r")
s = file.read()
str = s.split()
# print(str)
z=0
def fun(source):
    c=0
    x=-1
    while c < len(str):
        x=source.find(str[c])
        if x>-1:
            print (str[c])
            z=c
            break
        else:
            z=-1
            c=c+1
    if z >=0 :
           momo='l' # print(str[z])
    else:
            print("NA")
    return
fp = open("myfile.txt","r")
lines= fp.read().splitlines()
for l in lines:
    if l!="":

        f=l.find("www.")
        f1=l.find("http://")
        if f>-1 and f1==-1:
            l=l.replace("www.","http://");
        print(l+" : "),
        try:
            r= requests.get(l)
            soup=BeautifulSoup(r.content,"html.parser")
            s=soup.prettify()
            fun(s)
        except :
            print("Invalid Website")
fp.close()
file.close()
