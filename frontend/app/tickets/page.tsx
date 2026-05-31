import { DataTable } from "../../components/DataTable";
import { Sidebar } from "../../components/Sidebar";

const rows = [
  { type: "damaged_package", risk: "medium", suggestion: "收集照片后人工审核", status: "pending_review" },
  { type: "quality_issue", risk: "high", suggestion: "食品安全风险人工审核", status: "pending_review" }
];

export default function TicketsPage() {
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">售后工单</h1><DataTable columns={["type", "risk", "suggestion", "status"]} rows={rows} /></section></main>;
}
