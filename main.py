from time import time
from src.prepare_arguments import prep_args
from src.prepare_subdomains import prep_urls
from src.prepare_threads import prep_thread
from src.check_subdomain import testing_subdomain
from src.sub_domains import subdomains
from queue import Queue

def main():
    arguments = prep_args()
    urls = prep_urls(arguments.wordlist, arguments.domain)
    url_queue = Queue()
    for url in urls:
       url_queue.put(url)
    prep_thread(url_queue, arguments.threads)
    print("Sub-domains found - ","\n".join(i for i in subdomains))



if __name__ == "__main__":
    main()