import arxiv

search = arxiv.Search(
    query="climate change",
    max_results=10,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
    print(f"Title: ",result.title)
    print(f"Authors",result.authors)
    print(f"Summary: ",result.summary)
    print("\n")
