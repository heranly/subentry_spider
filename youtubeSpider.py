#_*_encoding:utf-8_*_
from pytube import YouTube
from multiprocessing import Pool
import time
import re
import os
import requests
import logging
import socket
socket.setdefaulttimeout(20)

#保存日志
logging.basicConfig(filename ='E:\youtube\log.txt', level = logging.DEBUG,format="%(levelname)s:%(asctime)s:%(message)s")

def get_str(id_url):
    """
    获取视频链接id
    :param id_url:
    :return:
    """
    print("starting download code...")
    lst = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Referer": "https://research.google.com/youtube8m/explore.html",
    }
    response = requests.get(id_url,headers=headers).text
    ids_str = re.findall("(\[.*\])",response)[0]
    id1=ids_str.split(",")
    id1[0]=id1[0].replace('[','')
    id1[-1]=id1[-1].replace(']','')
    for id in id1:
        url = "https://storage.googleapis.com/data.yt8m.org/2/j/i/{0}/{1}.js".format(id[1:3],id[1:-1])
        resp = requests.get(url,headers=headers).text
        get_str=resp.split(",")[-1].split(")")[0]
        lst.append(get_str)
    return lst


def download_video(url,keyword):
    """
    下载视频
    :param url:
    :param keyword:
    :return:
    """
    storePath = "E:\youtube\{}".format(keyword)
    if not os.path.exists(storePath):
        os.mkdir(storePath)
    try:
        YouTube(url).streams.first().download(storePath)
        print(url,"download compete",)
    except Exception as e:
        print("DOENLOAD ERROR:",e)
        logging.error("url error:{}".format(url))
        print("This url is:",url)
        time.sleep(5)
        pass

if __name__ == "__main__":
    pool=Pool(20)
    keyword="Car"
    total_id_url = "https://storage.googleapis.com/data.yt8m.org/2/j/v/0k4j.js"
    ids = get_str(total_id_url)
    print("total number",len(ids))
    for id in ids:
        real_url = "https://www.youtube.com/watch?v={}".format(id[1:-1])
        pool.apply_async(download_video,args=(real_url,keyword))
    pool.close()
    pool.join()
































