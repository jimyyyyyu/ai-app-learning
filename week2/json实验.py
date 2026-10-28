# -*- coding: utf-8 -*-
"""
JSON 读写文件实验（配合教程第 6 节）

运行：python json实验.py
流程：
  1) 把 2 条对话写进 test.json
  2) 暂停，等你打开 test.json 亲眼看看（记事本或 VS Code 都行）
  3) 再读回 Python，验证结构没丢
"""
import json

# ---------- 实验 1：写文件 ----------
data = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好！有什么可以帮你？"},
]

print("实验 1：把上面 2 条对话写进 test.json ...")
with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("✅ 写完了")

input(">>> 现在打开 week2 文件夹里的 test.json 看看长什么样，看完回来按回车继续...")

# ---------- 实验 2：读文件 ----------
print("\n实验 2：把 test.json 读回 Python ...")
with open("test.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("读回来的东西:", loaded)
print("它的类型:", type(loaded))
print("第一句话是谁说的:", loaded[0]["role"], "→", loaded[0]["content"])
print()
print("结论：写出去的列表，读回来还是列表——结构一点没丢。")
print("这就是项目 A 保存聊天记录的全部原理。")
