# coding:utf-8
"""
Name : test.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/25 14:57
Desc:
"""
import os

import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
id = 28875146
name = '海阔天空'
path_dir = './music'
path = os.path.join(path_dir, str(name) + '.mp3')
with open(path, mode='wb') as f:
    music_content = requests.get(url="http://music.163.com/song/media/outer/url?id={}.mp3".format(id),
                             headers=headers).content
    f.write(music_content)

