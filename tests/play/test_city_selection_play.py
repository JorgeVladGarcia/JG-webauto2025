import re
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay


class TestCitySelection:

    def test_city_selection(self, page: Page, log_test_name) -> None:
        """
        Test that user selects correct city from landpage options
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        random_city_selection = landing_page.click_random_city()
        # Correct for capitalization 
        random_city_expected = random_city_selection.title()
        expect(landing_page.dropdown).to_contain_text(random_city_expected)
