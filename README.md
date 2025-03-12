```
# Simple Website Crawler

A lightweight Python-based website crawler that traverses a given website, extracts all internal links, and optionally saves them to an output file. It’s designed to explore pages within the same domain using a breadth-first search approach.

---

## Features

- **Crawling within Domain:** The crawler only follows links that share the same domain as the provided base URL.
- **Link Extraction:** Utilizes [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to parse HTML and extract absolute URLs from `<a>` tags.
- **Breadth-First Search:** Implements a BFS algorithm to visit pages in a systematic manner, ensuring every reachable link is processed.
- **Progress Feedback:** Displays processing status on the console, showing the current URL, count of visited links, and the queue size.
- **Output Options:** Either prints the discovered links to the console or writes them to a specified output file.
- **Stylish Banner:** Features an ASCII art banner that displays when the crawler starts.

---

## Requirements

- **Python 3.x**
- **Required Packages:**
  - `requests`
  - `beautifulsoup4`

You can install the necessary packages using pip:

```bash
pip install requests beautifulsoup4
```

---

## Usage

Run the crawler from the command line by specifying the base URL with the `-u` or `--url` option. Optionally, use the `-o` or `--output` option to save the results to a file.

### Command Examples

- **Crawl a Website and Display Links:**

  ```bash
  ./crawler.py -u https://example.com
  ```

- **Crawl a Website and Save Links to a File:**

  ```bash
  ./crawler.py -u https://example.com -o links.txt
  ```

---

## Code Structure Overview

- **`get_links(url)` Function:**
  - **Purpose:** Downloads HTML content from the specified URL and extracts all hyperlinks.
  - **Process:** 
    - Performs an HTTP GET request using the `requests` module.
    - Parses the HTML content with BeautifulSoup.
    - Converts any relative links to absolute URLs using `urljoin`.
    - Returns a list of valid links found on the page.

- **`crawl_site(start_url)` Function:**
  - **Purpose:** Crawls the website starting from `start_url` by traversing links within the same domain.
  - **Process:**
    - Initializes a queue with the starting URL and a set to track visited URLs.
    - Uses a breadth-first search (BFS) strategy to visit and process each page.
    - Prints the progress, including the current URL being processed, total visited count, and queue length.
    - Collects all unique internal links.

- **`main()` Function:**
  - **Purpose:** Handles argument parsing, displays the ASCII art banner, and triggers the crawling process.
  - **Process:**
    - Uses `argparse` to obtain command-line parameters.
    - Calls the `crawl_site` function to begin crawling.
    - Outputs the results either to the console or to a specified file based on user input.

---

## Limitations

- **Domain Restriction:** The crawler only follows links within the same domain as the starting URL. It will ignore external links.
- **Dynamic Content:** It does not execute JavaScript; thus, links generated dynamically (via JavaScript) will not be processed.
- **Error Handling:** Basic error handling is implemented for network issues and HTTP errors.

---

## License

This project is licensed under the MIT License.
```