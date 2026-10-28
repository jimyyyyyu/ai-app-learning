

import os
import requests
import json

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


def save_history(messages):
    """退出时把对话历史存进文件。"""
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def load_history():
    """启动时读回历史；没有文件就用全新人设。"""
    try:
        with open("chat_history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"role": "system", "content": "你是一个gay。"}]


def main():
    print("=" * 42)
    print("你的第一个 AI 程序：命令行聊天机器人")
    print("输入 quit 退出")
    print("=" * 42)

    # messages 是"对话历史"：发给模型的不是一句话，而是整个聊天记录
    messages = load_history()

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

    save_history(messages)   # 循环结束后统一存盘（quit/Ctrl+C 都会走到这）


if __name__ == "__main__":
    main()
