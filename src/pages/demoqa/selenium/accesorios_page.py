from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.demoqa.selenium.base_page import BasePage
from config.config import  BASE_URL

logger = get_logger(__name__)

# Crear metodo LandingPage que hereda de BasePage 
class AccesoriosPage(BasePage):

    # Locators: 
    city_dropdown = (By.ID, "dropdown-basic")
    lapaz_option = (By.NAME, "59")
    cochabamba_option = (By.NAME, "61")
    santacruz_option = (By.NAME, "60")
    sucre_option = (By.NAME, "181")
    otros_option = (By.NAME, "62")
    
    # Actions:
    def click_city_dropdown(self):
        self.click_element(self.city_dropdown)

    def get_city_dropdown(self):
        return self.find_element(self.city_dropdown)
    
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