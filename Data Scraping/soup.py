from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
import requests
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Load the URLs from the CSV file
url_df = pd.read_csv("attraction_urls.csv")

driver = webdriver.Chrome(ChromeDriverManager().install())


def scrape_reviews(driver, max_reviews=100):
    reviews = []
    while len(reviews) < max_reviews:
        try:
            # Get the HTML content after dynamic rendering
            html_content = driver.page_source
            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract reviews from the current page
            reviews_list_div = soup.find("div", class_="LbPSX")
            if reviews_list_div:
                reviews_list = reviews_list_div.find_all("span", class_="yCeTE")
                reviews.extend([review.text.strip() for review in reviews_list])

            # Check for the next page button
            next_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next page"]')
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)  # Additional sleep for safety

        except NoSuchElementException:
            # No more "Next page" button, break out of the loop
            break

    return reviews[:max_reviews]


# Function to scrape detailed information for each attraction place
def scrape_attraction_details(website_url):
    # # Use requests to get initial HTML content
    # headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} response = requests.get(url,
    # headers=headers)

    # Open the webpage
    driver.get(website_url)

    # Wait for the page to load (adjust the sleep time if needed)
    time.sleep(10)

    # Get the HTML content after dynamic rendering
    html_content = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract information from the page
    attraction_place_details = {}

    # Place Name
    place_name_element = soup.find("h1", class_="biGQs _P fiohW eIegw")
    attraction_place_details["Place Name"] = place_name_element.text.strip() if place_name_element else None

    # Category
    category_element = soup.find("span", class_="eojVo")
    attraction_place_details["Category"] = category_element.text.strip() if category_element else None

    # Rating
    rating_element = soup.find("div", class_="biGQs _P fiohW hzzSG uuBRH")
    attraction_place_details["Rating"] = rating_element.text.strip() if rating_element else None

    # Address
    try:
        parent_div = driver.find_element_by_class_name("MJ")
        # Navigate to the child div containing the address
        child_div = parent_div.find_element_by_class_name("UikNM")
        # Navigate to the span element containing the address text
        span_element = child_div.find_element_by_tag_name("span")
        # Extract the text content if the span element is found
        attraction_place_details["Address"] = span_element.text.strip() if span_element else None

    except NoSuchElementException:
        # Handle case where address element is not found
        attraction_place_details["Address"] = None

    # About
    about_span = soup.find("span", class_="JguWG")
    attraction_place_details["About"] = about_span.text.strip() if about_span else None

    # Reviews List
    reviews_list = scrape_reviews(driver, 100)
    attraction_details["Reviews List"] = reviews_list
    return attraction_place_details


# Loop through each URL and scrape detailed information
all_attraction_details = []
for index, row in url_df.iterrows():
    url = "https://www.tripadvisor.com" + row["URL"]
    attraction_details = scrape_attraction_details(url)
    all_attraction_details.append(attraction_details)

# Close the webdriver
driver.quit()

# Create a DataFrame from the extracted data
attraction_details_df = pd.DataFrame(all_attraction_details)
# Save to CSV
attraction_details_df.to_csv("attractions.csv", index=False)
# Display the DataFrame
print(attraction_details_df)
