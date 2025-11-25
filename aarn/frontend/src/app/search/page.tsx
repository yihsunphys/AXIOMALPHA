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
