import { ApprovalQueue } from "../../components/ApprovalQueue";
import { ReportChart } from "../../components/ReportChart";
import { Sidebar } from "../../components/Sidebar";
import { StatCard } from "../../components/StatCard";

export default function DashboardPage() {
  return (
    <main className="flex">
      <Sidebar />
      <section className="flex-1 p-6">
        <h1 className="text-2xl font-semibold">经营首页</h1>
        <div className="mt-5 grid grid-cols-4 gap-4">
          <StatCard label="今日 GMV" value="¥128,600" note="较昨日 +8.4%" />
          <StatCard label="今日订单" value="842" />
          <StatCard label="客单价" value="¥152.7" />
          <StatCard label="退款率" value="3.2%" />
          <StatCard label="库存预警" value="3" />
          <StatCard label="待审批" value="6" />
          <StatCard label="Agent 调用" value="1,248" />
          <StatCard label="自动解决率" value="71%" />
        </div>
        <div className="mt-5 grid grid-cols-[1fr_320px] gap-4">
          <ReportChart />
          <ApprovalQueue />
        </div>
      </section>
    </main>
  );
}
