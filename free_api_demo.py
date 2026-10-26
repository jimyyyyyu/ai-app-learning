# -*- coding: utf-8 -*-
"""
练习：用 requests 调用免费 API（无需注册、无需 key，立刻能跑）

接口：Open-Meteo 免费天气接口
任务：查询北京当前的天气和气温
运行：python free_api_demo.py
"""
import requests

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.9042,    # 北京的纬度
    "longitude": 116.4074,  # 北京的经度
    "current": "temperature_2m,weather_code",  # 要哪些数据
    "timezone": "Asia/Shanghai",
}

# 1. 发请求
resp = requests.get(URL, params=params, timeout=30)
resp.raise_for_status()   # 失败立刻报错
data = resp.json()        # 2. 解析 JSON

# 3. 取出想要的数据
temp = data["current"]["temperature_2m"]
code = data["current"]["weather_code"]
weather = {
    0: "晴", 1: "基本晴", 2: "多云", 3: "阴",
    45: "雾", 61: "小雨", 80: "阵雨",
}.get(code, f"未知代码 {code}")

print(f"北京现在：{weather}，气温 {temp}°C")
print()
print("你已经完成：发 HTTP 请求 → 解析 JSON → 取出数据")
print("挑战：把经纬度换成你所在的城市（搜索“城市名 经纬度”），再跑一次")
