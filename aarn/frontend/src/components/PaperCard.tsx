import { Paper } from "@/types/paper";

export default function PaperCard({ paper }: { paper: Paper }) {
  return (
    <a
      href={/paper/}
      className="block bg-white p-5 rounded-xl shadow-sm border hover:shadow-md transition"
    >
      <h2 className="text-xl font-semibold">{paper.title}</h2>
      <p className="text-gray-600 text-sm mt-2">{paper.abstract}</p>
    </a>
  );
}
