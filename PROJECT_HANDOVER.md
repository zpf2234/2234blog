# Kirameku 博客项目搭建与部署交接文档

## 📌 项目基本信息

- **项目目录**: `d:\mc\blog`
  - 前端目录: `d:\mc\blog\Kirameku` (Next.js 16 + React 19)
  - 后端目录: `d:\mc\blog\Kirameku-backend` (FastAPI + SQLModel)
- **GitHub 个人代码仓库**: [https://github.com/zpf2234/2234blog](https://github.com/zpf2234/2234blog)

---

## 🗄️ 1. 云端 PostgreSQL 数据库 (已就绪)

- **托管平台**: Neon (Free Tier)
- **数据库连接字符串 (DATABASE_URL)**:
  `postgresql://neondb_owner:npg_3prCXgIU2jvL@ep-misty-lake-ax9dhf61.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require`

---

## ⚙️ 2. 后端 API 服务 (已上线运行)

- **托管平台**: Render (Free Tier)
- **后端公网 API 地址**: `https://two234blog.onrender.com`
- **接口验证**:
  - 健康检查接口: `https://two234blog.onrender.com/api/health` ➡️ 返回 `{"status":"ok"}`
  - 交互式 API 文档: `https://two234blog.onrender.com/docs`
- ** Render 部署配置参数参考**:
  - Root Directory: `Kirameku-backend`
  - Environment: `Python 3`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
  - 环境变量设置:
    - `DATABASE_URL` = `postgresql://neondb_owner:npg_3prCXgIU2jvL@ep-misty-lake-ax9dhf61.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require`
    - `SECRET_KEY` = `kirameku-production-secret-key-2026`

---

## 🌐 3. 前端部署与自定义域名绑定 (待完成最后步)

- **托管平台**: Vercel
- **Vercel 项目链接**: [https://vercel.com/peter-3e0a/2234blog](https://vercel.com/peter-3e0a/2234blog)
- **接手智能体/开发者需要完成的设置**:
  1. 打开 Vercel 项目设置页: [https://vercel.com/peter-3e0a/2234blog/settings](https://vercel.com/peter-3e0a/2234blog/settings)
  2. 点击 **General** ➡️ 将 **Root Directory** 从空值修改为: `Kirameku`（必须区分大小写，指定前端子文件夹）并点击 **Save**。
  3. 点击 **Environment Variables** 确认包含:
     - `NEXT_PUBLIC_API_URL` = `https://two234blog.onrender.com`
  4. 点击 **Deployments** ➡️ 找到最新一次部署 ➡️ 点击右侧的三个点 **(...)** ➡️ 点击 **Redeploy**。
  5. 部署成功后，在 **Domains** 绑定你的个人域名，并根据 Vercel 给出的解析提示去域名商后台添加 DNS 记录（A 记录指向 `76.76.21.21` 或 CNAME 指向 `cname.vercel-dns.com`）。

---

## 💻 4. 本地启动运行命令（备用）

### 启动本地后端：
```powershell
cd d:\mc\blog\Kirameku-backend
.\venv\Scripts\uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 启动本地前端：
```powershell
cd d:\mc\blog\Kirameku
pnpm dev
```
