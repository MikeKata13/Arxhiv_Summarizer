import arxiv

search = arxiv.Search(
    query="climate",
    max_results=2,
    sort_by=arxiv.SortCriterion.SubmittedDate,
    sort_order=arxiv.SortOrder.Descending
)

with open("results.txt", "w", encoding="utf-8") as file:
    for result in search.results():
        result.download_pdf()
        authors = ", ".join([author.name for author in result.authors])
        file.write(f"ID: {result.entry_id}\n")
        file.write(f"Published: {result.published}\n")
        file.write(f"DOI: {result.doi}\n")
        file.write(f"Title: {result.title}\n")
        file.write(f"Authors: {authors}\n")
        file.write(f"Summary: {result.summary}\n")
        file.write("\n")

print("Fetching Completed Successfully!")