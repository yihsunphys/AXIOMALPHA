# AXIOMALPHA
Find the α Behind Every Algorithm


Project Description
AARN is a domain-specific research knowledge system for approximation algorithms. It distills raw Semantic Scholar results into enriched, verified, structured metadata, enabling users to quickly find relevant papers, understand their approximation ratios, methods, and algorithms, and access verified insights.
Key Points:
Data Source


Fetch papers via Semantic Scholar API (title, authors, year, abstract, venue, PDF link, citations).


Only pull papers on-demand based on user search.


Enrichment Layer (LLM + Rules)


Automatically extract from abstract:


Approximation ratio


Algorithm type (PTAS, FPTAS, greedy, etc.)


Analysis method / technique


Key result snippet


Optional: multi-agent or regex/LLM hybrid verification.


Human Verification Layer


Admins can manually confirm/correct extracted metadata.


Users may submit suggestions for unverified data (stored as “pending”).


Verification levels:


Auto-generated (LLM)


User-suggested


Admin-verified (final truth)


Database / Cache


SQLModel + SQLite (or PostgreSQL later).


Store: enriched metadata, verification status, history, and suggestion queue.


Acts as both cache (avoid repeated API calls) and knowledge base.


Search & UI


React + Vite + Tailwind frontend.


Search bar: keyword/topic search.


Results table: main info + verified status.


Detail modal: abstract, algorithm, analysis, citations, PDF link.


Admin panel: verify/modify papers.


Optional: filter only verified papers.


MVP Scope


Fetch papers from Semantic Scholar on-demand.


LLM + regex extraction of ratio, algorithm, and technique.


SQLite persistence of enriched data.


Manual admin verification panel.


Results UI with modal showing full details.


User suggestions for unverified papers.


Future Enhancements (Optional for MVP)


Lineage graph of improvements across papers.


Problem-centric pages (all papers for a specific problem).


Clustering papers by technique or domain.


PDF parsing for richer extraction.


Multi-agent LLM verification.


Researcher pages, SOTA tracker, reputation system.



System Architecture (High-Level)
User
  │
  ▼
Frontend (Vite + React + Tailwind)
  ├─ Search form → send query to backend
  ├─ Results table (verified badge)
  ├─ Paper Detail Modal (abstract, algorithm, ratio, citations)
  └─ Admin Panel (verify/correct papers)
  │
  ▼
Backend (FastAPI, Railway deployment)
  ├─ /search → query Semantic Scholar → enrich with LLM → store & return
  ├─ /admin/verify → manually verify or update paper metadata
  ├─ /suggest → store user suggestions (pending)
  ├─ Verification module (regex + LLM)
  └─ Database module (SQLModel + SQLite/PostgreSQL)
        ├─ Papers (enriched + verified)
        ├─ Suggestions (user edits pending)
        └─ Version history


Key Technologies
Backend: FastAPI, SQLModel, SQLite/PostgreSQL


Frontend: React, Vite, TailwindCSS, Axios


LLM: OpenAI GPT (optional for verification/summarization)


API Integration: Semantic Scholar Graph API


Deployment:


Backend → Railway (Python server)


Frontend → Vercel (static build, calls backend API)



MVP Priorities
Core search → fetch → LLM distillation → DB cache.


Manual admin verification panel.


Frontend results table + modal UI.


Verified/unverified flags, filter.


Store user suggestions (optional MVP feature).


Everything else (lineage graphs, clusters, problem pages, reputation) can be post-MVP enhancements




                ┌───────────────┐
                │     User      │
                │───────────────│
                │ - Search      │
                │ - View Results│
                │ - Submit Suggestion │
                └───────┬───────┘
                        │
                        ▼
             ┌─────────────────────┐
             │     Frontend        │
             │ (React + Tailwind)  │
             │────────────────────│
             │ - Search Form       │
             │ - Results Table     │
             │ - Detail Modal      │
             │ - Verified Badge    │
             │ - Admin Panel       │
             └───────┬────────────┘
                     │
                     ▼
             ┌─────────────────────┐
             │     Backend         │
             │   (FastAPI)         │
             │────────────────────│
             │ - /search API       │
             │ - /verify API       │
             │ - /suggest API      │
             │ - LLM Extraction    │
             │ - Regex Verification│
             └───────┬────────────┘
                     │
     ┌───────────────┼───────────────┐
     ▼                               ▼
┌─────────────┐                 ┌─────────────┐
│Semantic     │                 │ Database    │
│Scholar API  │                 │ (SQLModel)  │
│─────────────│                 │─────────────│
│ - Fetch     │                 │ Papers Table│
│   metadata  │                 │ - enriched  │
│ - Abstracts │                 │ - verified  │
│ - PDFs      │                 │ - history   │
│ - Citations │                 │ Suggestions │
└─────────────┘                 └─────────────┘
                     ▲
                     │
              Admin Verification
                     │
                     ▼
             ┌─────────────────────┐
             │ Human-in-the-loop   │
             │ - Admins verify     │
             │ - Final labels      │
             └─────────────────────┘


