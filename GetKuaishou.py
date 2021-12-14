import json
import requests

def GetUrl(userid,number):
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
               "userId": "%s",
               "pcursor": "",
        "page": "profile"
      }"""%userid,
        "query": "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
    }
    response = requests.post(url=url, headers=headers, data=data).text
    res = json.loads(response)
    url_list = []
    for i in range(0, int(number)):
        url = res["data"]["visionProfilePhotoList"]["feeds"][i]["photo"]["photoUrls"][1]["url"]
        url_list.append(url)
    return url_list

def save(list):
    for i in range(0, len(list)):
        if i < len(list):
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
            }
            videofile = requests.get(url=list[i], headers=headers).content
            with open(fr".\video\video{i}.mp4", "wb") as f:
                f.write(videofile)
            print(f"视频{i}保存成功！")

        else:
            print("Successfully!!!")



userid=str(input("请输入userid"))
number=input("请输入获取视频条数")
list=GetUrl(userid,number)
save(list)
