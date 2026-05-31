"use client";
import { useEffect, useState } from "react";
import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

const data = [
  { day: "Mon", gmv: 18000 },
  { day: "Tue", gmv: 21000 },
  { day: "Wed", gmv: 19000 },
  { day: "Thu", gmv: 24000 },
  { day: "Fri", gmv: 28600 }
];

export function ReportChart() {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  return (
    <div className="h-72 min-h-72 min-w-0 rounded-md border border-black/10 bg-white p-4">
      {mounted ? (
        <ResponsiveContainer width="100%" height="100%" minWidth={1} minHeight={1}>
          <LineChart data={data}>
            <XAxis dataKey="day" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="gmv" stroke="#34745a" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      ) : null}
    </div>
  );
}
