import { InventoryAlertCard } from "../../components/InventoryAlertCard";
import { Sidebar } from "../../components/Sidebar";
import { apiGet } from "../../lib/api";

export const dynamic = "force-dynamic";

export default async function InventoryPage() {
  const res = await apiGet<{ data: Record<string, unknown>[] }>("/api/inventory/alerts");
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">库存预警</h1><div className="grid grid-cols-3 gap-4">{res.data.map((item) => <InventoryAlertCard key={String(item.sku_id)} item={item} />)}</div></section></main>;
}
