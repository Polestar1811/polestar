import { AgentChat } from "../../components/AgentChat";
import { Sidebar } from "../../components/Sidebar";

export default function ChatPage() {
  return (
    <main className="flex">
      <Sidebar />
      <section className="flex-1 p-6">
        <h1 className="mb-5 text-2xl font-semibold">Agent Chat</h1>
        <AgentChat />
      </section>
    </main>
  );
}
