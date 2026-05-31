"use client";
import { LogIn } from "lucide-react";
import { useState } from "react";
import { apiPost } from "../../lib/api";

export default function LoginPage() {
  const [email, setEmail] = useState("owner@example.com");
  async function login() {
    const res = await apiPost<{ access_token: string; user: { role: string } }>("/api/auth/login", { email, password: "demo" });
    localStorage.setItem("token", res.access_token);
    localStorage.setItem("role", res.user.role);
    location.href = "/dashboard";
  }
  return (
    <main className="grid min-h-screen place-items-center bg-rice">
      <div className="w-full max-w-sm rounded-md border border-black/10 bg-white p-6">
        <h1 className="text-2xl font-semibold text-tea">TeaAgent</h1>
        <input className="mt-6 w-full rounded-md border border-black/10 px-3 py-2" value={email} onChange={(e) => setEmail(e.target.value)} />
        <button className="mt-4 inline-flex w-full items-center justify-center gap-2 rounded-md bg-tea px-4 py-2 text-white" onClick={login}><LogIn size={16} />登录</button>
      </div>
    </main>
  );
}
