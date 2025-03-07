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
## Usage
Run the script: Execute the Python script in your preferred environment (Google Colab, Jupyter Notebook, or local machine).
Check output: The first few rows of the extracted quotes and authors will be displayed in the console.
CSV file generation:The script saves the extracted data as quotes.csv in the working directory.
Download CSV (only in Google Colab): If running in Colab, the script will automatically download the CSV file.
##Code Explanation
The script requests the webpage content using requests.get().
The HTML is parsed with BeautifulSoup (html.parser).
Quotes and authors are extracted using CSS selectors (find_all method).
Data is stored in a Pandas DataFrame and saved as a CSV file.
Includes error handling to check if the webpage loads successfully.
##Example Output (DataFrame)
Quote	                            Author
"The greatest glory in living..."	Nelson Mandela
"The way to get started is to..."	Walt Disney
