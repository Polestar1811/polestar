"use client";

import { Send, UserCheck } from "lucide-react";
import { useState } from "react";
import { apiPost } from "../lib/api";
import type { ChatResponse } from "../lib/types";

const agents = ["auto", "kb", "recommendation", "order", "aftersale", "inventory", "marketing", "reporting"];

export function AgentChat() {
  const [agent, setAgent] = useState("auto");
  const [message, setMessage] = useState("送长辈300元左右茶叶推荐");
  const [items, setItems] = useState<{ role: string; text: string }[]>([]);
  const [last, setLast] = useState<ChatResponse | null>(null);
  const [loading, setLoading] = useState(false);

  async function submit() {
    if (!message.trim()) return;
    setLoading(true);
    setItems((old) => [...old, { role: "user", text: message }]);
    try {
      const res = await apiPost<ChatResponse>("/api/chat", { message, agent_type: agent, context: {} });
      setLast(res);
      setItems((old) => [...old, { role: "assistant", text: res.reply }]);
      setMessage("");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="grid min-h-[calc(100vh-64px)] grid-cols-[180px_1fr_360px] gap-4">
      <div className="rounded-md border border-black/10 bg-white p-3">
        <div className="mb-3 text-sm font-medium">Agent</div>
        <div className="space-y-1">
          {agents.map((a) => (
            <button key={a} onClick={() => setAgent(a)} className={`w-full rounded-md px-3 py-2 text-left text-sm ${agent === a ? "bg-tea text-white" : "hover:bg-rice"}`}>{a}</button>
          ))}
        </div>
      </div>
      <div className="flex flex-col rounded-md border border-black/10 bg-white">
        <div className="flex-1 space-y-3 overflow-auto p-4">
          {items.map((item, i) => (
            <div key={i} className={`max-w-[75%] rounded-md px-3 py-2 text-sm ${item.role === "user" ? "ml-auto bg-tea text-white" : "bg-rice"}`}>{item.text}</div>
          ))}
        </div>
        <div className="flex gap-2 border-t border-black/10 p-3">
          <input className="flex-1 rounded-md border border-black/10 px-3 py-2" value={message} onChange={(e) => setMessage(e.target.value)} onKeyDown={(e) => e.key === "Enter" && submit()} />
          <button className="inline-flex items-center gap-2 rounded-md bg-clay px-4 py-2 text-white" onClick={submit} disabled={loading}><Send size={16} />发送</button>
        </div>
      </div>
      <div className="space-y-4">
        <button className="inline-flex w-full items-center justify-center gap-2 rounded-md border border-black/10 bg-white px-4 py-2"><UserCheck size={16} />人工接管</button>
        <div className="rounded-md border border-black/10 bg-white p-4">
          <div className="font-medium">工具轨迹</div>
          <pre className="mt-3 max-h-48 overflow-auto text-xs">{JSON.stringify(last?.tool_traces ?? [], null, 2)}</pre>
        </div>
        <div className="rounded-md border border-black/10 bg-white p-4">
          <div className="font-medium">JSON 输出</div>
          <pre className="mt-3 max-h-80 overflow-auto text-xs">{JSON.stringify(last?.structured_output ?? {}, null, 2)}</pre>
        </div>
      </div>
    </div>
  );
}
