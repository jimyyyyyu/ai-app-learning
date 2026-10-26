# -*- coding: utf-8 -*-
"""
第 1 周实战：调用 DeepSeek 大模型 API —— 你的第一个 AI 程序

使用前：
1. 打开 https://platform.deepseek.com 注册，创建 API Key（只显示一次，请复制保存）
2. 设置环境变量（PowerShell 里执行）：
       $env:DEEPSEEK_API_KEY = "sk-你的key"
3. 运行：
       python hello_ai.py
"""
import os
import requests

API_KEY = os.environ.get("DEEPSEEK_API_KEY")
URL = "https://api.deepseek.com/chat/completions"

if not API_KEY:
    print("未找到 API Key！请先设置环境变量：")
    print('    $env:DEEPSEEK_API_KEY = "sk-你的key"')
    raise SystemExit(1)


def chat(messages):
    """把对话历史发给大模型，返回模型的回复。"""
    payload = {
        "model": "deepseek-chat",      # 要调用的模型
        "messages": messages,          # 对话历史（system/user/assistant）
        "temperature": 0.7,            # 0 = 严谨，1 = 发散
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    resp = requests.post(URL, json=payload, headers=headers, timeout=60)
    resp.raise_for_status()  # 网络或鉴权出错时直接抛出，方便排查
    return resp.json()["choices"][0]["message"]["content"]


def main():
    print("=" * 42)
    print("你的第一个 AI 程序：命令行聊天机器人")
    print("输入 quit 退出")
    print("=" * 42)

    # messages 是"对话历史"：发给模型的不是一句话，而是整个聊天记录
    messages = [
        {"role": "system", "content": "你是一个耐心友好的中文学习助手。"}
    ]

    while True:
        try:
            user_input = input("\n你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break
        if user_input.lower() in ("quit", "exit", "退出"):
            print("再见！")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        try:
            reply = chat(messages)
        except Exception as e:  # 新手阶段：出错就原样打印出来问 AI
            print(f"出错了：{e}")
            print("把上面这行错误复制给 AI 助手，问它怎么解决。")
            continue
        print(f"AI：{reply}")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
