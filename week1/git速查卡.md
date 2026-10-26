# Git 三分钟速查卡

> 把 git 想成**游戏存档系统**：commit = 存档，GitHub = 云端备份，push = 上传存档。

## 常用命令只有 5 个

| 命令 | 作用 | 人话 |
|---|---|---|
| `git status` | 查看当前状态 | 看看哪些文件改了、存没存 |
| `git add .` | 暂存所有改动 | 把要存的东西摆到存档台上 |
| `git commit -m "说明"` | 提交（存档） | 按下存档键，写一句这次改了什么 |
| `git push` | 推送到 GitHub | 把存档上传到云端 |
| `git log --oneline` | 查看提交历史 | 看看有哪些存档点 |

## 以后每天写代码的固定流程（三行）

```powershell
git add .
git commit -m "今天改了什么"
git push
```

## 常见报错速查

| 报错 | 原因 | 解决 |
|---|---|---|
| `Please tell me who you are` | 没登记身份 | `git config --global user.name "名字"` 和 `user.email "邮箱"` |
| `'git' 不是内部或外部命令` | 装了 git 但窗口是旧的 | 关掉重开 PowerShell |
| `Updates were rejected` | 云端和本地内容不一致 | 先 `git pull --rebase` 再 `git push` |
| `failed to push some refs` | 远程地址错了 | `git remote -v` 检查，`git remote set-url origin 正确地址` |

## 一句话原则

**小步快存**：每完成一个小功能就存一次档，说明写清楚"改了什么"。这样任何时候改坏了，都能回到上一个存档点。
