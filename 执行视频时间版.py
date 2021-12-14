import time
import win32api
import win32con
import json
import os
import requests
import threading

def GetUrl():
    url = 'https://www.kuaishou.com/graphql'
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Host": "www.kuaishou.com",
        "Sec-Fetch-Site": "same-origin",
        "Cookie": "did=web_e729337906ec45878185571cfc3fc3d0; didv=1635087796000; clientid=3; client_key=65890b29; kpf=PC_WEB; kpn=KUAISHOU_VISION; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjc1MjEyODM3LjE2MzkzODg1ODIwNTMuMTA3ODUzODA=|MS43NjQ1ODM2OTgyODY2OTgyLjk2MTgzNTczLjE2MzkzODg1ODIwNTMuMTA3ODUzODE=|0|graphql-server|webservice|false|NA"
    }
    data = {
        "operationName": "visionProfilePhotoList",
        "variables": """{
        "userId": "3x4z2agpxub4qmg",
        "pcursor": "",
        "page": "profile"
      }""",
        "query": "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
    }
    response = requests.post(url=url, headers=headers, data=data).text
    res = json.loads(response)
    url_list = []
    for i in range(0, 20):
        url = res["data"]["visionProfilePhotoList"]["feeds"][i]["photo"]["photoUrls"][1]["url"]
        url_list.append(url)
    return url_list

def StartVideo(w,h):
    os.system(fr".\Fplay\ffplay.exe  .\video\video.mp4 -noborder -x {w} -y {h} -loop 0")

def adjustBack():
       urllists=GetUrl()
       for i in  range(0,len(urllists)):
           if i+1 < len(urllists):
               headers = {
                   "Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
               }
               videofile = requests.get(url=urllists[i], headers=headers).content
               with open(r".\video\video.mp4", "wb") as f:
                   f.write(videofile)
               w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
               h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
           else:
               i=0


adjustBack()