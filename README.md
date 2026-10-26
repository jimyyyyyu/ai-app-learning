# 第 1 周实战：环境搭建 + 第一个 AI 程序

> 本周目标：装好环境、拿到 API Key、跑通两个脚本、完成语法查漏。

## 一、本周任务清单

- [ ] 检查/安装 Python 3.10+、git、VS Code
- [ ] 安装 requests 库
- [ ] 注册 DeepSeek 开放平台，创建 API Key
- [ ] 跑通 `free_api_demo.py`（免费天气 API，无需 key）
- [ ] 跑通 `hello_ai.py`（你的第一个大模型程序）
- [ ] 完成语法查漏自测（见第三节）
- [ ] 把本周成果推到 GitHub（第 1 周里程碑）

## 二、详细步骤

### 1. 检查环境（PowerShell 里运行）

```powershell
python --version
git --version
code --version
```

- Python 没装 → python.org 下载 3.11 或 3.12，**安装时勾选 "Add Python to PATH"**
- git 没装 → git-scm.com 下载安装
- VS Code 没装 → code.visualstudio.com 下载安装

### 2. 安装 requests 库

```powershell
python -m pip install requests
```

### 3. 注册 DeepSeek 并创建 API Key

1. 打开 https://platform.deepseek.com
2. 注册登录 → 左侧「API Keys」→「创建 API Key」，复制保存（**只显示一次**）
3. 充值 10 元（练一个月绰绰有余）

### 4. 设置环境变量（把 key 给脚本，但不写死在代码里）

临时设置（当前 PowerShell 窗口有效）：

```powershell
$env:DEEPSEEK_API_KEY = "sk-你的key"
```

永久设置（新开窗口也有效）：

```powershell
setx DEEPSEEK_API_KEY "sk-你的key"
```

### 5. 运行脚本

```powershell
python free_api_demo.py   # 免费天气接口练习，不需要 key
python hello_ai.py        # 大模型聊天机器人
```

> 如果中文显示乱码：在终端里先执行 `chcp 65001` 再运行；若是把输出重定向到文件/管道，可先执行 `$env:PYTHONIOENCODING="utf-8"`。

### 6. git 与 GitHub（第 1 周里程碑）

```powershell
git init
git add .
git commit -m "week1: 第一个 AI 程序"
git branch -M main
git remote add origin https://github.com/你的用户名/ai-app-learning.git
git push -u origin main
```

## 三、语法查漏自测（你有脚本基础，重点补这些）

1. 字典和列表的常用操作：取值、遍历、增删
2. 函数：定义、参数、返回值
3. 异常处理：`try/except` 什么时候用
4. JSON：`json.loads` / `json.dumps` 是什么
5. f-string 格式化字符串
6. `import` 与模块

## 四、卡住了怎么办

1. 把报错信息**原样复制**
2. 贴给 AI 助手："我在运行 xxx 时遇到这个错误：\<报错\>，我的环境是 Windows，请帮我分析"
3. 先自己读报错**最后一行**——80% 的问题出在那

## 五、本周要理解的核心概念

- **HTTP 请求**：你发一个"请求"（URL + 参数 + 密钥），服务器回一个"响应"（JSON）
- **API Key**：相当于你的账号密码，绝不能写进代码上传到 GitHub（`.gitignore` 已帮你忽略 `.env`）
- **大模型 API 的本质**：就是一次普通的 HTTP 请求，返回一段文字
