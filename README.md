# Web Data Scraper for Flipkart Mobile Phones

This project is a Python-based web scraper designed to collect data from the Flipkart website for Apple mobile phones. Using the `BeautifulSoup` library, the scraper fetches details like product names, prices, specifications, ratings, number of reviews, images, and links, then stores them in a structured CSV format for further analysis.

## Features

- **Data Collection**: Scrapes key details about mobile phones from Flipkart such as names, prices, specifications, ratings, number of reviews, images, and product links.
- **CSV Export**: The collected data is stored in a structured format in a CSV file (`Scraped_Data.csv`).
- **Easy to Use**: The scraper is straightforward to run and can be customized for different categories on Flipkart.

## Libraries Used

- `BeautifulSoup`: For parsing HTML and scraping the data.
- `requests`: For sending HTTP requests to the Flipkart website.
- `pandas`: For organizing and exporting the data into a CSV file.

## How It Works

1. **Requesting Data**: Sends an HTTP request to the Flipkart search page for Apple mobiles.
2. **Parsing HTML**: BeautifulSoup parses the HTML content, identifying relevant product information such as names, prices, and reviews.
3. **Data Extraction**: Extracts key details like names, prices, specifications, ratings, number of reviews, images, and links for each mobile product.
4. **Data Structuring**: Organizes the scraped data into a pandas DataFrame and ensures each list has the same length by truncating or padding with `None`.
5. **Export to CSV**: The data is saved as `Scraped_Data.csv` for further use.

## Prerequisites

- Python 3.x
- Install the required libraries by running:

  ```bash
  pip install requests beautifulsoup4 pandas
  ```
## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/web-data-scraper.git
   cd web-data-scraper
   ```

2. Run the script:

   ```bash
   python scraper.py
   ```

3. The scraped data will be saved to a file named `Scraped_Data.csv` in the project directory.

## Example Output

Here is an example of the first few rows of the scraped data:

| Names            | Prices  | Specifications              | Ratings | Number of Reviews | Images         | Links                           |
|------------------|---------|-----------------------------|---------|-------------------|----------------|----------------------------------|
| iPhone 12        | ₹79,999 | 128 GB, Dual Camera, etc.    | 4.5     | 10,234 Ratings    | image_url_1    | https://www.flipkart.com/xyz...  |
| iPhone 13        | ₹89,999 | 256 GB, OLED Display, etc.   | 4.8     | 15,764 Ratings    | image_url_2    | https://www.flipkart.com/abc...  |

## Customization

- You can modify the search URL to scrape data for different categories or products on Flipkart.
- The code is flexible to accommodate new fields or data points if you want to extract more details.

## Contact 
ashek9837@gmail.com



