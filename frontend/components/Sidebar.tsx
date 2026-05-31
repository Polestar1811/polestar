import Link from "next/link";
import { BarChart3, Boxes, Home, Megaphone, MessageSquare, Package, Settings, ShieldCheck, TicketCheck } from "lucide-react";

const items = [
  ["/dashboard", Home, "首页"],
  ["/chat", MessageSquare, "Agent"],
  ["/products", Package, "商品"],
  ["/orders", ShieldCheck, "订单"],
  ["/inventory", Boxes, "库存"],
  ["/tickets", TicketCheck, "售后"],
  ["/campaigns", Megaphone, "营销"],
  ["/reports", BarChart3, "报表"],
  ["/admin", Settings, "管理"]
] as const;

export function Sidebar() {
  return (
    <aside className="min-h-screen w-56 border-r border-black/10 bg-white px-3 py-4">
      <div className="mb-6 px-3 text-xl font-semibold text-tea">TeaAgent</div>
      <nav className="space-y-1">
        {items.map(([href, Icon, label]) => (
          <Link className="flex items-center gap-3 rounded-md px-3 py-2 text-sm hover:bg-rice" key={href} href={href}>
            <Icon size={18} />
            {label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
