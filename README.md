# TeaAgent 企业智能体系统

TeaAgent 是一个面向茶叶电商公司的企业智能体系统，覆盖客服问答、商品推荐、订单查询、售后处理、库存预警、营销内容生成、经营分析、权限控制、审计日志和模型调用日志。

当前版本已经可以作为本地客户演示版运行：没有 DeepSeek API Key 时使用可控 mock 输出；配置 Key 后可通过统一 LLM Provider 接入 DeepSeek OpenAI-compatible API。

## 一键本地运行

在项目根目录运行：

```powershell
.\start-local.ps1
```

脚本会启动：

- 后端 API：http://127.0.0.1:8000/docs
- 前端网页：http://127.0.0.1:3000
- 局域网访问：http://你的电脑IP:3000

如果客户和你在同一个局域网内，让客户浏览器打开脚本输出的 `http://电脑IP:3000` 即可。

## GitHub 外网演示

如果客户不在同一个局域网，可以用 GitHub Codespaces 生成外网访问链接。配置和步骤见：

[GITHUB-CODESPACES.md](./GITHUB-CODESPACES.md)

简版流程：

```bash
git add .
git commit -m "Prepare TeaAgent Codespaces demo"
git push
```

然后在 GitHub 仓库页面创建 Codespace，并运行：

```bash
bash start-codespaces.sh
```

## 分开启动

后端：

```powershell
.\start-backend.ps1
```

前端：

```powershell
.\start-frontend.ps1
```

## 配置 DeepSeek

推荐使用交互式脚本，不要把 Key 发在聊天窗口里：

```powershell
.\configure-deepseek.ps1
```

脚本会写入本地 `.env` 文件：

```env
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEFAULT_LLM_PROVIDER=deepseek
DEFAULT_FAST_MODEL=deepseek-chat
DEFAULT_REASONING_MODEL=deepseek-reasoner
```

`.env` 已被 `.gitignore` 忽略，不会进入代码仓库。

后端启动后，可以测试 DeepSeek 是否连通：

```powershell
.\test-deepseek.ps1
```

如果返回 `"mock": true`，说明后端还没有读到 API Key，或者 Key 为空；如果返回模型回复和延迟，则说明真实模型已连通。

## 登录账号

演示版账号如下，任意密码均可登录：

- owner@example.com / owner
- cs@example.com / customer_service
- ops@example.com / operations
- warehouse@example.com / warehouse
- finance@example.com / finance

## 验收用例

在 `/chat` 输入：

- 送长辈300元左右茶叶推荐
- 我的ORD001订单到哪了
- 收到礼盒破损了
- 哪些SKU快断货了
- 帮我写一篇小红书龙井礼盒文案
- 本周销售情况怎么样

## 验证

后端：

```powershell
.\verify-backend.ps1
```

前端：

```powershell
.\build-frontend.ps1
```

已验证项：

- 后端测试通过
- 前端生产构建通过
- 前端依赖审计 0 漏洞
- 工具调用带 trace_id
- 高风险 Agent 建议写 audit_log
- LLM/Router 调用写 llm_log

## Docker 运行

如果客户电脑安装了 Docker Desktop：

```powershell
copy .env.example .env
docker compose up --build
```

## 当前仍是 mock 的外部系统

以下系统已保留封装接口，但当前使用 mock 数据：

- ERP/OMS/CRM
- 物流查询
- 发票系统
- 退款/补发执行系统
- 企业微信/邮件/短信
- ChromaDB 知识库检索

生产上线前，需要把 `backend/app/tools` 中的 mock 函数替换成真实系统连接，并增加真实数据库迁移、备份、监控和日志采集。
