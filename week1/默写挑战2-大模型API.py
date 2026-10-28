# -*- coding: utf-8 -*-
"""
默写挑战 2：大模型 API 最小骨架（第 1 周教程第 3-5 节内容）

规则：
1. 不翻教程，把 ____N____ 填空补全
2. 运行前先设置：$env:DEEPSEEK_API_KEY = "sk-你的key"
3. 运行成功（AI 用一句话回答"什么是 API"）算过关
4. 过关后，隔半天从空白文件整个重写一遍

运行：python 默写挑战2-大模型API.py
"""
import os
import requests

API_KEY = os.environ.get("____1____")   # 从环境变量取什么？
URL = "https://api.deepseek.com/chat/completions"

payload = {
    "model": "____2____",                # 用哪个模型？
    "messages": [
        {"role": "____3____", "content": "你是简洁的中文助手"},
        {"role": "user", "content": "用一句话解释什么是 API"},
    ],
    "temperature": 0.7,
}
headers = {
    "Authorization": f"Bearer ____4____",   # 带上谁？
    "Content-Type": "application/json",
}
resp = requests.____5____(URL, json=payload, headers=headers, timeout=60)  # 发哪种请求？
answer = resp.json()["____6____"][0]["message"]["content"]   # 答案藏在哪一层？
print(f"AI：{answer}")

# 我的卡点记录（每翻一次教程记一笔）：
# 1. ____7____
# 2.
