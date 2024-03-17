# Parivahan_Sewa_Scraper

RCDL Scraper
The RCDL (Regional Driving License) Scraper is a Python script designed to scrape driver's license details from a specific website. It fetches information such as the current status of the driver's license, holder's name, old/new DL number, date of initial issue, date of the last endorsement, driving license validity details, class of vehicle details, and more.

Features
Fetches CAPTCHA image and prompts the user to enter the CAPTCHA value.
Sends a POST request with DL number, DOB, and CAPTCHA value to scrape data from the website.
Parses the HTML content using XPath to extract specific pieces of information.
Organizes the scraped data into a structured JSON format.
Provides error handling for cases such as an unidentified CAPTCHA image or failed data retrieval from the website.
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/rcdl-scraper.git
Navigate to the project directory:

bash
Copy code
cd rcdl-scraper
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the script:

bash
Copy code
python rcdl_scraper.py
Follow the prompts to input the DL number and DOB (date of birth).

Once the script finishes execution, it will display the scraped data in JSON format.

Configuration
Before running the script, ensure the following:

Verify that the URLs for CAPTCHA image and data retrieval are correct (captcha_url and data_url variables in the script).
Adjust the XPath expressions (XPATH_EXPRESSION_FOR_COV_ROWS, etc.) to match the structure of the HTML page being scraped.
Requirements
Python 3.x
requests
lxml
Pillow (PIL)