from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.demoqa.selenium.base_page import BasePage
# from pages.demoqa.selenium.elements_page import ElementsPage → researvar para La Paz page 
from config.config import  BASE_URL

'''
Landing page is a class that:
- inherets methods from base page 
- stores locators 
- calls methods for actions over elements
- 
'''

logger = get_logger(__name__)

# Crear metodo LandingPage que hereda de BasePage 
class LandingPage(BasePage):

    ## Locators: 
    lapaz_option = (By.NAME, "59")
    cochabamba_option = (By.NAME, "61")
    santacruz_option = (By.NAME, "60")
    sucre_option = (By.NAME, "181")
    otros_option = (By.NAME, "62")
    # forms_option = (By.XPATH, "//h5[text()='Forms']")    
    # alerts_frames_windows_option = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")    
    # sucre_option = (By.XPATH, "")
    # otros_option = (By.XPATH, "")

    # go to base URL    
    def __init__(self, driver, environment):
        super().__init__(driver)        
        self.url = BASE_URL[environment]
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    # lapaz option
    def click_lapaz_option(self):        
        self.click_element(self.lapaz_option)
        # return ElementsPage(self.driver)
    
    def get_lapaz_option(self):
        return self.find_element(self.lapaz_option)
    
    # cochabamba option
    def click_cochabamba_option(self):        
        self.click_element(self.cochabamba_option)
        # return ElementsPage(self.driver)
    
    def get_cochabamba_option(self):
        return self.find_element(self.cochabamba_option)

    # santacruz option
    def click_santacruz_option(self):        
        self.click_element(self.santacruz_option)
        # return ElementsPage(self.driver)
    
    def get_santacruz_option(self):
        return self.find_element(self.santacruz_option)

    # sucre option
    def click_sucre_option(self):        
        self.click_element(self.sucre_option)
        # return ElementsPage(self.driver)
    
    def get_sucre_option(self):
        return self.find_element(self.sucre_option)
    
    # otros option
    def click_otros_option(self):        
        self.click_element(self.otros_option)
        # return ElementsPage(self.driver)
    
    def get_otros_option(self):
        return self.find_element(self.otros_option)
    
    # forms option
    # def click_forms_option(self):        
    #     self.click_element(self.forms_option)
    
    # def get_forms_option(self):
    #     return self.find_element(self.forms_option)
        
    # Alerts, Frame & Windows option
    # def click_alerts_frames_windows_option(self):        
    #     self.click_element(self.alerts_frames_windows_option)
    
    # def get_alerts_frames_windows_option(self):
    #     return self.find_element(self.alerts_frames_windows_option)