# 第 2 周：Python 核心强化 + 文件批量整理工具

> 本周目标：把列表、字典、函数、异常、JSON 练成肌肉记忆，并做出一个真实有用的工具。

## 每日安排

| 天 | 任务 |
|---|---|
| 1–2 | 做完 `exercises.py`（五组练习，全部打 ✅ 算过关） |
| 3–4 | 精读下方"知识点速览"，不懂的查文档或问 AI |
| 5–6 | 完成项目 `organizer.py`（文件批量整理工具） |
| 7 | git 三连推送 + 写本周复盘（50 字即可） |

## 知识点速览（做题卡住时回来看）

### 一、列表 list
```python
nums = [3, 1, 2]
nums.append(0)      # 末尾加一个 -> [3, 1, 2, 0]
nums.sort()         # 原地排序   -> [0, 1, 2, 3]
nums[0]             # 取第 1 个（下标从 0 开始）
nums[-1]            # 取最后 1 个
nums[1:3]           # 切片：第 2、3 个
[x * 2 for x in nums]   # 推导式：批量加工
```

### 二、字典 dict（键值对）
```python
d = {"name": "小明", "age": 20}
d["name"]           # 取值；键不存在会报 KeyError
d.get("score", 0)   # 安全取值：不存在时给默认值
d["city"] = "北京"   # 新增/修改
for k, v in d.items():   # 遍历
d.setdefault("count", 0) # 有就用，没有就创建
```

### 三、函数
```python
def add(a, b, scale=1):        # scale 是默认参数
    """两数相加并缩放。"""
    return (a + b) * scale

add(3, 4)          # 7
add(3, 4, scale=2) # 14，关键字参数
```
> 好习惯：函数名用动词；写 docstring（三引号说明）；一个函数只做一件事。

### 四、异常处理
```python
try:
    result = d["missing_key"]   # 可能出错的操作
except KeyError:
    result = "没有这个键"        # 出错时的兜底
finally:
    pass                        # 无论成败都执行（可选）
```
> 原则：**能预见的错误用 try 兜住，而不是让程序崩溃**。

### 五、JSON（数据交换的通用格式）
```python
import json
text = json.dumps({"a": 1}, ensure_ascii=False)  # Python -> 字符串
data = json.loads('{"a": 1}')                    # 字符串 -> Python
```
> 大模型 API 返回的就是 JSON——第 3 周天天见。

### 六、文件操作 pathlib（本周项目的主角）
```python
from pathlib import Path
p = Path("demo_files")          # 文件夹
p.mkdir(exist_ok=True)          # 创建（已存在不报错）
p.iterdir()                     # 遍历里面的所有东西
f = p / "a.txt"                 # 拼接路径
f.suffix                        # ".txt"
f.name                          # "a.txt"
f.is_file()                     # 是不是文件
f.is_dir()                      # 是不是文件夹
f.stat().st_mtime               # 最后修改时间戳
```

## 项目任务书：organizer.py

**需求**：把 `demo_files` 里乱放的文件按扩展名自动归类到子文件夹：

```
demo_files/报告.txt   -> demo_files/文档/报告.txt
demo_files/照片1.jpg  -> demo_files/图片/照片1.jpg
```

**验收标准**：
1. 运行 `python organizer.py` 后，demo_files 里的文件各归各位
2. 没匹配到规则的文件进"其他"文件夹
3. 文件夹（如"旧文件夹"）保持不动
4. 重复运行不报错（先自动还原现场）

**扩展挑战（做完了再挑）**：
- 按"最后修改年份"归档（提示：`f.stat().st_mtime` + `datetime.fromtimestamp`）
- 支持命令行指定文件夹：`python organizer.py 任意路径`（提示：`sys.argv`）
- 移动时遇到重名文件自动加序号（`报告.txt`、`报告_1.txt`）
- 整理完输出一份 `整理报告.json`（提示：把统计结果 `json.dump` 到文件）

## 本周复盘问题（第 7 天回答）

1. `Path.iterdir()` 和列表推导式结合能做什么？
2. 为什么用 `.suffix.lower()` 而不是 `.suffix`？
3. 如果 demo_files 里出现一个 `.TXT` 文件（大写），你的程序会怎么处理？

## 卡住了怎么办

1. 先看报错最后一行
2. 把报错 + 相关代码一起贴给 AI 助手问
3. 别死磕超过 30 分钟——问人/问 AI 也是能力
