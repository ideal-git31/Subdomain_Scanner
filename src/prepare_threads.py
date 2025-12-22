from threading import Thread
from .check_subdomain import testing_subdomain

def prep_thread(url_queue, threads):
    thread_list = []
    for _ in range(threads):
       thread_list.append(Thread(target = testing_subdomain, args=(url_queue, ), daemon=True))

    for thread in thread_list:
        thread.start()   

    for thread in thread_list:
        thread.join()     

