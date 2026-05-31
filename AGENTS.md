# TeaAgent Agent 工作规范

## 项目目标

实现一个面向茶叶电商企业的智能体系统，帮助客服、运营、仓库、财务和管理者处理高频业务。

## 技术栈

- 前端：Next.js、React、TypeScript、Tailwind CSS、lucide-react、recharts
- 后端：FastAPI、Pydantic、SQLAlchemy、PostgreSQL、Redis、ChromaDB
- LLM：DeepSeek/Kimi OpenAI-compatible API，通过统一 Provider 调用

## 代码规范

- 所有业务工具必须通过 `backend/app/tools` 封装。
- Agent 不直接访问数据库，不直接执行高风险动作。
- API Key 只从环境变量读取。
- 输出结构优先使用 Pydantic schema。

## 后端规范

- 敏感动作写入 `audit_log`。
- LLM 调用写入 `llm_log`。
- 工具调用必须带 `trace_id`。
- 权限判断集中在 `permission_service.py`。

## 前端规范

- 页面以后台工作台为主，信息密度适中。
- 操作按钮使用图标和简短文本。
- 金额、客户、订单敏感信息按角色展示。

## Prompt 管理规范

- 每个 Agent 的 system prompt 独立保存在 `backend/app/prompts`。
- Prompt 只描述职责、边界、JSON 输出和合规规则。

## 禁止事项

1. 不允许把 API Key 写进代码。
2. 不允许让前端直连 DeepSeek/Kimi。
3. 不允许让模型直接操作数据库。
4. 不允许模型直接执行退款、补发、群发等高风险动作。
5. 不允许无权限访问财务、客户隐私和订单敏感信息。
6. 不允许编造商品信息、物流信息、售后政策。
7. 不允许绕过 audit_log。
