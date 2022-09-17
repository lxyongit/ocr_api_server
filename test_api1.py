#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/1/6 23:28
# @Author  : sml2h3
# @Email   : sml2h3@gmail.com
# @File    : test_api.py
# @Software: PyCharm
import base64
import json
import requests

print(' ')
# ******************OCR识别部分开始******************
host = "http://127.0.0.1:9898"
# 目标检测就把ocr改成det,其他相同
# 方式一
file = open(r'test.jpg', 'rb').read()
# file = open(r'test_calc.png', 'rb').read()

# 滑块识别

target_file = open(r'match_bg.png', 'rb').read()
bg_file = open(r'match_bg.png', 'rb').read()

# api_url = f"{host}/slide/match/file/json"
# resp = requests.post(api_url, files={'target_img': target_file, 'bg_img': bg_file})
# print(f"{api_url=}, {resp.text=}")

api_url = f"{host}/slide/match/b64"
target_b64str = base64.b64encode(target_file).decode()
bg_b64str = base64.b64encode(bg_file).decode()

jsonstr = json.dumps({'target_img': target_b64str, 'bg_img': bg_b64str})

api_url = f"{host}/slide/match/b64/json"
resp = requests.post(api_url, data=base64.b64encode(jsonstr.encode()).decode())
print(f"{api_url=}, {resp.text=}")