import requests
from .sub_domains import subdomains
from .prepare_arguments import prep_args

def testing_subdomain(url_queue):
    arguments = prep_args()
    
    while not url_queue.empty():
        try:
            url = url_queue.get()
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                subdomains.append(url)
                if arguments.verbose:
                    print(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            continue
        except StopIteration:
            break 
