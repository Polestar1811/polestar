export function DataTable({ columns, rows }: { columns: string[]; rows: Record<string, unknown>[] }) {
  return (
    <div className="overflow-hidden rounded-md border border-black/10 bg-white">
      <table className="w-full text-left text-sm">
        <thead className="bg-rice">
          <tr>{columns.map((c) => <th className="px-4 py-3 font-medium" key={c}>{c}</th>)}</tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr className="border-t border-black/10" key={i}>
              {columns.map((c) => <td className="px-4 py-3" key={c}>{String(row[c] ?? "")}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
