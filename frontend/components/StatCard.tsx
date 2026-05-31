export function StatCard({ label, value, note }: { label: string; value: string; note?: string }) {
  return (
    <div className="rounded-md border border-black/10 bg-white p-4">
      <div className="text-sm text-black/60">{label}</div>
      <div className="mt-2 text-2xl font-semibold">{value}</div>
      {note ? <div className="mt-2 text-xs text-black/50">{note}</div> : null}
    </div>
  );
}
