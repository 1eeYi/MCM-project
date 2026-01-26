
# MCM 项目 GitHub 协作教材（队友版）

这是一份面向美赛 4 人协作的“专门教材”，请大家花 5 分钟仔细阅读并配置环境。

**仓库地址（统一用这个）：**

* **HTTPS**：`https://github.com/kunnyd955-web/MCM-project.git`
* **SSH**（推荐）：`git@github.com:kunnyd955-web/MCM-project.git`

---

## 一、协作原则（务必遵守）

1. **不要直接改 main 分支**：`main` 只放“能跑的版本”。
2. **每个人只在自己的分支开发**：分支命名规范为 `feature/<你的名字>`。
3. **每次提交要小步快跑**：一次提交只做一件事。
4. **合并必须走 PR (Pull Request)**：至少 1 人看过再合并。
5. **不要把大数据/结果文件推到 Git**：`data/`, `results/`, `logs/` 都不提交。

---

## 二、一次性准备：Git + GitHub 登录方式（强烈建议 SSH）

### 2.1 安装 Git

* **Windows**：安装 [Git for Windows](https://git-scm.com/download/win)
* **macOS**：终端输入 `git --version`，没有就安装 Xcode Command Line Tools。
* **Linux**：`sudo apt install git -y`

**验证安装：**

```bash
git --version

```

### 2.2 配置用户名邮箱（只做一次）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

```

### 2.3 配置 GitHub SSH（推荐：免密码、稳定）

**第一步：生成 Key**

```bash
ssh-keygen -t ed25519 -C "你的邮箱"
# 一路回车即可

```

**第二步：复制公钥**

* macOS / Linux：
```bash
cat ~/.ssh/id_ed25519.pub

```


* Windows（Git Bash）：
```bash
cat ~/.ssh/id_ed25519.pub

```



**第三步：把公钥添加到 GitHub**
GitHub 网页右上角头像 → **Settings** → **SSH and GPG keys** → **New SSH key** → 粘贴保存。

**验证连接：**

```bash
ssh -T git@github.com
# 出现 "Hi <username>! You've successfully authenticated..." 即成功

```

---

## 三、首次克隆仓库（每个人都要做）

**推荐用 SSH：**

```bash
git clone git@github.com:kunnyd955-web/MCM-project.git
cd MCM-project

```

**如果你只能用 HTTPS：**

```bash
git clone https://github.com/kunnyd955-web/MCM-project.git
cd MCM-project

```

---

## 四、创建你的个人分支（只做一次）

把 `<name>` 替换成你自己的英文名或拼音，例如 `alice`：

```bash
git checkout -b feature/<name>
git push -u origin feature/<name>

```

**检查当前分支：**

```bash
git branch
# 带 * 的就是你当前分支

```

---

## 五、每天/每次写代码的标准流程（照抄即可）

### 5.1 开始写之前：同步 main 并合到你的分支

**（防止冲突的关键步骤）**

```bash
git checkout main
git pull
git checkout feature/<name>
git merge main

```

### 5.2 写完一小段：提交并推送

```bash
git status
git add .
git commit -m "一句话说明你做了什么"
git push

```

### 5.3 发 PR 合并到 main（网页操作）

1. 打开 GitHub 仓库 → **Pull requests** → **New pull request**
2. **Base** 选 `main`，**Compare** 选 `feature/<name>`
3. **写清楚：**
* 做了什么
* 怎么验证（跑哪个脚本、预期输出）


4. **合并：** 由队长（Kunny）或指定负责人执行。

---

## 六、冲突怎么处理（最常见的坑）

如果你在 `git merge main` 时出现冲突：

1. **先看哪些文件冲突：**
```bash
git status

```


2. **打开冲突文件**，你会看到类似标记：
```text
<<<<<<< HEAD
你的改动
=======
main 的改动
>>>>>>> main

```


3. **手动修改**：保留正确版本，**删掉**这些 `<<<`, `===`, `>>>` 标记。
4. **提交解决后的版本**：
```bash
git add <冲突文件>
git commit -m "Resolve merge conflict"
git push

```



> ⚠️ **警告**：如果你不确定怎么保留，立刻把冲突文件发群里，不要乱合。

---

## 七、不要提交这些内容（必须遵守）

以下目录/文件不允许推上去（避免仓库爆炸）：

* `data/` (原始数据)
* `results/` (跑出来的结果)
* `logs/` (日志)
* 大文件：`*.zip`, `*.pt`, `*.pth`

**如果不小心 `add` 了但还没 `commit`：**

```bash
git restore --staged <文件名>

```

---

## 八、用 PyCharm 开发（GUI 操作指引）

1. **打开项目**：PyCharm → Open → 选择 `MCM-project` 文件夹。
2. **关联 Git**：右下角看到 Git 分支信息即可。
3. **切换/创建分支**：右下角分支名 → **New Branch** → 输入 `feature/<name>`。
4. **拉取 main 更新**：顶部菜单 **Git** → **Pull...**
5. **把 main 合并到你的分支**：
* 先切到你的分支（右下角选 `feature/<name>`）
* **Git** → **Merge Changes...**
* 选择 `main` → **Merge**


6. **提交与推送**：
* **Git** → **Commit...** → 写 message → Commit
* **Git** → **Push...**


7. **发 PR**：建议直接去 GitHub 网页发，最稳定。

---

## 九、用 VS Code 开发（GUI 操作指引）

1. **打开项目**：VS Code → File → Open Folder → 选择 `MCM-project`。
2. **安装插件**：推荐 GitLens, Python (Microsoft)。
3. **创建/切换分支**：左下角显示分支名 → 点击 → **Create new branch** → `feature/<name>`。
4. **同步 main (Pull)**：Source Control（左侧分支图标）→ 右上角 `...` → **Pull**。
5. **合并 main 到你的分支**（建议终端）：
```bash
git checkout feature/<name>
git merge main

```


6. **提交与推送**：
* Source Control 面板：Staged Changes 点 `+` 暂存
* 输入 message → 点 **Commit**
* 点 **Sync / Push**


7. **发 PR**：建议使用 GitHub 网页。

---

## 十、云端怎么配合（队友只需知道规则）

云端服务器只做两件事：

1. `git pull` 拉取 main 分支代码
2. 跑代码出结果

**禁止**队友在云端直接改代码。如果必须改，也要提交回仓库并走 PR 流程（一般不建议）。

---

## 十一、快速自查清单（每次提交前看一眼）

* [ ] 我现在在 `feature/<name>` 分支吗？
* [ ] 我 pull 过 main 并 merge 过 main 吗？
* [ ] 我提交的都是代码，**不包含** data/results/logs 吗？
* [ ] commit message 是否能让别人看懂？

---

## 十二、紧急救援

如果你卡住了，在项目目录执行这三条命令，把输出截图发群里：

```bash
git status
git branch
git log --oneline -5

```