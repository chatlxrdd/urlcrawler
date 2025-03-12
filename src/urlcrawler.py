#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def get_links(url):
    """
    Downloads and parses the HTML content of 'url',
    returns a list of all <a> tag absolute URLs found on the page.
    """
    links = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        # Any network, SSL, or HTTP status error will be caught here
        return links

    soup = BeautifulSoup(response.text, 'html.parser')

    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            # Convert relative link to absolute
            absolute_link = urljoin(url, href)
            links.append(absolute_link)

    return links

def crawl_site(start_url):
    parsed_start = urlparse(start_url)
    base_domain = parsed_start.netloc

    queue = deque([start_url])
    visited = set([start_url])

    while queue:
        current_url = queue.popleft()
        print(f"Processing: {current_url} | Visited: {len(visited)} | Queue: {len(queue)}")
        found_links = get_links(current_url)

        for link in found_links:
            parsed_link = urlparse(link)
            if parsed_link.netloc == base_domain and parsed_link.scheme in ('http', 'https'):
                if link not in visited:
                    visited.add(link)
                    queue.append(link)

    return visited

def main():
    RED = "\033[31m"
    RESET = "\033[0m"
    banner = r"""      ___           ___           ___                ___           ___           ___           ___           ___       ___           ___     
     /\__\         /\  \         /\__\              /\  \         /\  \         /\  \         /\__\         /\__\     /\  \         /\  \    
    /:/  /        /::\  \       /:/  /             /::\  \       /::\  \       /::\  \       /:/ _/_       /:/  /    /::\  \       /::\  \   
   /:/  /        /:/\:\  \     /:/  /             /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/ /\__\     /:/  /    /:/\:\  \     /:/\:\  \  
  /:/  /  ___   /::\~\:\  \   /:/  /             /:/  \:\  \   /::\~\:\  \   /::\~\:\  \   /:/ /:/ _/_   /:/  /    /::\~\:\  \   /::\~\:\  \ 
 /:/__/  /\__\ /:/\:\ \:\__\ /:/__/             /:/__/ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/_/:/ /\__\ /:/__/    /:/\:\ \:\__\ /:/\:\ \:\__\
 \:\  \ /:/  / \/_|::\/:/  / \:\  \             \:\  \  \/__/ \/_|::\/:/  / \/__\:\/:/  / \:\/:/ /:/  / \:\  \    \:\~\:\ \/__/ \/_|::\/:/  /
  \:\  /:/  /     |:|::/  /   \:\  \             \:\  \          |:|::/  /       \::/  /   \::/_/:/  /   \:\  \    \:\ \:\__\      |:|::/  / 
   \:\/:/  /      |:|\/__/     \:\  \             \:\  \         |:|\/__/        /:/  /     \:\/:/  /     \:\  \    \:\ \/__/      |:|\/__/  
    \::/  /       |:|  |        \:\__\             \:\__\        |:|  |         /:/  /       \::/  /       \:\__\    \:\__\        |:|  |    
     \/__/         \|__|         \/__/              \/__/         \|__|         \/__/         \/__/         \/__/     \/__/         \|__|    """
    print(RED + banner + RESET)

    parser = argparse.ArgumentParser(description='Simple Website Crawler')
    parser.add_argument('-u', '--url', required=True, help='Base URL to crawl')
    parser.add_argument('-o', '--output', help='Output file to store links (optional)')
    args = parser.parse_args()

    start_url = args.url.strip()
    all_links = crawl_site(start_url)

    # Output the found links
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for link in sorted(all_links):
                f.write(link + '\n')
        print(f"[+] Crawl complete. {len(all_links)} links saved to {args.output}")
    else:
        print(f"[+] Found {len(all_links)} links on {start_url}:\n")
        for link in sorted(all_links):
            print(link)

if __name__ == "__main__":
    main()
