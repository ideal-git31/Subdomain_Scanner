def prep_urls(wordlist, domain):
    words = wordlist.read().split()
    for word in words:
        yield f"https://{word}.{domain}"