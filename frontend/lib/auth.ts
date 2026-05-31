export function getRole() {
  if (typeof window === "undefined") return "owner";
  return localStorage.getItem("role") || "owner";
}
