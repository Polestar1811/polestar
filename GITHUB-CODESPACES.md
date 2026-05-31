# 使用 GitHub Codespaces 给客户外网访问

## 适合什么场景

GitHub Codespaces 适合演示、测试、客户试用链接。它可以把项目里的 3000 和 8000 端口转成公网 URL，例如：

- 前端：`https://你的codespace名-3000.app.github.dev`
- 后端：`https://你的codespace名-8000.app.github.dev/docs`

注意：Codespaces 会休眠，有用量额度，不建议当正式生产服务器。

## 第一步：推到 GitHub 仓库

在项目根目录执行：

```bash
git init
git add .
git commit -m "Initial TeaAgent"
git branch -M main
git remote add origin https://github.com/你的账号/tea-agent.git
git push -u origin main
```

如果你已经有仓库，只需要设置正确的 `origin` 并推送。

## 第二步：创建 Codespace

打开 GitHub 仓库页面：

1. 点击 `Code`
2. 切换到 `Codespaces`
3. 点击 `Create codespace on main`

GitHub 会根据 `.devcontainer/devcontainer.json` 安装 Python、Node、后端依赖和前端依赖。

## 第三步：配置 DeepSeek API Key

不要把 Key 写进 Git 仓库。

推荐方式：

1. 在 GitHub 页面打开 `Settings`
2. 进入 `Codespaces`
3. 添加 Repository secret：
   - `DEEPSEEK_API_KEY`

或者在 Codespaces 终端里临时写入 `.env`：

```bash
cp .env.example .env
sed -i "s|^DEEPSEEK_API_KEY=.*|DEEPSEEK_API_KEY=你的key|" .env
```

## 第四步：启动

在 Codespaces 终端运行：

```bash
bash start-codespaces.sh
```

脚本会启动后端和前端，并尽量把端口设置成 Public。

如果端口没有自动公开：

1. 打开 Codespaces 底部 `Ports` 面板
2. 找到 `3000` 和 `8000`
3. 右键选择 `Port Visibility`
4. 选择 `Public`

GitHub 官方说明：Codespaces 转发端口默认是私有；设置成 Public 后，任何知道 URL 的人无需登录即可访问。组织策略可能限制 Public 选项。

## 给客户的链接

把 3000 的链接发给客户：

```text
https://你的codespace名-3000.app.github.dev
```

如果客户需要看 API 文档，再发 8000：

```text
https://你的codespace名-8000.app.github.dev/docs
```

## 更正式的外网部署

如果要给客户长期使用，不建议用 Codespaces。建议：

- 前端：Vercel
- 后端：Render / Railway / Fly.io / 云服务器
- 数据库：Supabase Postgres / Neon / 云厂商 RDS
- GitHub Actions：自动测试和部署
