from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

print("Test started...")

# Set up browser
driver = webdriver.Chrome()

# Open the local login.html file
file_path = f"file:///{os.getcwd()}/login.html"
driver.get(file_path)

time.sleep(2)  # Let the page load

try:
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")
    
    # Fill in dummy credentials
    email_field.send_keys("test@example.com")
    password_field.send_keys("password123")
    
    # Click login
    login_button.click()
    
    print("Test Passed: Login form interacted successfully.")
except Exception as e:
    print("Test Failed:", e)

driver.quit()
print("Test finished.")
