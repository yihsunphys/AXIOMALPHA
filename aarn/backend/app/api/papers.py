from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..db.base import get_session
from ..db.models import Paper
from ..db.crud import upsert_papers as crud_upsert
import json

router = APIRouter(prefix="/papers")


def paper_to_dict(paper):
    return {
        "paper_id": paper.paper_id,
        "title": paper.title,
        "authors": json.loads(paper.authors or "[]"),
        "year": paper.year,
        "venue": paper.venue,
        "pdf_url": paper.pdf_url,
        "abstract": paper.abstract,
        "citations": paper.citations,
        "verified": paper.verified,
        "verified_by": getattr(paper, "verified_by", None),
        "verification_notes": getattr(paper, "verification_notes", None),
        "approx_ratio": getattr(paper, "approx_ratio", None),
        "algorithm": getattr(paper, "algorithm", None),
        "analysis_method": getattr(paper, "analysis_method", None),
    }


@router.get("/{paper_id}")
def get_paper(paper_id: str, session: Session = Depends(get_session)):
    paper = session.get(Paper, paper_id)
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper_to_dict(paper)


@router.post("/upsert")
def upsert_papers_endpoint(
    papers: list[dict],
    session: Session = Depends(get_session)
):
    updated = crud_upsert(session, papers)
    return [paper_to_dict(p) for p in updated]
