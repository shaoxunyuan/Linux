# Linux基础及应用教程-实验-文本查看

## 一、实验目标

1. 掌握 `cat`、`more`、`less`、`head`、`tail` 等 Linux 文本查看命令的基本使用方法。
2. 理解不同文本查看命令的适用场景与区别。
3. 能够熟练查看、分页阅读、截取文件内容，并比较不同命令的输出效果。

---

## 二、实验环境

1. **硬件**：机房 PC（已启用虚拟化功能）。  
2. **软件**：VMware Workstation + CentOS 系统（预装登录账号密码见桌面 “关于密码.txt”）。

---

## 三、实验内容与步骤

### 文件准备（按路径与文件名执行）

> **执行路径要求**：在当前用户家目录下执行：
> 
> ```bash
> cd ~
> pwd
> ```
> 
> 输出应形如 `/home/student`。

#### 1️⃣ 创建实验目录

```bash
mkdir -p ~/text_lab
cd ~/text_lab
pwd
```

#### 2️⃣ 生成带有“文本+数字”的示例文件（可直接复制命令）

```bash
for i in $(seq 1 100); do echo "第${i}行：这是一个用于文本查看实验的示例内容。" >> mixed_text.txt; done
ls -lh mixed_text.txt
head -n 3 mixed_text.txt
tail -n 3 mixed_text.txt
```

#### 3️⃣ 复制系统示例文件

```bash
cp /etc/passwd ./passwd
ls -lh passwd
head -n 3 passwd
```

#### 4️⃣ 创建长文本文件（可直接复制命令）

```bash
for i in $(seq 1 500); do echo "日志记录第 ${i} 条：用于分页浏览与搜索的长文本样例。" >> long_text.txt; done
wc -l long_text.txt
```

#### 5️⃣ 创建动态文件用于 `tail -f`（可直接复制命令）

```bash
count=0; while true; do if (( count % 5 == 0 )); then echo "【10秒提醒】当前时间：$(date)" >> app.log; else echo "启动应用：$(date)" >> app.log; fi; ((count++)); sleep 2; done &
```

---

### 任务1. 使用 cat 查看完整文件内容

1. 查看 `mixed_text.txt` 文件内容：  
   
   ```bash
   cat ~/text_lab/mixed_text.txt
   ```
   
   显示整个文件内容，适用于内容较短的文本。

2. 同时显示行号：  
   
   ```bash
   cat -n ~/text_lab/mixed_text.txt
   ```

3. 查看系统文件 `/etc/passwd`：  
   
   ```bash
   cat ~/text_lab/passwd
   ```

---

### 任务2. 使用 more 分页查看文件

1. 分页查看 `long_text.txt` 文件：  
   
   ```bash
   more ~/text_lab/long_text.txt
   ```
   
   - 按 **空格键** 翻页。  
   - 按 **Enter** 下移一行。  
   - 按 **q** 退出分页查看。

2. 也可以查看 `/etc/passwd`：  
   
   ```bash
   more ~/text_lab/passwd
   ```

---

### 任务3. 使用 less 灵活查看文件

1. 查看 `mixed_text.txt` 文件：  
   
   ```bash
   less ~/text_lab/mixed_text.txt
   ```

2. 可使用以下快捷键操作：  
   
   - **↑ / ↓**：逐行滚动  
   - **PageUp / PageDown**：分页滚动  
   - **/关键字**：搜索，如 `/第50行`  
   - **n**：下一个匹配，**N**：上一个匹配  
   - **q**：退出

3. 查看长文件体验滚动与搜索：  
   
   ```bash
   less ~/text_lab/long_text.txt
   ```

---

### 任务4. 使用 head 查看文件前几行

1. 默认显示前 10 行：  
   
   ```bash
   head ~/text_lab/mixed_text.txt
   ```

2. 指定显示前 5 行：  
   
   ```bash
   head -n 5 ~/text_lab/mixed_text.txt
   ```

3. 查看系统文件前 3 行：  
   
   ```bash
   head -n 3 ~/text_lab/passwd
   ```

---

### 任务5. 使用 tail 查看文件末尾内容

1. 默认显示末尾 10 行：  
   
   ```bash
   tail ~/text_lab/mixed_text.txt
   ```

2. 指定显示末尾 5 行：  
   
   ```bash
   tail -n 5 ~/text_lab/mixed_text.txt
   ```

3. 查看系统文件末尾内容：  
   
   ```bash
   tail -n 5 ~/text_lab/passwd
   ```

4. 结合 `-f` 参数实时监控文件变化（需找到生成的app.log）：  
   
   ```bash
   tail -f ~/text_lab/app.log
   ```

---

### 任务6. 对比与综合操作练习

1. 比较 `head` 与 `tail` 输出：  
   
   ```bash
   head -n 3 ~/text_lab/mixed_text.txt
   tail -n 3 ~/text_lab/mixed_text.txt
   ```

2. 管道结合 `cat` 与 `head` 使用：  
   
   ```bash
   cat ~/text_lab/mixed_text.txt | head -n 10
   ```

3. 管道结合 `cat` 与 `tail` 使用：  
   
   ```bash
   cat ~/text_lab/mixed_text.txt | tail -n 5
   ```

4. 用 `less` 查看命令输出结果：  
   
   ```bash
   cat ~/text_lab/mixed_text.txt | less
   ```

---

## 四、实验报告要求

1. 提供 `cat` 命令查看 `mixed_text.txt` 的截图，并说明何时使用 `cat` 最合适。  
2. 展示 `more` 翻页查看 `long_text.txt` 的截图，描述翻页与退出按键。  
3. 提供 `less` 搜索 `/第50行` 的截图，解释 `n/N` 的意义。  
4. 对比 `more` 与 `less` 的操作体验与功能差异。  
5. 提供 `head` 查看前 10 行与前 5 行的输出截图。  
6. 提供 `tail` 查看末尾 10 行与 5 行的截图。  
7. 解释 `head` 与 `tail` 的默认输出行数及常用参数。  
8. 展示 `tail -f` 监控 `app.log` 的截图或说明应用场景。  
9. 思考：当文件很大（上百 MB）时，为何不推荐直接 `cat`？请给出原因与替代方案。  
10. 总结五个命令的区别与最佳使用场景。

---

✅ **提示**：  

- `cat`：快速输出小文件内容。  
- `more`、`less`：分页浏览大文件。  
- `head`、`tail`：截取文件部分内容。  
- `tail -f`：实时日志监控。  
- 管道操作（`|`）可组合命令提升灵活性。
