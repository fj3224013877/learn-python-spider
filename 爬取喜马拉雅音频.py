import requests
HEADERS = {
            "cookie":"x-ats=ACMxY2I3MmM1NDAwNjg2OTI5r_WDEIgHk4J4bXdlYl93d3c; _xmLog=h5&caf44b56-9a44-47cc-a8da-04f4e88bb1c5&process.env.sdkVersion; 1&remember_me=y; 1&_token=493897527&FC9354C0340NB35548FEFCAC1425426ED49FEAA689299D5975A3E1DAFEF5F8DDA5063C9F47D3153M98F930293B84A8C_; xm-page-viewid=ximalaya-web; DATE=1724251967428; wfp=ACMxNzA5ZWZhMzYzMGRiYmI3b6DjG4JJRnh4bXdlYl93d3c; crystal=U2FsdGVkX19DiG/ut/mK/WYTh91BCtRPC5QXJCipa6wIYMh8zlcR5ll+mo1B7KGfsq/zZ9oXjfl2GdjAE7FbI3hTQkKvksTZSAlSm6SZ4HXVYZgfshuHax3Tv7tmyDAMmHLI/x4gEPzNYLSNbqIQ/RRM9WXj+FH2jSnxJ6FvRWdhcZjUSaQBTIQFRFkrDYVYMNljnLm7ipmpMnK8+AKFzObGUGQFlxqEgrRpNRsSMALE7q5wOGfjnJ1jz2nYIJ1K; impl=www.ximalaya.com.login; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1724251969; HMACCOUNT=F85CAA59AC895F10; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1724338314; cmci9xde=U2FsdGVkX1+sntrimgbxJlCuj+DlNluy8E4PhloXv7atVsvzogN2vR0N5yIxSQQLbSzD3oJgYgAkj/n89K9Rkw==; pmck9xge=U2FsdGVkX1+0TF3ZRQV+49nb+I/B65X5sBIJnQf3siI=; assva5=U2FsdGVkX1+wCvLDzsldhoQA5alwxg2oHSZTNvRXH8uPKGbbjIzLsByU1q2oejWIrqoSf4q7i4m9FlRj8bsZvQ==; vmce9xdq=U2FsdGVkX185+pbhODHHFadW4CJTQh8LaBDGRe82uBKzhUKMVwyEkbpS6mfJZST5wNrKG2tOadUsk5uCRUv+BEc/15EBh8knz+F0fyu/IDXCbD6thA97wrL4A8f9R94PUA7+QXc7b0WW5Y6H88+p6vE4pA7nav8QyqQA1Vp+0/I=; assva6=U2FsdGVkX19IkUxLN+uj2iSRxGgya0mJ78zyxM/amkOrwpjxcn22PmOAH3G0Wx0+1iaJXYyxJBYKO1Ou0NfJfQ==",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
            "referer":"https://www.ximalaya.com/album/71143288"
            }
    
url = "https://www.ximalaya.com/mobile-playpage/track/v3/baseInfo/1724338629286?device=www2&trackId=570761677&trackQualityLevel=1"

response = requests.get(url=url,headers=HEADERS)
json_date = response.json()
title = json_date['trackInfo']['title']
Mw = json_date['trackInfo']['playUrlList'][0]['url']
print(title)
print(Mw)

#大秦004造纸术丨听友裙 684914202
#IjX71DVijcqhvj84DExznjkN5cGL7BIPdiV97-Eo5cVkYe4bLi0YV2ZBan1FLYHL4OPkdsHspGzbBpoBLADvJx_baQhYVMXKuK2k6tXMgM-MSMAOQiD_AFCqRwSbNfQOZMFmPKKhr__3KyPJRNGVyvA9opZhjqR2p69ElziHD08v5aG_SeYlaRCff73QZvDy0gVsqi5Nz-kADgXvnIcYhqPloUQG-cCt9XRZDUrRFN9tNCbqqnPPlnrdXfg4FdvjzGErDI1bbAcZI0GSmdN785DhpSiHuXQPMa9EZ-H4m2ztFPnOAAlFs06rdx4#爬取到名称与下载链接密文，暂时不会解密
