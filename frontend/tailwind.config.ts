import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#1d2823",
        tea: "#34745a",
        clay: "#b96535",
        rice: "#f6f1e7"
      }
    }
  },
  plugins: []
};

export default config;
