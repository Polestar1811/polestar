# TeaAgent 企业级完善路线

## 已完成

- 多 Agent 路由和结构化 JSON 输出
- 商品推荐、订单查询、售后、库存、营销、报表、知识库问答
- FastAPI API 层
- Next.js 后台工作台
- JWT 登录和 RBAC
- audit_log、llm_log、tool trace_id
- DeepSeek/Kimi Provider 封装
- 本地和局域网启动脚本
- 后端自动化测试
- 前端生产构建和依赖安全审计

## 企业上线前必须补齐

1. 数据持久化
   - PostgreSQL 正式表结构和 Alembic 迁移
   - 用户密码哈希、登录失败限制、Token 刷新
   - audit_log/llm_log/tool_log 持久化查询

2. 真实业务系统连接
   - OMS 订单和物流
   - ERP 库存和采购
   - CRM 客户画像
   - 售后系统、退款系统、发票系统
   - 企业微信、短信、邮件

3. 知识库
   - 文件上传
   - 文档切分
   - ChromaDB/Milvus 向量检索
   - 来源引用和版本管理

4. 高风险审批
   - 退款、补发、群发、库存调整审批流
   - 审批人、审批时间、审批结果留痕
   - 超额和异常规则

5. 模型治理
   - Prompt 后台编辑、版本发布、回滚
   - 模型路由策略配置
   - Token 成本统计
   - JSON 解析失败重试
   - 敏感信息脱敏

6. 部署运维
   - Docker Desktop 本地部署包
   - 生产 Nginx/HTTPS
   - 日志轮转、备份、监控
   - 环境变量和密钥管理

## 建议下一阶段

下一阶段建议优先做“可交付给客户试用”的企业版：

- PostgreSQL 持久化
- Prompt 管理后台可编辑
- 知识库文件上传和检索
- DeepSeek 真实调用接入到 Agent
- 售后/营销审批流
- 局域网部署包和客户使用手册
