import re
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay


class TestLandingPagePlay:

    def test_landing_page(self, page: Page, log_test_name) -> None:
        """
        Test that the landing page displays all options
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        expect(landing_page.lapaz_option).to_be_visible()
        expect(landing_page.cbba_option).to_be_visible()
        expect(landing_page.scz_option).to_be_visible()
        expect(landing_page.sucre_option).to_be_visible()
        expect(landing_page.otros_option).to_be_visible()
