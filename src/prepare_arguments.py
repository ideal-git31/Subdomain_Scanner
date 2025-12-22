from argparse import ArgumentParser, FileType

def prep_args():
    '''Prepare Arguments
      
         return:
             args(argparse.Namespace)
    '''
    parser = ArgumentParser(description="Sub-domain Scanner",
                            usage="%{prog}s example.com"
                            )
    parser.add_argument(
        metavar="Domain",
        dest="domain",
        help="Domain Name"
    )
    parser.add_argument(
        "-w", "--wordlist",
        dest="wordlist",
        type=FileType("r"),
        help="Lists of words or path of your word file",
        default="src/test_words.txt"
    )
    parser.add_argument(
        "-t", "--threads",
        dest="threads",
        type=int,
        help="Threads to use",
        default=500
    )
    parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="verbose output"
    )
    args = parser.parse_args()
    return args