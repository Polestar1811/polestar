const data = [
  { day: "周一", gmv: 18000 },
  { day: "周二", gmv: 21000 },
  { day: "周三", gmv: 19000 },
  { day: "周四", gmv: 24000 },
  { day: "周五", gmv: 28600 },
  { day: "周六", gmv: 32600 },
  { day: "周日", gmv: 29200 }
];

function points(width: number, height: number) {
  const max = Math.max(...data.map((d) => d.gmv));
  const min = Math.min(...data.map((d) => d.gmv));
  return data
    .map((d, index) => {
      const x = 40 + (index * (width - 80)) / (data.length - 1);
      const y = 24 + (height - 64) * (1 - (d.gmv - min) / Math.max(1, max - min));
      return `${x},${y}`;
    })
    .join(" ");
}

export function ReportChart() {
  const width = 720;
  const height = 260;
  return (
    <div className="h-72 rounded-md border border-black/10 bg-white p-4">
      <div className="mb-3 flex items-center justify-between">
        <div>
          <div className="text-sm text-black/50">GMV 趋势</div>
          <div className="text-xl font-semibold">¥172,400</div>
        </div>
        <div className="rounded-md bg-tea/10 px-2 py-1 text-xs text-tea">本周 +12.8%</div>
      </div>
      <svg className="h-[205px] w-full" viewBox={`0 0 ${width} ${height}`} role="img" aria-label="GMV trend chart">
        {[0, 1, 2, 3].map((line) => (
          <line key={line} x1="40" x2={width - 40} y1={28 + line * 52} y2={28 + line * 52} stroke="#e8e0d2" strokeWidth="1" />
        ))}
        <polyline fill="none" stroke="#34745a" strokeWidth="4" strokeLinejoin="round" strokeLinecap="round" points={points(width, height)} />
        {data.map((d, index) => {
          const point = points(width, height).split(" ")[index].split(",").map(Number);
          return (
            <g key={d.day}>
              <circle cx={point[0]} cy={point[1]} r="5" fill="#b96535" />
              <text x={point[0]} y={height - 14} textAnchor="middle" fontSize="13" fill="#5f6d65">{d.day}</text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}
