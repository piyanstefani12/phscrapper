import set
import requests as re
from bs4 import BeautifulSoup

def main(inputed=input("Masukkan Link: "), jumlah=int(input("Masukkan Jumlah Halaman"))):
    set.halaman1(porns=inputed)
    for i in range(2, jumlah+1):
        linkstr = str(f"{inputed}?page={i}")
        set.halaman1(linkstr)
        print(linkstr)

main()