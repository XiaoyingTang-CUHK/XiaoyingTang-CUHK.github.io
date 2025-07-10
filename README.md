# SMILE Lab 网站

香港中文大学（深圳）SMILE实验室官方网站

## 项目结构

```
website/
├── index.html          # 首页
├── research.html       # 研究页面
├── publications.html   # 出版物页面
├── team.html          # 团队页面
├── contact.html       # 联系我们页面
├── style.css          # 样式文件
└── README.md          # 项目说明
```

## 部署步骤

### 1. 本地准备

```bash
# 进入项目目录
cd Desktop/website

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: SMILE Lab website"
```

### 2. 推送到远程仓库

```bash
# 添加远程仓库（替换为您的Git仓库地址）
git remote add origin <your-repository-url>

# 推送到远程仓库
git push -u origin main
```

### 3. 服务器部署

#### 选项A：使用Nginx部署

```bash
# 在服务器上安装Nginx
sudo apt update
sudo apt install nginx

# 创建网站目录
sudo mkdir -p /var/www/smile-lab

# 克隆项目到服务器
sudo git clone <your-repository-url> /var/www/smile-lab

# 配置Nginx
sudo nano /etc/nginx/sites-available/smile-lab
```

Nginx配置示例：
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/smile-lab;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

```bash
# 启用站点
sudo ln -s /etc/nginx/sites-available/smile-lab /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启Nginx
sudo systemctl restart nginx
```

#### 选项B：使用Apache部署

```bash
# 安装Apache
sudo apt update
sudo apt install apache2

# 部署文件到Apache目录
sudo cp -r * /var/www/html/

# 重启Apache
sudo systemctl restart apache2
```

### 4. 自动化部署脚本

创建部署脚本 `deploy.sh`：

```bash
#!/bin/bash
echo "开始部署SMILE Lab网站..."

# 更新代码
git pull origin main

# 备份当前版本
sudo cp -r /var/www/smile-lab /var/www/smile-lab-backup-$(date +%Y%m%d-%H%M%S)

# 部署新版本
sudo cp -r * /var/www/smile-lab/

# 设置权限
sudo chown -R www-data:www-data /var/www/smile-lab
sudo chmod -R 755 /var/www/smile-lab

# 重启Web服务器
sudo systemctl restart nginx

echo "部署完成！"
```

## 维护说明

- 定期备份网站文件
- 监控服务器状态
- 更新SSL证书（如使用HTTPS）
- 定期更新依赖和系统

## 联系方式

如有问题，请联系网站管理员。 