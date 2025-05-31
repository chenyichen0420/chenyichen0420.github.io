```python
import requests
head = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "referer":"https://paper.i21st.cn/",
    "range":"bytes=0-8388608",
    "if-none-match":"\"68186792-2fc31c\"",
    "if-modified-since":"Mon, 01 May 2025 00:00:00 GMT"
}
url = input("please input the url of the webpage:\n")
resp = requests.get(url=url, headers=head).text
bep = resp.find(r"<audio controls='controls' src='")
enp = resp.find(r"'></audio>")
bep += len(r"<audio controls='controls' src='")
url = resp[bep:enp]
print(url)
back = requests.get(url,headers=head)
if back.status_code == 206 or back.status_code == 200:
    with open("audio.mp3",'wb') as f:
        f.write(back.content)
# VIP教师会员和本期电子版订户登录后下载 - out！
```
