# Project Name: DJURSBO Web Scraper

## Overview
This project is a web scraping tool built using Scrapy, a powerful and flexible web scraping framework in Python. The purpose of this web scraper is to extract specific information from the website "djursbo.dk". The spider is designed to navigate the website, extract relevant data using CSS selectors and XPath expressions, and store the extracted information in a structured format.

## Requirements
Before running the DJURSBO web scraper, ensure you have the following installed:

- Python 3.x
- Scrapy library
- You can install Scrapy using pip:

```
pip install scrapy
```

## Usage
1. Clone the repository or download the code files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Execute the scraper using the following command:

```
scrapy runspider your_spider.py -o output.json
```

Replace your_spider.py with the filename of the Python file containing the web spider code.

The scraper will start processing the website "djursbo.dk" and extract the desired information. The scraped data will be saved in a file named output.json in JSON format. You can change the output format (e.g., CSV, XML) by modifying the file extension in the above command.

## Spider Details
The ForsideSpider class is the main spider defined in the code. It extends Scrapy's Spider class and contains the necessary logic to navigate the website and extract data.

## Spider Configuration
- name: The name of the spider, which will be used to identify it when running the scraper.

- allowed_domains: A list of domain names that the spider is allowed to crawl. In this case, it's set to ["djursbo.dk"].

- start_urls: A list of URLs from which the spider will start crawling. The spider will begin by visiting "https://djursbo.dk/".

## Data Extraction
- The spider uses CSS selectors and XPath expressions to extract the following data from each page it visits:

- description: Extracts text from paragraph (<p>) elements on the page.

- title: Extracts text from heading (<h>) elements on the page.

- order: Extracts text from <span> elements with a class name or attribute "pull-left" using XPath.

- price: Extracts text from <span> elements with a class name or attribute "pull-right" and "rend bg-binding" using XPath.

## Data Storage
The extracted data is stored in a structured format using Python dictionaries. For each item scraped from the website, a dictionary is created to hold the relevant information. The information includes:

1. page: The URL of the page from which the data was extracted.

2. description: The extracted description text.

3. title: The extracted title text.

4. order: The extracted order information.

5. price: The extracted price information.

## Output
The scraped information is yielded from the spider using the yield keyword. The data is then processed by Scrapy, and the output is saved in the specified format (output.json in this case).

## Customization
If you want to modify the data being extracted or add more scraping logic, you can do so by adjusting the CSS selectors and XPath expressions within the parse method of the ForsideSpider class. Additionally, you can change the output file format and name as per your requirements.
