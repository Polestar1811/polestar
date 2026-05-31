export function ApprovalQueue() {
  return (
    <div className="rounded-md border border-black/10 bg-white p-4">
      <div className="font-medium">审批队列</div>
      <div className="mt-3 space-y-2 text-sm text-black/70">
        <div>售后人工审核 · 中风险</div>
        <div>营销群发审批 · 待确认优惠</div>
      </div>
    </div>
  );
}
