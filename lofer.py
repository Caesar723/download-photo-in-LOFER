from urllib import request
from bs4 import BeautifulSoup
im=0
def get(a):
    global imm
    url="https://aliizia.lofter.com/?page="+str(a)
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    req=request.Request(url,headers=header)
    response=request.urlopen(req)

    data = response.read()
    data=str( data,encoding="utf-8")
    be=BeautifulSoup(data,"html.parser")
    imm=be.find_all("img")
def download(n):
    global imm
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    im=imm[n]["src"]
    img = request.Request(im, headers=head)
    img = request.urlopen(img)
    img = img.read()
    with open("lofer lz/" + str(i) + "-" + str(n) + ".jpg", mode='wb') as f:
        f.write(img)
for i in range(1,18):
    get(i)
    for b in range(1,len(imm)):
        download(b)


