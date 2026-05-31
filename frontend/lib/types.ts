export type ChatResponse = {
  reply: string;
  intent: string;
  agent: string;
  structured_output: Record<string, unknown>;
  tool_traces: Record<string, unknown>[];
  sources: string[];
  need_human: boolean;
};
