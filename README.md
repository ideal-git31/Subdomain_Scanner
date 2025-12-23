# Subdomain Scanner

## Project Overview

It is a python based command line tool to scan the working subdomains of a application or website.
It is easy to use and fast tool.


## Features

1. Command Line Interface.
2. Easy to use and fast.
3. Multiple Flags for different outputs or different operations

       -V or --verbose (for verbose output)
       -t or --threads (threads to use)
       -w or --wordlist (List of words or path of word file)

## Run

1. Clone the whole project into your system.
2. Then run the following comand:

       python3 main.py example.com
   You can play with it using different other flags.

## Project Structure

    Subdomain_Scanner/
    |
    |--- src/
    |     |--- prepare_arguments.py    # Prepare command line arguments
    |     |--- prepare_subdomains.py   # Prepare subdomains to scan
    |     |--- prepare_threads.py      # Prepare threads for parallel scanning
    |     |--- sub_domains.py          # Store all the working Subdomains
    |     |--- check_subdomain.py      # Scans the subdomains
    |     |--- test_words.txt          # Default file of words to prepare subdomains
    |
    |--- main.py                       # Parent file to run all functions and print working subdomains
    |--- README.md
