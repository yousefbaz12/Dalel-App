from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the webdriver (make sure to have the appropriate webdriver for your browser installed)
driver = webdriver.Chrome("C:/Users/makan/OneDrive/Desktop/chromedriver-win64/chromedriver.exe")

# URL of the TripAdvisor page
url = "https://www.tripadvisor.com/Attractions-g294201-Activities-oa30-Cairo_Cairo_Governorate.html"
# Open the webpage
driver.get(url)

# Wait for the page to load (adjust the sleep time if needed)
time.sleep(5)

# Get the HTML content after dynamic rendering
html_content = driver.page_source

# Close the webdriver
driver.quit()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract information from the page
attraction_data = []

# Find all place elements
place_elements = soup.find_all("article", class_="GTuVU XJlaI")

for place_element in place_elements:
    # Extracting name
    name = place_element.find("div", class_="XfVdV o AIbhI").text.strip().split(".")[1].strip()

    # Extracting category
    category = place_element.find("div", class_="biGQs _P pZUbB hmDzD").text.strip()

    # Extracting URL
    url_element = place_element.find("a", class_="BUupS _R w _Z y M0 B0 Gm wSSLS")
    attraction_url = url_element.get('href', '') if url_element else ''

    # Append data to the list
    attraction_data.append({
        "Name": name,
        "Category": category,
        "URL": attraction_url
    })
