import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NexTrip - Travel Planner",
  description: "Constraint-driven travel planner for HackCellence 2026",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
