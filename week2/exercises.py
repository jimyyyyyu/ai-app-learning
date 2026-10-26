# -*- coding: utf-8 -*-
"""
第 2 周练习题：列表 / 字典 / 函数 / 异常 / JSON

运行：python exercises.py
目标：每道题都打 ✅
规则：标了 TODO 的行现在是"故意写错"的，改成正确答案再运行。
      全部 ✅ 后，就可以去做 organizer.py 项目了。
"""
import json


def check(name, got, expected):
    if got == expected:
        print(f"✅ {name}")
    else:
        print(f"❌ {name}")
        print(f"   期望 {expected!r}，你得到 {got!r}")


print("=" * 40)
print("一、列表")
print("=" * 40)

# 1. 列表推导式：1 到 10 的平方（示例，已经写好了）
squares = [i * i for i in range(1, 11)]
check("1. 列表推导式", squares, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

# 2. 索引：取第 3 个元素（提示：下标从 0 开始）
third = squares[0]   # TODO：把 0 改成正确答案
check("2. 索引取值", third, 9)

# 3. 切片：取最后 3 个元素（示例）
last3 = squares[-3:]
check("3. 切片", last3, [64, 81, 100])

# 4. 方法：给 nums 加一个 0，再排好序
nums = [3, 1, 2]
nums.append(0)   # TODO：这行是对的，照抄一遍加深记忆
# nums.sort()    # TODO：取消这行的注释
check("4. append / sort", nums, [0, 1, 2, 3])

print()
print("=" * 40)
print("二、字典")
print("=" * 40)

student = {"name": "小明", "age": 20, "city": "北京"}

# 5. 取值（示例）
name = student["name"]
check("5. 取值", name, "小明")

# 6. 安全的取值：键不存在时返回默认值（示例）
score = student.get("score", 0)
check("6. get 默认值", score, 0)

# 7. 遍历所有键值对（示例）
pairs = [(k, v) for k, v in student.items()]
check("7. items 遍历", pairs, [("name", "小明"), ("age", 20), ("city", "北京")])

# 8. 词频统计：统计句子中每个词出现几次
sentence = "the cat and the dog and the bird"
freq = {}
for word in sentence.split():
    freq[word] = 0   # TODO：改成"在原来的次数上 +1"（提示：freq.get(word, 0) + 1）
check("8. 词频统计", freq, {"the": 3, "cat": 1, "and": 2, "dog": 1, "bird": 1})

print()
print("=" * 40)
print("三、函数")
print("=" * 40)

# 9. 定义函数：两数相加
def add(a, b):
    return 0   # TODO：改成 a + b

check("9. 函数定义", add(3, 4), 7)

# 10. 默认参数 + f-string
def greet(name, greeting="你好"):
    return name   # TODO：改成 f"{greeting}，{name}"

check("10. 默认参数", greet("小明") + "|" + greet("小明", "早上好"),
      "你好，小明|早上好，小明")

print()
print("=" * 40)
print("四、异常处理")
print("=" * 40)

# 11. try/except：字典里没有的键，用 try 兜住
def safe_lookup(d, key):
    try:
        return d[key]
    except KeyError:
        return d.get(key)   # TODO：改成返回 "没有这个键"

check("11. try/except", safe_lookup({"a": 1}, "b"), "没有这个键")

# 12. 主动抛出异常
def divide(a, b):
    if b == 0:
        # raise ValueError("除数不能为 0")   # TODO：取消注释
        pass
    return a / b

try:
    divide(1, 0)
    check("12. raise", "没抛异常", "应该抛 ValueError")
except ValueError:
    check("12. raise", "抛出了 ValueError", "抛出了 ValueError")

print()
print("=" * 40)
print("五、JSON")
print("=" * 40)

# 13. Python 对象 -> JSON 字符串（示例）
data = {"name": "小明", "skills": ["Python", "AI"]}
text = json.dumps(data, ensure_ascii=False)
check("13. dumps", text, '{"name": "小明", "skills": ["Python", "AI"]}')

# 14. JSON 字符串 -> Python 对象（示例）
loaded = json.loads('{"age": 20}')
check("14. loads", loaded, {"age": 20})

print()
print("完成！全是 ✅ 就说明基础过关，去做 organizer.py 项目吧")
