import os
import json
import requests                             

API_KEY = os.environ.get("DEEPSEEK_API_KEY")
URL = "https://api.deepseek.com/chat/completions"

if not API_KEY:
    print("未找到 API Key！请先设置环境变量：")
    print('    $env:DEEPSEEK_API_KEY = "sk-你的key"')
    raise SystemExit(1)


def chat(messages):                          # 原样不动
    """把对话历史发给大模型，返回模型的回复。"""
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.7,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    resp = requests.post(URL, json=payload, headers=headers, timeout=60)
    resp.raise_for_status()
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
        return [{"role": "system", "content": "你是一个耐心友好的中文学习助手。"}]


def main():
    print("=" * 42)
    print("你的第一个 AI 程序：命令行聊天机器人")
    print("输入 quit 退出")
    print("=" * 42)

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
        except Exception as e:
            print(f"出错了：{e}")
            print("把上面这行错误复制给 AI 助手，问它怎么解决。")
            continue
        print(f"AI：{reply}")
        messages.append({"role": "assistant", "content": reply})

    save_history(messages)                 


if __name__ == "__main__":
    main()