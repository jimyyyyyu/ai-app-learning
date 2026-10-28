# -*- coding: utf-8 -*-
"""
文件整理工具——演示版（配合教程第 9 节）

这个文件 = organizer.py 三个 TODO 全部填好后的样子。
它的作用：把 demo_files 里乱放的文件，按类型自动装进子文件夹。

运行：python organizer演示.py
流程：
  1) 先列出"整理前"的乱摊子
  2) 逐条打印"谁搬去了哪"
  3) 列出"整理后"的样子
  4) 自动还原，方便你反复看
"""
import shutil
from pathlib import Path

TARGET = Path("demo_files")

RULES = {
    ".txt": "文档",
    ".md": "文档",
    ".docx": "文档",
    ".pdf": "文档",
    ".jpg": "图片",
    ".png": "图片",
    ".py": "代码",
    ".mp3": "音视频",
    ".mp4": "音视频",
}


def show(title):
    """列出 demo_files 的完整结构：根目录的文件夹 + 每个文件夹里的文件。"""
    print(f"\n--- {title} ---")
    print("根目录文件:", [p.name for p in TARGET.iterdir() if p.is_file()])
    for d in sorted(p for p in TARGET.iterdir() if p.is_dir()):
        print(f"  {d.name}/:", [p.name for p in d.iterdir()])


def organize(folder):
    for file in folder.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()
        subfolder = RULES.get(ext, "其他")

        dest_dir = folder / subfolder          # TODO 2 的答案：拼出目标文件夹
        dest_dir.mkdir(exist_ok=True)          # TODO 2 的答案：不存在就创建

        shutil.move(str(file), str(dest_dir / file.name))   # TODO 3 的答案：搬过去
        print(f"  {file.name}  ->  {subfolder}/")


def reset():
    """还原现场：只还原整理器自己的输出文件夹，不碰 旧文件夹。"""
    output_names = set(RULES.values()) | {"其他"}
    for sub in [p for p in TARGET.iterdir() if p.is_dir() and p.name in output_names]:
        for f in sub.iterdir():
            shutil.move(str(f), str(TARGET / f.name))
        sub.rmdir()


if __name__ == "__main__":
    reset()
    show("整理前：乱摊子")
    print("\n开始整理（每个文件搬去哪）：")
    organize(TARGET)
    show("整理后：各归各位")
    print("\ndemo_files\\文档\\ 里的内容：", [p.name for p in (TARGET / "文档").iterdir()])
    print("demo_files\\图片\\ 里的内容：", [p.name for p in (TARGET / "图片").iterdir()])
    print("demo_files\\其他\\ 里的内容：", [p.name for p in (TARGET / "其他").iterdir()])

    reset()
    print("\n（已自动还原，你的 organizer.py 练习不受影响）")
