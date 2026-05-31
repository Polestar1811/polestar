import { DataTable } from "../../components/DataTable";
import { Sidebar } from "../../components/Sidebar";

const rows = [
  { area: "用户角色", status: "owner/admin/cs/ops/warehouse/finance/viewer" },
  { area: "Prompt 管理", status: "文件化配置" },
  { area: "模型配置", status: "DeepSeek/Kimi Provider" },
  { area: "调用日志", status: "llm_log/tool_log/audit_log" }
];

export default function AdminPage() {
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">管理后台</h1><DataTable columns={["area", "status"]} rows={rows} /></section></main>;
}
