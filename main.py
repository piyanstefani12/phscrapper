import set
import requests as re
from bs4 import BeautifulSoup

def main(inputed=input("Masukkan Link: "), jumlah=2):
    set.halaman1(porns=inputed)
    for i in range(2, jumlah):
        linkstr = str(f"{inputed}?page={i}")
        set.halaman1(inputed + linkstr)
        print(inputed + linkstr)

main(inputed="https://www.pornhub.com/pornstar/eliza-ibarra/videos", jumlah=13)