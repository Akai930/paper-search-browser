# utils/paper_controller.py
from api.paper_api import search_papers_semantic
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class PaperFields:
    title: str
    abstract: Optional[str]
    url: str
    paperId: str
    # 必要なら関連度や大学などの属性を追加してもよい

@dataclass
class PaperResult:
    paper: List[PaperFields] = field(default_factory=list)

def semantic_controller(query: str, year_range: tuple, limit: int = 10):
    year_from, year_to = year_range
    data = search_papers_semantic(query, year_from=year_from, year_to=year_to, limit=limit)
    papers = PaperResult()
    for d in data:
        paper = PaperFields(
            title=d["title"],
            abstract=d.get("abstract"),
            url=d["url"],
            paperId=d["paperId"]
        )
        papers.paper.append(paper)
    return papers

if __name__ == "__main__":
    query = "Time-Series Gene Expression Data Imputation"
    data = semantic_controller(query, (2020, 2025))
    print("title:", data.paper[0].title)
    print("abstract:", data.paper[0].abstract)
