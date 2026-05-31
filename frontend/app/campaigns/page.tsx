import { Sidebar } from "../../components/Sidebar";

export default function CampaignsPage() {
  return (
    <main className="flex">
      <Sidebar />
      <section className="flex-1 p-6">
        <h1 className="text-2xl font-semibold">营销中心</h1>
        <div className="mt-5 grid grid-cols-2 gap-4">
          {["活动 brief", "小红书文案", "抖音脚本", "私域文案"].map((x) => <div key={x} className="rounded-md border border-black/10 bg-white p-4"><div className="font-medium">{x}</div><p className="mt-3 text-sm text-black/60">通过 Agent Chat 或 /api/campaigns/generate 生成，涉及优惠和群发会进入审批。</p></div>)}
        </div>
      </section>
    </main>
  );
}
