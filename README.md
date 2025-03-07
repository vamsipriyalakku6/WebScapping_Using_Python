# WebScapping_Using_Python
# Web Scraping Quotes from http://quotes.toscrape.com/

## Overview
This Python script scrapes quotes and their respective authors from the website **http://quotes.toscrape.com/** using the **BeautifulSoup** library. The extracted data is then stored in a CSV file.

## Features
- Fetches quotes and authors from the website
- Parses HTML content using **BeautifulSoup**
- Stores the extracted data in a **Pandas DataFrame**
- Saves the data as a CSV file
- Downloads the CSV file (for Google Colab users)

## Prerequisites
Make sure you have the following dependencies installed:
```bash
pip install numpy pandas requests beautifulsoup4

## **Usage**
1. Run the script in your preferred Python environment (Google Colab, Jupyter Notebook, or local machine).
2. The first few rows of the extracted quotes and authors will be displayed in the console.
3. The script saves the extracted data as `quotes.csv` in the working directory.
4. If running in Google Colab, the script will automatically download the CSV file.


## **Code Explanation**
- The script sends a request to the webpage using `requests.get()`.
- It parses the HTML content using `BeautifulSoup` with the `html.parser`.
- Quotes and authors are extracted using CSS selectors via the `find_all` method.
- The extracted data is stored in a Pandas `DataFrame` and then saved as a CSV file.
- Error handling is included to check if the webpage loads successfully.

## Example Output (DataFrame)

| Quote                                      | Author         |
|--------------------------------------------|---------------|
| "The greatest glory in living..."         | Nelson Mandela |
| "The way to get started is to..."         | Walt Disney   |

