"""
This file is used to test the functionalities in the browser.
It will use Selenium.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class MySeleniumTests(StaticLiveServerTestCase):
    """
    This class provides a configuration and a set of actions to
    simulate the behaviour of a human user.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30000)

    def test_browser(self):
        """
        This contains the list of actions to perform in the browser,
         the order in which Selenium executes them and the assertions to test.
        """
        # First we go full screen
        self.driver.maximize_window()
        # Then we go on the website
        self.driver.get("http://localhost:8000/foodfacts/")
        self.assertIn(
            "GRAS", self.driver.find_element("id", "main_title").text)

        # Then we go on the sigin page
        self.driver.get("http://localhost:8000/roles/signin/")
        self.assertIn(
            "CONNEXION", self.driver.find_element(By.TAG_NAME, "h1").text)
        # We sign in
        signin_email = self.driver.find_element("name", "email")
        signin_email.send_keys("monami@gmail.com")
        signin_password = self.driver.find_element("name", "password")
        signin_password.send_keys("Niam1989")
        self.driver.find_element("xpath", '//input[@type="submit"]').click()

        self.assertIn(
            "Editez", self.driver.find_element("id", "sub_title").text
        )

        # We look for a product
        search_navbar_input = self.driver.find_element("id", "nav_input")
        self.driver.execute_script("document.getElementById('nav_input').value = 'Biscuit'")
        search_navbar_input.submit()

        self.assertIn(
            "biscuit", self.driver.find_element("id", "product_found").text
        )

        # We go to the product's page
        self.driver.find_element("id", f"details{1}").click()

        self.assertIn(
            "Nutriscore", self.driver.find_element("id", "nutriscore_h3").text
        )
        # We go to its Open Food Facts page
        self.driver.execute_script("document.getElementById('offacts_link').click()")

        # We go back to the results
        self.driver.execute_script("window.history.go(-2)")
        # We add the products to our favourites
        self.driver.find_elements(By.CLASS_NAME, "add_to_fav")[0].click()
        # We go to the favourites page
        self.driver.get("http://localhost:8000/roles/favourites")
        self.assertIn(
            "VOS FAVORIS", self.driver.find_element(By.TAG_NAME,"h1").text
        )
        # We unlike the product and go back to th results
        self.driver.find_elements(By.CLASS_NAME, "unlike_form")[0].submit()
        self.driver.execute_script("window.history.go(-2)")
        # This is because of the browser's cache
        self.driver.refresh()
        # We log out
        self.driver.get("http://localhost:8000/roles/signin/")
        # submit
        self.assertIn(
            "CONNEXION", self.driver.find_element(By.TAG_NAME,"h1").text
        )

        self.driver.execute_script("document.getElementById('logout_btn').click()")
        
        # Reset password
        # Get the reset password page
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("http://localhost:8000/roles/reset_password/")
        
        self.assertIn(
            "Forgot your password? Please enter the email address", self.driver.find_element(By.TAG_NAME, "h3").text
        )
        
        # Provide your email address
        #wait.until(EC.element_to_be_clickable(("id", "id_email"))).send_keys("test@test.com").click()
        
        reset_input_field = self.driver.find_element("name", "email")

        reset_input_field.send_keys('test@test.com')
        #self.driver.execute_script("document.getElementById('id_email').value = 'test@test.com'")
        reset_input_field.submit()
        
        # The email has been sent
        self.driver.get("http://localhost:8000/roles/reset_password_sent/")
        self.assertIn(
            "Password reset sent", self.driver.find_element(By.TAG_NAME, "h1").text
        )

        # Actual reset form
        self.driver.get("http://localhost:8000/roles/reset/MQ/bsbney-d5cf45d18708cbc1a0618a020152c3a7")
        self.assertIn(
            "Change password", self.driver.find_element(By.TAG_NAME, "h3").text
        )

        # Password has been updated
        self.driver.get("http://localhost:8000/roles/reset_password_complete/")
        self.assertIn(
            "Password reset complete", self.driver.find_element(By.TAG_NAME, "h1").text
        )
        
        # We close the browser.
        self.driver.close()
