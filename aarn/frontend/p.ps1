Write-Host "Generating AARN frontend structure..." -ForegroundColor Cyan

# Create directories
New-Item -ItemType Directory -Force -Path "src\lib" | Out-Null
New-Item -ItemType Directory -Force -Path "src\types" | Out-Null
New-Item -ItemType Directory -Force -Path "src\components" | Out-Null
New-Item -ItemType Directory -Force -Path "src\app\search" | Out-Null
New-Item -ItemType Directory -Force -Path "src\app\paper\[id]" | Out-Null

# -------------------------
# lib/api.ts
# -------------------------
@"
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;
"@ | Set-Content "src/lib/api.ts"

# -------------------------
# types/paper.ts
# -------------------------
@"
export interface Paper {
  id: string;
  title: string;
  abstract: string;
}
"@ | Set-Content "src/types/paper.ts"

# -------------------------
# components/PaperCard.tsx
# -------------------------
@"
import { Paper } from "@/types/paper";

export default function PaperCard({ paper }: { paper: Paper }) {
  return (
    <a
      href={`/paper/${paper.id}`}
      className="block bg-white p-5 rounded-xl shadow-sm border hover:shadow-md transition"
    >
      <h2 className="text-xl font-semibold">{paper.title}</h2>
      <p className="text-gray-600 text-sm mt-2">{paper.abstract}</p>
    </a>
  );
}
"@ | Set-Content "src/components/PaperCard.tsx"

# -------------------------
# app/search/page.tsx
# -------------------------
@"
"use client";

import { useState } from "react";
import api from "@/lib/api";
import PaperCard from "@/components/PaperCard";

export default function SearchPage() {
  const [query, setQuery] = useState("");
  const [papers, setPapers] = useState([]);

  const handleSearch = async () => {
    const res = await api.get("/search/", { params: { q: query } });
    setPapers(res.data);
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Search Papers</h1>

      <div className="flex gap-3 mb-6">
        <input
          className="border px-4 py-2 rounded-lg flex-1"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter keyword"
        />
        <button
          onClick={handleSearch}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg"
        >
          Search
        </button>
      </div>

      <div className="space-y-4">
        {papers.map((p: any) => (
          <PaperCard key={p.id} paper={p} />
        ))}
      </div>
    </div>
  );
}
"@ | Set-Content "src/app/search/page.tsx"

# -------------------------
# app/paper/[id]/page.tsx
# -------------------------
@"
"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";

export default function PaperPage({ params }: any) {
  const { id } = params;
  const [paper, setPaper] = useState(null);

  useEffect(() => {
    api.get(`/papers/${id}`).then((res) => {
      setPaper(res.data);
    });
  }, [id]);

  if (!paper) return <div>Loading...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold">{paper.title}</h1>
      <p className="mt-4 text-gray-700 whitespace-pre-line">{paper.abstract}</p>
    </div>
  );
}
"@ | Set-Content "src/app/paper/[id]/page.tsx"


Write-Host "All frontend files generated successfully." -ForegroundColor Green
