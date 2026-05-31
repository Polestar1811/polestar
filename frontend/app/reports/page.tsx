import { ReportChart } from "../../components/ReportChart";
import { Sidebar } from "../../components/Sidebar";
import { StatCard } from "../../components/StatCard";

export default function ReportsPage() {
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">经营报表</h1><div className="grid grid-cols-4 gap-4"><StatCard label="GMV" value="¥128,600" /><StatCard label="渠道最佳" value="私域" /><StatCard label="SKU Top1" value="龙井礼盒" /><StatCard label="周转风险" value="3 SKU" /></div><div className="mt-5"><ReportChart /></div></section></main>;
}
