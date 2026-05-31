import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "TeaAgent", description: "茶叶电商企业智能体系统" };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
