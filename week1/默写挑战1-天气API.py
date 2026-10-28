# -*- coding: utf-8 -*-
"""
默写挑战 1：天气 API（第 1 周教程第 1-2 节内容）

规则：
1. 不翻教程，把 ____N____ 填空补全
2. 卡住先自己想 2 分钟，实在不行再翻教程，并记下卡点
3. 运行成功（打印出北京天气）算过关
4. 过关后，隔半天再从空白文件整个重写一遍

运行：python 默写挑战1-天气API.py
"""
import requests

URL = "____1____"            # 天气服务的地址（open-meteo）
params = {
    "latitude": 39.9042,     # 北京的纬度
    "longitude": 116.4074,   # 北京的经度
    "current": "____2____",  # 要哪些数据：温度 + 天气代码
}
resp = requests.____3____(URL, params=params, timeout=30)   # 发哪种请求？
data = ____4____            # 把响应解析成 Python 字典
temp = data["____5____"]["temperature_2m"]   # 温度藏在哪一层？
print(f"北京现在气温 {temp}°C")

# 我的卡点记录（每翻一次教程记一笔）：
# 1. ____6____
# 2.
