import argparse
import pandas as pd
from pubmed_fetcher.fetch import fetch_pubmed_papers
from pubmed_fetcher.filter import filter_non_academic_authors

def main():
    parser = argparse.ArgumentParser(
        description="""
        PubMed Fetcher: A command-line tool to fetch research papers from PubMed 
        and filter out non-academic authors.

        Usage Examples:
        ---------------
        **base command is  
        
        -->get-papers-list 
                        or
        -->get-paper-list.bat
                        or
        --> python -m pubmed_fetcher.cli
        **
        1. Fetch papers for a query and print to console:
           baseCommand "medical term" 
           Eg: get-papers-list "covid vaccine"

        2. Save results to a CSV file:
           baseCommand "medical term" -f filename.csv
              Eg: get-papers-list "cancer treatment" -f results.csv
           

        3. Enable debug mode for additional information:
            baseCommand "medical term" -d
           Eg: python -m pubmed_fetcher.cli "heart disease" -d

        4. Combine debug mode and file output:
        baseCommand "medical term" -f filename.csv -d
           python -m pubmed_fetcher.cli "diabetes research" -d -f diabetes_results.csv
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    
    parser.add_argument(
        "-f", "--file", type=str, 
        help="Specify the filename to save results as a CSV. If not provided, prints to console."
    )
    
    parser.add_argument(
        "-d", "--debug", action="store_true", 
        help="Enable debug mode to print additional execution details."
    )

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Fetching papers for query: {args.query}")

    # Fetch papers
    papers = fetch_pubmed_papers(args.query, max_results=100)

    if args.debug:
        print(f"[DEBUG] {len(papers)} papers fetched.")

    # Filter non-academic authors
    filtered_papers = filter_non_academic_authors(papers)

    if args.debug:
        print(f"[DEBUG] {len(filtered_papers)} papers after filtering.")

    # Convert to DataFrame
    df = pd.DataFrame(filtered_papers)

    # Save to file or print
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df.to_string(index=False))  # Print in a readable format

if __name__ == "__main__":
    main()
