from pages.demoqa.selenium.landing_page import LandingPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestDemoQALandingPage:
        
    
    def test_landing_page(self, driver, env):
        """
        Test that the casa ideas landing page is displayed with all options
        """                
        logger.info("Environment: %s", env)
        # create the page object
        landing_page = LandingPage(driver, env)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("La Paz option: " + landing_page.get_lapaz_option().text)
        logger.info("Cochabamba option: " + landing_page.get_cochabamba_option().text)
        logger.info("Santa Cruz option: " + landing_page.get_santacruz_option().text)
        logger.info("Sucre option: " + landing_page.get_sucre_option().text)
        logger.info("Otras ciudades option: " + landing_page.get_otros_option().text)
        assert landing_page.get_lapaz_option().text == "LA PAZ", "Elements option is not displayed"
        assert landing_page.get_cochabamba_option().text == "COCHABAMBA", "Elements option is not displayed"
        assert landing_page.get_santacruz_option().text == "SANTA CRUZ", "Elements option is not displayed"
        assert landing_page.get_sucre_option().text == "SUCRE", "Elements option is not displayed"
        assert landing_page.get_otros_option().text == "OTRAS CIUDADES", "Elements option is not displayed"

    def test_city_selction_landing_page(self, driver, env):
        """
        Test that city selection is correct 
        """