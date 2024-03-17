import requests  # Importing the requests library to make HTTP requests
from lxml import html  # Importing html from lxml to parse HTML
import json  # Importing the json library to work with JSON data
from PIL import Image  # Importing Image from PIL to open and show images
from io import BytesIO  # Importing BytesIO for byte stream operations
from PIL import UnidentifiedImageError  # Importing UnidentifiedImageError to catch errors related to unidentified images

class RCDLScraper:
    def __init__(self, captcha_url, data_url):
        self.captcha_url = captcha_url  # URL to fetch CAPTCHA image
        self.data_url = data_url  # URL to post data and scrape information

    def scrape_data(self, dl_number, dob):
        # Fetching CAPTCHA image and displaying it for user input
        response = requests.get(self.captcha_url)
        
        try:
            img = Image.open(BytesIO(response.content))  # Opening CAPTCHA image from the response
            img.show()  # Displaying the CAPTCHA image
        except UnidentifiedImageError:
            # Handling the error if the CAPTCHA image cannot be identified or opened
            return "Failed to identify CAPTCHA image. Please make sure the URL is correct and the response is an image."

        captcha_value = input("Please input the CAPTCHA value from the image: ")  # Prompting user to enter the CAPTCHA
        
        # Sending POST request with required form data including DL number, DOB, and CAPTCHA
        response = requests.post(self.data_url, data={'dlNumber': dl_number, 'dob': dob, 'captcha': captcha_value})

        if response.status_code == 200:
            # Parsing the HTML content if the response status code is 200 (OK)
            tree = html.fromstring(response.content)
            
            # Using XPath to extract specific pieces of information from the HTML
            # Each variable holds a specific piece of data scraped from the webpage
            # If the expected element is not found, a default value of "N/A" is assigned
            
            # Extracting the current status of the DL
            current_status_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[1]/tbody/tr[1]/td[2]/span/text()') 
            current_status = current_status_elements[0].strip() if current_status_elements else "N/A"
            
            # Extracting the holder's name
            holder_name_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[1]/tbody/tr[2]/td[2]/text()')
            holder_name = holder_name_elements[0].strip() if holder_name_elements else "N/A"
            
            # Extracting old/new DL number
            old_new_dl_no_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[1]/tbody/tr[3]/td[2]/text()')
            old_new_dl_no = old_new_dl_no_elements[0].strip() if old_new_dl_no_elements else "N/A"
            
            # Extracting source of data
            source_of_data_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[1]/tbody/tr[4]/td[2]/text()')
            source_of_data = source_of_data_elements[0].strip() if source_of_data_elements else "N/A"
            
            # Extracting the date of initial issue
            initial_issue_date_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[2]/tbody/tr[1]/td[2]/text()')
            initial_issue_date = initial_issue_date_elements[0].strip() if initial_issue_date_elements else "N/A"
            
            # Extracting the initial issuing office
            initial_issuing_office_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[2]/tbody/tr[2]/td[2]/text()')
            initial_issuing_office = initial_issuing_office_elements[0].strip() if initial_issuing_office_elements else "N/A"
            
            # Extracting the date of the last endorsement
            last_endorsed_date_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[3]/tbody/tr[1]/td[2]/text()')
            last_endorsed_date = last_endorsed_date_elements[0].strip() if last_endorsed_date_elements else "N/A"
            
            # Extracting the office of the last endorsement
            last_endorsed_office_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[3]/tbody/tr[2]/td[2]/text()')
            last_endorsed_office = last_endorsed_office_elements[0].strip() if last_endorsed_office_elements else "N/A"


            # Extracting driving license validity details
            # Extracting driving license validity details for non-transport
            non_transport_valid_from_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[4]/tbody/tr[1]/td[2]/text()')
            non_transport_valid_from = non_transport_valid_from_elements[0].strip() if non_transport_valid_from_elements else "N/A"

            non_transport_valid_upto_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[4]/tbody/tr[1]/td[3]/text()')
            non_transport_valid_upto = non_transport_valid_upto_elements[0].strip() if non_transport_valid_upto_elements else "N/A"

            # Extracting driving license validity details for transport
            transport_valid_from_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[4]/tbody/tr[2]/td[2]/text()')
            transport_valid_from = transport_valid_from_elements[0].strip() if transport_valid_from_elements else "N/A"

            transport_valid_upto_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[4]/tbody/tr[2]/td[3]/text()')
            transport_valid_upto = transport_valid_upto_elements[0].strip() if transport_valid_upto_elements else "N/A"

            
            # Placeholder XPaths for hazardous and hill validity, to be replaced with actual XPaths
            # These fields are expected to hold the validity of certain special permissions
            hazardous_valid_till_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[5]/tbody/tr/td[2]/text()')
            hazardous_valid_till = hazardous_valid_till_elements[0].strip() if hazardous_valid_till_elements else "N/A"

            hill_valid_till_elements = tree.xpath('//*[@id="form_rcdl:j_idt63"]/table[5]/tbody/tr/td[4]/text()')
            hill_valid_till = hill_valid_till_elements[0].strip() if hill_valid_till_elements else "N/A"

            
            # Extracting class of vehicle details. The actual XPath needs to be specified
            cov_elements = tree.xpath('XPATH_EXPRESSION_FOR_COV_ROWS')
            class_of_vehicle_details = []
            for elem in cov_elements:
                # Looping through each element to extract details
                # These XPaths are placeholders and should be replaced with actual values to extract class of vehicle details
                cov_category = elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[1]/text()')[0].strip() if elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[1]/text()') else "N/A"
                class_of_vehicle = elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[2]/text()')[0].strip() if elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[2]/text()') else "N/A"
                cov_issue_date = elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[3]/text()')[0].strip() if elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/tr[1]/td[3]/text()') else "N/A"
                vehicle_category = elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/text()')[0].strip() if elem.xpath('//*[@id="form_rcdl:j_idt117_data"]/text()') else class_of_vehicle

                class_of_vehicle_details.append({
                    "cov_category": cov_category,
                    "class_of_vehicle": vehicle_category,  # Using vehicle_category as it could represent either class_of_vehicle or a specific vehicle category
                    "cov_issue_date": cov_issue_date,
                })


            # Organizing the scraped data into a structured JSON format
            data = {
                "current_status": current_status,
                "holder_name": holder_name,
                "old_new_dl_no": old_new_dl_no,
                "source_of_data": source_of_data,
                "initial_issue_date": initial_issue_date,
                "initial_issuing_office": initial_issuing_office,
                "last_endorsed_date": last_endorsed_date,
                "last_endorsed_office": last_endorsed_office,
                "driving_license_validity_details": {
                    "non_transport": {
                        "valid_from": non_transport_valid_from,
                        "valid_upto": non_transport_valid_upto
                    },
                    "transport": {
                        "valid_from": transport_valid_from,
                        "valid_upto": transport_valid_upto
                    }
                },
                "hazardous_valid_till": hazardous_valid_till,
                "hill_valid_till": hill_valid_till,
                "class_of_vehicle_details": class_of_vehicle_details,
            }
            return json.dumps(data, indent=4)  # Returning the organized data as a JSON string
        else:
            return "Failed to retrieve data from the website."  # Returning a message if the POST request did not succeed

if __name__ == "__main__":
    captcha_url = "https://parivahan.gov.in/rcdlstatus/DispplayCaptcha?txtp_cd=1&bkgp_cd=2&noise_cd=2&gimp_cd=3&txtp_length=5&pfdrid_c=true?-1207445462&pfdrid_c=true"
    data_url = "https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
    scraper = RCDLScraper(captcha_url, data_url)
    dl_number = input("Please input DL number: ")
    dob = input("Please input DOB (DD-MM-YYYY): ")
    scraped_data = scraper.scrape_data(dl_number, dob)
    print(scraped_data)
