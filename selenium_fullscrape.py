from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")   
chrome_options.add_argument("--disable-gpu")   
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox for headless mode (required in some environments)

# Set up proxy  
proxy = "http://your-proxy-server:port"
chrome_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://example.com"

driver.get(url)

# Wait for the body element to be loaded (wait for 20 seconds max)
body_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)
# Get the text from the body tag
text = body_element.text

# Print the extracted text
print(text)

driver.quit()
