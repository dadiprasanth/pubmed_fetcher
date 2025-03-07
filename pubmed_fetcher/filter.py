from typing import List, Dict

# Keywords that indicate academic institutions
ACADEMIC_KEYWORDS = ["university", "college", "institute", "school", "hospital", "research", "center", "academy"]

def is_non_academic(affiliation: str) -> bool:
    """Check if an author is affiliated with a non-academic institution."""
    if not affiliation:
        return False
    return not any(keyword in affiliation.lower() for keyword in ACADEMIC_KEYWORDS)

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Extract non-academic authors and their company affiliations."""
    filtered_papers = []

    for paper in papers:
        non_academic_authors = [
            author for author in paper["Authors"] if is_non_academic(author["affiliation"])
        ]

        if non_academic_authors:
            filtered_papers.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Authors": [author["name"] for author in non_academic_authors],
                "Company Affiliation": [author["affiliation"] for author in non_academic_authors],
            })

    return filtered_papers
