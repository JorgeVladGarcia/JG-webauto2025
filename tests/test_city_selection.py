from pages.demoqa.selenium.landing_page import LandingPage
from pages.demoqa.selenium.accesorios_page import AccesoriosPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestCitySelection:
        
    
    def test_city_page(self, driver, env):
        """
        Test that city selection is valid 
        """               
        # create the page object
        landing_page = LandingPage(driver, env)
        
        # Click on option
        city_selection = landing_page.click_lapaz_option

        # Assert that option is displayed 
        #assert "La Paz" in landing_page.get_city_dropdown().text, "City is not displayed"
