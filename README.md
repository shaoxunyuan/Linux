南京中医药大学 人工智能与信息技术学院

# Linux <img src="figures/linux.logo.png" alt="图标" style="width:30px;" />

## 目录  

1. [Linux的介绍和安装](#Linux的介绍和安装)
2. [Linux目录结构](#Linux目录结构)  
3. [Linux常用命令](#Linux常用命令)  
4. [Shell编程](#Shell编程)
5. [正则表达式](#正则表达式)
6. [Linux网络安全](#Linux网络安全)


## Linux的介绍和安装

&nbsp;&nbsp;&nbsp;&nbsp;Linux由林纳斯·托瓦兹于1991年开发，旨在创建一个开放源代码的操作系统。

&nbsp;&nbsp;&nbsp;&nbsp;从最初的单用户系统发展为支持多种硬件架构的强大平台，广泛应用于服务器、桌面和嵌入式设备。  

### 开源软件和GNU协议的定义和意义

&nbsp;&nbsp;&nbsp;&nbsp;开源软件是指源代码公开，允许用户自由使用、修改和分发的软件。

&nbsp;&nbsp;&nbsp;&nbsp;这种软件通常通过社区参与不断改进，促进了技术的创新与共享。  

&nbsp;&nbsp;&nbsp;&nbsp;GNU（GNU's Not Unix!）是一个自由软件项目，旨在创建一个完全自由的操作系统。

&nbsp;&nbsp;&nbsp;&nbsp;GNU项目由理查德·斯托曼（Richard Stallman）于1983年发起。与GNU相关的最重要的许可证是GNU通用公共许可证（GPL）。

### Linux的开发模式

&nbsp;&nbsp;&nbsp;&nbsp;**开源（Open Source）**：Linux内核及其大部分组件的源代码都是开放的，任何人都可以查看、修改和分发。开源理念鼓励社区的参与和创新。

&nbsp;&nbsp;&nbsp;&nbsp;**社区驱动（Community-Driven）**：Linux的开发和维护依赖于一个全球范围的开发者社区。这个社区包括个人开发者、企业贡献者和各种组织，大家通过邮件列表、论坛和其他协作平台共同合作。

&nbsp;&nbsp;&nbsp;&nbsp;**模块化（Modularity）**：Linux系统采用模块化设计，内核由多个模块组成，这使得功能可以以模块的形式加载和卸载，便于管理和优化系统性能。

&nbsp;&nbsp;&nbsp;&nbsp;**版本控制（Version Control）**：Linux的开发通常使用Git等版本控制系统，这使得多个人可以在同一项目上进行协作，便于管理代码的变化和更新。

&nbsp;&nbsp;&nbsp;&nbsp;**持续集成和持续发布（CI/CD）**：Linux的发展采用了持续集成和持续发布的模式，各个版本不断更新，以增强功能、修复漏洞和提高性能。

&nbsp;&nbsp;&nbsp;&nbsp;**遵循标准（Standards Compliance）**：Linux遵循POSIX等标准，确保兼容性和可移植性，使得Linux应用程序能够在不同的系统上运行。


### Linux的内核版和发行版

&nbsp;&nbsp;&nbsp;&nbsp;**内核版**  

&nbsp;&nbsp;&nbsp;&nbsp;Linux内核是操作系统的核心，版本以“X.Y.Z”格式命名。各个版本不断更新，以增强功能和安全性。  

&nbsp;&nbsp;&nbsp;&nbsp;Linux内核由芬兰计算机科学家林纳斯·托瓦兹（Linus Torvalds）于1991年首次发布。最初版本为0.01，作为替代Minix操作系统的个人项目。

&nbsp;&nbsp;&nbsp;&nbsp;**发行版**  

&nbsp;&nbsp;&nbsp;&nbsp;发行版包括内核及其相关软件，常见版本有：  

&nbsp;&nbsp;&nbsp;&nbsp;**Ubuntu**：友好，适合初学者。  

&nbsp;&nbsp;&nbsp;&nbsp;**Fedora**：追求最新技术，适合开发者。  

&nbsp;&nbsp;&nbsp;&nbsp;**Debian**：稳定，适合生产环境。  

&nbsp;&nbsp;&nbsp;&nbsp;**Arch Linux**：高度自定义，适合高级用户。  

&nbsp;&nbsp;&nbsp;&nbsp;`lsb_release -a` 是一个在 Linux 系统中用于显示 Linux 发行版信息的命令。

&nbsp;&nbsp;&nbsp;&nbsp;运行 `lsb_release -a` 命令后，将输出以下信息：

&nbsp;&nbsp;&nbsp;&nbsp;**Distributor ID**: 显示发行版的名称，例如 Ubuntu、Debian、CentOS 等。

&nbsp;&nbsp;&nbsp;&nbsp;**Description**: 显示详细的发行版描述信息，通常包括版本号和发行版名称。

&nbsp;&nbsp;&nbsp;&nbsp;**Release**: 显示具体的版本号，例如 20.04、7.9 等。

&nbsp;&nbsp;&nbsp;&nbsp;**Codename**: 显示发行版的代号，例如 Ubuntu 的 LTS 版本可能是 "Focal Fossa" (20.04) 或 "Bionic Beaver" (18.04)。


### Linux的安装步骤

1. 选择合适的发行版并下载ISO文件。  
2. 下载合适的虚拟机软件。  
3. 创建新的虚拟机并加载ISO文件。  
4. 按照安装向导完成安装过程。 

## Linux目录结构

<div style="display: flex; justify-content: center;">  
  
  <img src="figures/LinuxContent.jpg" alt="图片" style="width: 800px;" />  
  
</div>  

https://www.runoob.com/linux/linux-system-contents.html 

## Shell编程

## Linux常用命令

<div style="display: flex; justify-content: center;">  

  <img src="figures/command.png" alt="图片" style="width: 800px;" />  

</div>  

<div style="display: flex; justify-content: center;">  
  
  <img src="figures/LinuxCommand.png" alt="图片" style="width: 800px;" />  
  
</div>  


## Shell编程

1. **Shell 变量**  
   Shell变量用于存储信息，便于在脚本中重复使用。  

2. **Shell 传递参数**  
   可以通过位置参数（如 `$1`、`$2`）在脚本中接收外部传递的参数。  

3. **Shell 数组**  
   Shell支持一维数组，允许存储多个值，以便于批量处理和数据管理。  

4. **Shell 运算符**  
   Shell提供多种运算符，如算术运算符、比较运算符和逻辑运算符，用于进行各种计算和判断。  

5. **Shell echo命令**  
   `echo`命令用于在终端输出文本或变量内容，常用于调试和信息显示。  

6. **Shell printf命令**  
   `printf`命令提供格式化输出功能，可以控制文本的显示格式，适用于需要精确格式的输出。  

7. **Shell test 命令**  
   `test`命令用于条件判断，评估表达式的真或假，通常与if语句结合使用。  

8. **Shell 流程控制**  
   流程控制结构（如if、for、while）用于控制脚本执行的流程，以实现不同的逻辑分支。  

9. **Shell 函数**  
   函数是可以重复调用的代码块，有助于提高代码的重用性和模块化。  

10. **Shell 输入/输出重定向**  
    输入/输出重定向允许将命令的输入和输出重定向到文件或其他命令，实现更灵活的数据管理。
    
## 正则表达式

正则表达式（Regular Expression）是一种用于匹配字符串的模式，广泛应用于文本处理和数据验证。在Linux中，正则表达式常用于工具如 `grep`、`sed`、`awk`等。  

### 基本语法  

1. **字符匹配**  
   - `.`: 匹配任意单个字符。  
   - `[]`: 匹配括号内的任意单个字符，例如 `[abc]` 匹配 `a`、`b` 或 `c`。  

2. **特殊字符**  
   - `\`: 转义字符，用于匹配特殊字符本身，例如 `\$` 匹配 `$` 字符。  
   - `^`: 匹配行的开始。  
   - `$`: 匹配行的结束。  

3. **数量词**  
   - `*`: 匹配前一个字符零次或多次。  
   - `+`: 匹配前一个字符一次或多次。  
   - `?`: 匹配前一个字符零次或一次。  
   - `{n}`: 精确匹配前一个字符 n 次。  
   - `{n,}`: 匹配前一个字符 n 次或多次。  
   - `{n,m}`: 匹配前一个字符至少 n 次，但不超过 m 次。  

4. **逻辑操作**  
   - `|`: 用于表示“或”逻辑，例如 `a|b` 匹配 `a` 或 `b`。  

### 常用命令  

- **grep**  
  在文件中搜索匹配正则表达式的行：  
  ```bash  
  grep '正则表达式' 文件名

# Linux网络安全

## Linux 网络安全

Linux 系统作为服务器领域的主流操作系统，其网络安全防护需从基础配置、访问控制、协议优化等多层面构建防线。以下从密码策略、防火墙、安全协议与服务三个核心模块，详细说明配置方案与实践要点。

### 密码策略强化

密码作为系统访问的第一道防线，其复杂度与时效性直接影响系统安全。通过配置系统参数，可强制用户使用高安全性密码，并定期更新。

#### 设置复杂密码策略：

通过修改系统配置文件与安装密码复杂度检查工具，强制用户密码满足 “大小写字母 + 数字 + 特殊字符” 的组合要求，同时限制弱密码使用。



1. **修改**`/etc/login.defs`**基础配置**
   该文件控制系统登录相关的基础参数，可设置密码最小长度、密码过期警告时间等：
   
   

```
sudo vim /etc/login.defs
```

关键配置参数修改如下：



* `PASS_MIN_LEN 8`：设置密码最小长度为 8 位（建议生产环境设为 12 位以上）；

* `PASS_WARN_AGE 7`：密码过期前 7 天向用户发送警告；

* `PASS_MAX_DAYS 90`：密码最长有效天数（与后续`/etc/shadow`配置联动）。
1. **安装**`pam_cracklib`**强化复杂度检查**
   仅通过`login.defs`无法实现字符类型限制，需借助 PAM（可插拔认证模块）的`pam_cracklib.so`组件：
   
   

```
\# 安装依赖（部分系统默认已安装）

sudo yum install cracklib cracklib-devel  # CentOS/RHEL

sudo apt install libpam-cracklib          # Ubuntu/Debian
```

修改 PAM 密码配置文件`/etc/pam.d/system-auth`（CentOS）或`/etc/pam.d/common-password`（Ubuntu），在`password required ``pam_cracklib.so`行后添加参数：



```
password required pam\_cracklib.so minlen=12 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1 reject\_username
```

参数说明：



* `minlen=12`：密码最小长度 12 位（实际长度 = 最小长度 - 字符类型奖励，需确保实际长度达标）；

* `ucredit=-1`：至少包含 1 个大写字母（`-1`表示 “至少 1 个”，`+1`表示 “最多 1 个”）；

* `lcredit=-1`：至少包含 1 个小写字母；

* `dcredit=-1`：至少包含 1 个数字；

* `ocredit=-1`：至少包含 1 个特殊字符（如！@#\$%^&\*）；

* `reject_username`：禁止密码包含用户名（如用户`root`不能使用`root@123`这类密码）。
1. **禁止使用弱密码字典**
   结合`pam_pwcheck`或`fail2ban`，可导入弱密码字典（如`/usr/share/dict/weakpass`），拒绝用户设置常见弱密码（如`123456`、`password`等）。

#### 密码过期策略：

通过`/etc/shadow`文件与`chage`命令，配置密码过期时间、历史密码禁止复用等规则，防止密码长期未更新导致泄露风险。



1. `/etc/shadow`**文件字段说明**
   该文件存储用户密码哈希与密码策略信息，每行格式如下（以`root`用户为例）：
   
   

```
root:\$6\$xxxxxxxx\$xxxxxxxx:19500:7:90:15:99999:
```

关键字段（从左数第 3-7 位）：



* 第 3 位：上次修改密码的时间（从 1970-01-01 起的天数）；

* 第 4 位：密码修改后至少等待多少天才能再次修改（`7`表示 7 天内不可改）；

* 第 5 位：密码最长有效天数（`90`表示 90 天后过期）；

* 第 6 位：密码过期前警告天数（`15`表示提前 15 天警告）；

* 第 7 位：密码过期后宽限天数（超过过期时间后，用户仍可登录修改密码的天数）。
1. **使用**`chage`**命令批量配置**
   无需手动编辑`/etc/shadow`，可通过`chage`命令快速配置用户密码策略：
   
   

```
\# 配置用户boyi的密码策略

sudo chage -m 7 -M 90 -W 15 -I 7 boyi
```

参数说明：



* `-m 7`：密码最小修改间隔 7 天；

* `-M 90`：密码最长有效 90 天；

* `-W 15`：过期前 15 天警告；

* `-I 7`：密码过期后 7 天内仍可登录修改（超过 7 天账号锁定）。
1. **检查密码策略生效状态**
   执行以下命令查看用户当前密码策略：
   
   

```
sudo chage -l boyi
```

### 安装和配置防火墙

Linux 防火墙是网络访问控制的核心，通过过滤进出网络接口的数据包，限制非法 IP、端口的访问。主流防火墙工具为`iptables`（传统工具）与`firewalld`（CentOS7 + 默认，动态防火墙）。

#### 1. 防火墙工具选择与安装



* `firewalld`**（推荐，适用于 CentOS7+/RHEL7+/Fedora）**
  默认已预装，若未安装可执行：
  
  

```
sudo yum install firewalld firewall-config  # 安装服务与图形化工具

sudo systemctl start firewalld              # 启动服务

sudo systemctl enable firewalld             # 开机自启

sudo systemctl status firewalld             # 检查运行状态
```



* `iptables`**（适用于 CentOS6/Ubuntu 或需复杂规则场景）**
  部分系统默认未安装，需手动安装：
  
  

```
sudo yum install iptables iptables-services  # CentOS

sudo apt install iptables iptables-persistent  # Ubuntu

sudo systemctl start iptables

sudo systemctl enable iptables
```

#### 2. 核心防火墙规则配置（以`firewalld`为例）

`firewalld`基于 “区域（zone）” 管理规则，不同区域对应不同安全级别，常用区域为`public`（公共网络，默认）、`internal`（内部网络）。



* **查看当前区域与规则**
  
  

```
sudo firewall-cmd --get-active-zones  # 查看活跃区域

sudo firewall-cmd --list-all          # 查看当前区域所有规则
```



* **开放常用安全端口**
  仅开放业务必需端口（如 SSH 22、HTTP 80、HTTPS 443），禁止所有未授权端口：
  
  

```
\# 开放SSH端口（远程登录必需，生产环境建议修改默认22端口）

sudo firewall-cmd --permanent --add-port=22/tcp

\# 开放HTTP/HTTPS端口（web服务）

sudo firewall-cmd --permanent --add-port=80/tcp

sudo firewall-cmd --permanent --add-port=443/tcp

\# 开放数据库端口（如MySQL 3306，仅允许特定IP访问）

sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100/32" port port="3306" protocol="tcp" accept'

\# 重新加载规则使生效

sudo firewall-cmd --reload
```



* **禁止危险端口与 IP**
  拒绝已知恶意 IP 或常见攻击端口（如 3389、135 等 Windows 常见端口，Linux 环境无需开放）：
  
  

```
\# 禁止特定IP访问所有端口

sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.10/32" reject'

\# 禁止所有IP访问3389端口

sudo firewall-cmd --permanent --remove-port=3389/tcp  # 若已开放则移除

sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="3389" protocol="tcp" reject'

sudo firewall-cmd --reload
```



* **配置端口转发（可选）**
  若需将外部端口映射到内部服务端口（如将 8080 端口转发到 80）：
  
  

```
sudo firewall-cmd --permanent --add-masquerade  # 启用地址伪装

sudo firewall-cmd --permanent --add-forward-port=port=8080:proto=tcp:toaddr=127.0.0.1:toport=80

sudo firewall-cmd --reload
```

#### 3. `iptables`基础规则示例（备用）

若使用`iptables`，需手动编写链规则，以下为基础安全配置：



```
\# 清空现有规则

sudo iptables -F

\# 设置默认策略（入站拒绝、出站允许、转发拒绝）

sudo iptables -P INPUT DROP

sudo iptables -P OUTPUT ACCEPT

sudo iptables -P FORWARD DROP

\# 允许已建立连接的数据包

sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

\# 允许本地回环（localhost）

sudo iptables -A INPUT -i lo -j ACCEPT

\# 允许SSH端口

sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

\# 保存规则（CentOS）

sudo service iptables save
```

### 安全协议和服务配置

Linux 系统默认启用部分服务与协议，部分存在安全漏洞（如 Telnet、FTP 明文传输），需禁用不安全服务，启用加密协议，同时优化服务配置以降低攻击面。

#### 1. 禁用不安全服务与协议



* **禁止 Telnet 服务（明文传输，已被 SSH 替代）**
  
  

```
sudo systemctl stop telnet.socket

sudo systemctl disable telnet.socket

\# 卸载Telnet服务（可选）

sudo yum remove telnet-server  # CentOS

sudo apt remove telnetd        # Ubuntu
```



* **禁用 FTP 服务（明文传输，建议替换为 SFTP）**
  若无需 FTP 服务，直接禁用；若需文件传输，使用 SSH 内置的 SFTP（加密传输）：
  
  

```
sudo systemctl stop vsftpd  # 停止FTP服务（以vsftpd为例）

sudo systemctl disable vsftpd

\# 验证SFTP可用性（SSH启用则默认支持）

sftp user@server\_ip  # 客户端测试连接
```



* **关闭不必要的系统服务**
  查看并禁用无用服务（如`rpcbind`、`cups`等）：
  
  

```
\# 查看运行中的服务

sudo systemctl list-units --type=service --state=running

\# 禁用无用服务（示例：禁用打印机服务cups）

sudo systemctl stop cups

sudo systemctl disable cups
```

#### 2. 启用加密协议与优化配置



* **强化 SSH 服务安全（核心远程登录协议）**
  SSH 默认使用 22 端口，存在暴力破解风险，需通过修改`/etc/ssh/sshd_config`优化配置：
  
  

```
sudo vim /etc/ssh/sshd\_config
```

关键配置修改：



```
sudo systemctl restart sshd
```



* `Port 2222`：修改默认端口为非 22 端口（如 2222，降低扫描风险）；

* `PermitRootLogin no`：禁止 root 用户直接远程登录；

* `PasswordAuthentication no`：禁用密码登录，仅允许 SSH 密钥登录（最安全，需提前配置密钥）；

* `PermitEmptyPasswords no`：禁止空密码登录；

* `MaxAuthTries 3`：最大认证尝试次数 3 次（超过则断开连接）；

* `ClientAliveInterval 600`：客户端无操作 10 分钟后断开连接。
  修改后重启 SSH 服务生效：
- **启用 HTTPS 协议（Web 服务加密）**
  对于 Web 服务（如 Nginx、Apache），需配置 SSL/TLS 证书，强制使用 HTTPS 加密传输：
  
  

```
\# 以Nginx为例，配置HTTPS（需提前获取SSL证书，如Let's Encrypt免费证书）

sudo vim /etc/nginx/conf.d/ssl.conf
```

核心配置片段：



```
server {

&#x20;   listen 443 ssl;

&#x20;   server\_name example.com;

&#x20;   # SSL证书路径

&#x20;   ssl\_certificate /etc/letsencrypt/live/example.com/fullchain.pem;

&#x20;   ssl\_certificate\_key /etc/letsencrypt/live/example.com/privkey.pem;

&#x20;   # 启用TLS1.2/1.3（禁用不安全的TLS1.0/1.1）

&#x20;   ssl\_protocols TLSv1.2 TLSv1.3;

&#x20;   # 加密套件（优先选择安全强度高的套件）

&#x20;   ssl\_prefer\_server\_ciphers on;

&#x20;   ssl\_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

&#x20;   # 强制HTTP跳转HTTPS

&#x20;   return 301 https://\$host\$request\_uri;

}
```

重启 Nginx 生效：



```
sudo systemctl restart nginx
```

#### 3. 协议版本与加密套件优化



* **禁用不安全的 TLS 版本**
  对于所有启用 SSL/TLS 的服务（SSH、HTTPS、SMTP 等），禁用 TLS1.0、TLS1.1（存在漏洞），仅保留 TLS1.2 及以上版本；

* **选择安全加密套件**
  优先使用支持前向 secrecy（前向保密）的加密套件（如`EECDH+AESGCM`、`EDH+AESGCM`），避免使用 RC4、3DES 等弱加密算法。

> （注：文档部分内容可能由 AI 生成）


