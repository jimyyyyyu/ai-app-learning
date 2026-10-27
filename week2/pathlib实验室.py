# -*- coding: utf-8 -*-
"""
pathlib 实验室：10 分钟看懂文件操作
运行：python pathlib实验室.py
看完输出后，自己改几个地方试试（比如换个文件夹、换个扩展名）
"""
from pathlib import Path
import shutil

print("=" * 44)
print("0. 路径是一个'对象'，不是一个字符串")
print("=" * 44)
here = Path.cwd()                       # 当前目录
print("当前目录:", here)

f = Path("demo_files") / "报告.txt"      # 用 / 拼路径（不是字符串相加！）
print("拼出来的路径:", f)
print("文件名:", f.name)                 # 最后一段
print("扩展名:", f.suffix)               # 最后一个点后面的部分
print("父文件夹:", f.parent)             # 去掉最后一段
print("存在吗:", f.exists(), "| 是文件:", f.is_file())

print()
print("=" * 44)
print("1. 创建文件：write_text（准备实验材料）")
print("=" * 44)
tf = Path("demo_files") / "实验用_报告.txt"
if not tf.exists():
    tf.write_text("这是实验用文件", encoding="utf-8")
print("实验文件已就绪:", tf)

print()
print("=" * 44)
print("2. 创建文件夹：mkdir(exist_ok=True)")
print("=" * 44)
test = here / "demo_files" / "实验文件夹"
test.mkdir(exist_ok=True)               # 已存在也不报错
print("创建了:", test)

print()
print("=" * 44)
print("3. 遍历文件夹：iterdir()")
print("=" * 44)
for item in Path("demo_files").iterdir():
    kind = "文件夹" if item.is_dir() else "文件  "
    print(f"{kind} | {item.name:<14} | 后缀: {item.suffix or '（无）'}")

print()
print("=" * 44)
print("4. 移动文件：shutil.move(从哪里, 到哪里)")
print("=" * 44)
target = test / tf.name
if not target.exists() and tf.exists():
    shutil.move(str(tf), str(target))
print("移动后，新位置存在吗:", target.exists())

print()
print("=" * 44)
print("5. 清理现场（放回原位、删除实验文件夹和文件）")
print("=" * 44)
if target.exists():
    shutil.move(str(target), str(tf))   # 挪回原位
if test.exists() and not any(test.iterdir()):
    test.rmdir()                        # 删除空文件夹
tf.unlink(missing_ok=True)              # 删除实验文件
print("实验文件已删:", not tf.exists(), "| 实验文件夹已删:", not test.exists())

print()
print("完成！organizer.py 用到的全部武器就这 5 个：")
print("  Path()拼路径 / iterdir()遍历 / suffix扩展名 / mkdir建目录 / shutil.move移动")
