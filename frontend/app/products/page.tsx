import { DataTable } from "../../components/DataTable";
import { Sidebar } from "../../components/Sidebar";
import { apiGet } from "../../lib/api";

export const dynamic = "force-dynamic";

export default async function ProductsPage() {
  const res = await apiGet<{ data: Record<string, unknown>[] }>("/api/products");
  const rows = res.data.map((p) => ({ sku_id: p.sku_id, name: p.name, price: p.price, stock: p.stock, tags: Array.isArray(p.tags) ? p.tags.join("/") : "" }));
  return <main className="flex"><Sidebar /><section className="flex-1 p-6"><h1 className="mb-5 text-2xl font-semibold">商品管理</h1><DataTable columns={["sku_id", "name", "price", "stock", "tags"]} rows={rows} /></section></main>;
}
