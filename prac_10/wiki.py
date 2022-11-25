import wikipedia

print("Brodie's Wiki page search thingy")
search_phrase = input("Search phrase: ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        title = page.title
        summary = wikipedia.summary(search_phrase)
        url = page.url
        print(f"Page tile: {title}\n")
        print("Summary:")
        print(summary)
        print(f"URL: {url}\n")
    except wikipedia.exceptions.PageError:
        print("Invalid page, please try again.")
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation error, please try again.")
    search_phrase = input("Search phrase: ")
