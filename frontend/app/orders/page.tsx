import { DataTable } from "../../components/DataTable";
import { Sidebar } from "../../components/Sidebar";

const rows = [
  { order_no: "ORD001", customer: "C001", status: "已发货", tracking: "运输中", actions: "查看物流/创建售后" },
  { order_no: "ORD002", customer: "C002", status: "待出库", tracking: "暂无", actions: "允许改地址" },
  { order_no: "ORD003", customer: "C003", status: "已签收", tracking: "已签收", actions: "售后审核" }
];

export default function OrdersPage() {
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">订单查询</h1><DataTable columns={["order_no", "customer", "status", "tracking", "actions"]} rows={rows} /></section></main>;
}
