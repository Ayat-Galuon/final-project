# import pytest
# import time
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# class TestDefaultSuite():
#   def setup_method(self, method):
#     self.driver = webdriver.Chrome()
#     self.driver.get("http://127.0.0.1:8000/#/")
#     self.driver.set_window_size(1070, 660)
#     self.vars = {} 
  
#   def teardown_method(self, method):
#     self.driver.quit()
   
  
#   def test_search_button(self):
#     """
#     This test verifies that the search functionality works correctly by searching for 'mug'.
#     """
#     # Enter 'mug' in the search bar and click the search button.
#     self.driver.find_element(By.NAME, "q").send_keys("mug")
#     self.driver.find_element(By.CSS_SELECTOR, ".p-2").click()
#     assert self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(2) strong").text == "Roronoa Zoro Mug"

# def test_login(self):
#     """
#     This test including logging out, logging back in, 
#     navigating to a product card, and verifying the username is displayed correctly upon login.
#     """
#     # Click on the username dropdown and log out.
#     self.driver.find_element(By.ID, "username").click() #
#     self.driver.find_element(By.LINK_TEXT, "Logout").click() #

#     self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     self.driver.find_element(By.ID, "email").send_keys("ayatabug@gmail.com")
#     self.driver.find_element(By.ID, "password").send_keys("1234ayat")
#     self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     element = self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(2) .card-img")
#     actions = ActionChains(self.driver)
#     actions.move_to_element(element).perform()
#     assert self.driver.find_element(By.ID, "username").text == "AYATABUG@GMAIL.COM"

# # def test_teste2e(self):
# #     self.driver.get("http://127.0.0.1:8000#/")  # Open the website
# #     self.driver.set_window_size(1296, 688)    # Set window size
    
# #     # Check if the "Logout" link is present (indicating the user is logged in)
# #     try:
# #         logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
# #         # If the "Logout" button is found, click it to log out
# #         logout_button.click()
# #         print("Logged out successfully")
# #     except:
# #         # If the "Logout" button is not found, continue with the test
# #         print("No user logged in. Continuing with the test.")

# #     # Perform login actions (continue with the test flow)
# #     self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
# #     self.driver.find_element(By.ID, "email").send_keys("ayatabug@gmail.com")
# #     self.driver.find_element(By.ID, "password").send_keys("1234ayat")
# #     self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()

# #     # Interact with the next element and assert the username is displayed correctly
# #     element = self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(2) .card-img")
# #     actions = ActionChains(self.driver)
# #     actions.move_to_element(element).perform()

# #     # Verify the username after login
# #     assert self.driver.find_element(By.ID, "username").text == "AYATABUG@GMAIL.COM"
  


# def test_order_summary(self):
#     """
#     This test simulates the user interaction of navigating through items.
#     """
#     self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(3) .card-img").click()
#     #self.driver.execute_script("window.scrollTo(0,134)")
#     self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
#     self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
#     self.driver.find_element(By.ID, "address").click()
#     self.driver.find_element(By.ID, "address").send_keys("123 Sunset Blvd")
#     self.driver.find_element(By.ID, "city").send_keys("Los Angeles")
#     self.driver.find_element(By.ID, "postalCode").send_keys("90001")
#     self.driver.find_element(By.ID, "country").send_keys("USA")
#     self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
#     self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
#     assert self.driver.find_element(By.CSS_SELECTOR, ".card .list-group-item:nth-child(1)").text == "ORDER SUMMARY"
    

  
# def test_navigation_back_to_homepg(self):
#     """
#     This test verifies that the 'Go Back' button on an item's detail page
#     successfully navigates the user back to the Home page section.
#     """
#     self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(1) .card-img").click()
#     self.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()
#     assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "LATEST PRODUCTS"
    
