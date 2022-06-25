# coding:utf-8
"""
Name : crawl.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/25 12:07
Desc:   crawl wangyiyun music
"""
import os

import requests
import re

def main():
    """
    主函数
    """
    url = "https://music.163.com/playlist?id=7440011920"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    response = requests.get(url=url, headers=headers)
    if not os.path.exists("./music"):
        os.mkdir('./music')
    path_dir = './music'
    try:
        if response.status_code == 200:
            musics = re.findall('a href="/song(.*?)</a>', response.text)
            music_id = re.findall(r'id=(.*?)">[\u4e00-\u9fa5]', str(musics))
            music_name = re.findall('[\u4e00-\u9fa5]+', str(musics))
            href = zip(music_id,  music_name)

            for id, name in href:
                path = os.path.join(path_dir, str(name) + '.mp3')
                with open(path, mode='wb') as f:
                    music_content = requests.get(url="http://music.163.com/song/media/outer/url?id={}.mp3".format(id), headers=headers).content
                    f.write(music_content)
    except requests.ConnectionError as e:
        print(e)


if __name__ == '__main__':
    main()