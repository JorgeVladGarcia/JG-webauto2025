import re
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay
import time

class TestProductSelection:
    def test_product_selection(self, page: Page) -> None:
        """
        Test that user selects product successfully
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        landing_page.click_random_city()
        landing_page.click_on_espacios()
        accesorios_page = landing_page.click_on_accesorios()
        accesorios_page.click_random_item()
        expect(accesorios_page.success_toast).to_be_visible()
