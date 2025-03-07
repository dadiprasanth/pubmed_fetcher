import requests
import xmltodict
from typing import List, Dict

PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetch research papers from PubMed API."""
    
    # Step 1: Get Paper IDs
    search_url = f"{PUBMED_BASE_URL}/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()
    pubmed_ids = search_data.get("esearchresult", {}).get("idlist", [])

    # Step 2: Fetch Details for Each Paper
    papers = []
    for pubmed_id in pubmed_ids:
        fetch_url = f"{PUBMED_BASE_URL}/efetch.fcgi"
        fetch_params = {"db": "pubmed", "id": pubmed_id, "retmode": "xml"}
        fetch_response = requests.get(fetch_url, params=fetch_params)

        data = xmltodict.parse(fetch_response.content)
        article = data.get("PubmedArticleSet", {}).get("PubmedArticle", {})

        title = article.get("MedlineCitation", {}).get("Article", {}).get("ArticleTitle", "N/A")
        pub_date = article.get("MedlineCitation", {}).get("Article", {}).get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "N/A")

        # Extract Authors and Affiliations
        author_list = article.get("MedlineCitation", {}).get("Article", {}).get("AuthorList", {}).get("Author", [])
        authors = []
        if isinstance(author_list, list):
            for author in author_list:
                name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                affiliation_info = author.get("AffiliationInfo")

                # If affiliation_info is a list, get the first item; if it's a dict, use it directly
                if isinstance(affiliation_info, list) and len(affiliation_info) > 0:
                    affiliation = affiliation_info[0].get("Affiliation", "")
                elif isinstance(affiliation_info, dict):
                    affiliation = affiliation_info.get("Affiliation", "")
                else:
                    affiliation = ""

                authors.append({"name": name, "affiliation": affiliation})

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Authors": authors
        })

    return papers
