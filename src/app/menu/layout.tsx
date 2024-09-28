import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Sidebar from "../components/sidebar/sidebar";
import TopNav from "../components/top-nav/top-nav";
import "../globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Next.js App with Sidebar and Top Nav",
  description: "Created with Next.js, Tailwind CSS, and shadcn/ui",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex h-screen bg-gray-100">
          <Sidebar />
          <div className="flex flex-col flex-1 overflow-hidden">
            <TopNav />
            <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100">
              <div className="container mx-auto px-6 py-8">{children}</div>
            </main>
          </div>
        </div>
      </body>
    </html>
  );
}
