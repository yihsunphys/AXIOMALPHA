import "./globals.css";

export const metadata = {
  title: "AARN",
  description: "Research Navigator Frontend",
};

export default function RootLayout({ children }) {
  return (
    <html lang="zh-Hant">
      <body className="min-h-screen bg-gray-50 text-gray-900">

        <nav className="backdrop-blur bg-white/70 border-b border-gray-200 sticky top-0 z-20">
          <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="/" className="text-2xl font-bold">AARN</a>
            <div className="flex gap-6 text-lg">
              <a href="/search" className="hover:text-blue-600">搜尋論文</a>
            </div>
          </div>
        </nav>

        <main className="max-w-5xl mx-auto px-6 py-10">
          {children}
        </main>

      </body>
    </html>
  );
}
