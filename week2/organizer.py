# -*- coding: utf-8 -*-
"""
第 2 周项目：文件批量整理工具

任务：把 demo_files 文件夹里乱放的文件，按扩展名自动归类到子文件夹：

    demo_files/报告.txt   -> demo_files/文档/报告.txt
    demo_files/照片1.jpg  -> demo_files/图片/照片1.jpg

运行：python organizer.py
验收：见 week2/README.md 的"项目任务书"
"""
import shutil
from pathlib import Path

# 目标文件夹（做完基础版后，挑战题会让你支持任意路径）
TARGET = Path("demo_files")

# 分类规则：扩展名 -> 子文件夹名
RULES = {
    ".txt": "文档",
    ".md": "文档",
    ".docx": "文档",
    ".pdf": "文档",
    ".jpg": "图片",
    ".png": "图片",
    ".py": "代码",
    # TODO 1：再加两类规则，比如 .mp3 / .mp4 -> "音视频"
}


def organize(folder: Path) -> None:
    """把 folder 里的文件按扩展名归类到子文件夹。"""
    for file in folder.iterdir():
        if not file.is_file():
            continue  # 跳过文件夹

        ext = file.suffix.lower()              # 扩展名，如 ".txt"
        subfolder = RULES.get(ext, "其他")      # 没规则的进"其他"

        # TODO 2：如果子文件夹不存在，先创建
        #   提示：dest_dir = folder / subfolder
        #        dest_dir.mkdir(exist_ok=True)

        # TODO 3：把文件移动过去
        #   提示：shutil.move(str(file), str(dest_dir / file.name))

        print(f"{file.name} -> {subfolder}/")


def reset_demo() -> None:
    """把 demo_files 还原成乱放的状态，方便反复测试。

    只还原"整理器自己的输出文件夹"（RULES 里的分类 + 其他），
    绝不碰用户自己的文件夹（比如 旧文件夹）——这是验收标准要求的。

    读一遍这个函数，弄懂它在干什么（这是加分项）。
    """
    output_names = set(RULES.values()) | {"其他"}
    for sub in [p for p in TARGET.iterdir() if p.is_dir() and p.name in output_names]:
        for f in sub.iterdir():
            shutil.move(str(f), str(TARGET / f.name))
        sub.rmdir()


if __name__ == "__main__":
    reset_demo()     # 先还原现场，让每次测试结果一致
    organize(TARGET)
    print("完成！去 demo_files 文件夹看看效果")
