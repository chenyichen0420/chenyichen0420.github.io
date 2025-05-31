import requests
import re
import json
import time
cookie_val = input('Insert your cookie here.\n')
cnt = int(input("input hack cnt\n"))
save = {-1:"example"}
erlist = {}
print("Insert hack id here")
for i in range(0,cnt):
    save[i] = input()
for i in range(0,cnt):
    bid = save[i]
    url = 'https://www.bilibili.com/video/'
    url = url + bid + '/'
    cookie = cookie_val
    headers = {
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie": cookie
    }
    try:
        response = requests.get(url=url, headers=headers)
        html = response.text
        title = re.findall('title="(.*?)"', html)[0]
        info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        json_data = json.loads(info)
        video_url = json_data['data']['dash']['video'][0]['baseUrl']
        audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
        video_content = requests.get(url=video_url, headers=headers, stream=True).content
        audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
    except:
        print("unable to get "+bid)
        print("retry latter")
        erlist[len(erlist)]=bid
        time.sleep(15)
        continue
    with open('video\\' + bid + '.mp4', mode='wb') as v:
        v.write(video_content)
    with open('video\\' + bid + '.mp3', mode='wb') as a:
        a.write(audio_content)
    print(bid + ' finished!')
    time.sleep(5)
cnt=len(erlist)
for i in range(0,cnt):
    bid = erlist[i]
    url = 'https://www.bilibili.com/video/'
    url = url + bid + '/'
    cookie = cookie_val
    headers = {
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie": cookie
    }
    try:
        response = requests.get(url=url, headers=headers)
        html = response.text
        title = re.findall('title="(.*?)"', html)[0]
        info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        json_data = json.loads(info)
        video_url = json_data['data']['dash']['video'][0]['baseUrl']
        audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
        video_content = requests.get(url=video_url, headers=headers, stream=True).content
        audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
    except:
        print("unable to get "+bid)
        print("retry latter")
        erlist[len(erlist)]=bid
        time.sleep(15)
        continue
    with open('video\\' + bid + '.mp4', mode='wb') as v:
        v.write(video_content)
    with open('video\\' + bid + '.mp3', mode='wb') as a:
        a.write(audio_content)
    print(bid + ' finished!')
    time.sleep(5)
for i in range(cnt,len(erlist)):
    bid = erlist[i]
    url = 'https://www.bilibili.com/video/'
    url = url + bid + '/'
    cookie = cookie_val
    headers = {
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie": cookie
    }
    try:
        response = requests.get(url=url, headers=headers)
        html = response.text
        title = re.findall('title="(.*?)"', html)[0]
        info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        json_data = json.loads(info)
        video_url = json_data['data']['dash']['video'][0]['baseUrl']
        audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
        video_content = requests.get(url=video_url, headers=headers, stream=True).content
        audio_content = requests.get(url=audio_url, headers=headers, stream=True).content
    except:
        print("unable to get "+bid)
        print("please handle it on hand")
        time.sleep(15)
        continue
    with open('video\\' + bid + '.mp4', mode='wb') as v:
        v.write(video_content)
    with open('video\\' + bid + '.mp3', mode='wb') as a:
        a.write(audio_content)
    print(bid + ' finished!')
    time.sleep(5)
