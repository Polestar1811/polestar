export function InventoryAlertCard({ item }: { item: Record<string, unknown> }) {
  return (
    <div className="rounded-md border border-black/10 bg-white p-4">
      <div className="font-medium">{String(item.name)}</div>
      <div className="mt-2 text-sm text-black/60">库存 {String(item.stock)} · {String(item.stock_status)} · {String(item.risk_level)}</div>
    </div>
  );
}
