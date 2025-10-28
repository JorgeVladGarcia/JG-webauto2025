import re
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay


class TestLandingPagePlay:

    def test_landing_page(self, page: Page) -> None:
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
        # expect(page.get_by_text("LA PAZ", exact=True)).to_be_visible()
        # expect(page.get_by_text("COCHABAMBA", exact=True)).to_be_visible()
        # expect(page.get_by_text("SANTA CRUZ", exact=True)).to_be_visible()
        # expect(page.get_by_text("SUCRE", exact=True)).to_be_visible()
        # expect(page.get_by_text("OTROS", exact=True)).to_be_visible()
        # page.get_by_text("SUCRE", exact=True).dblclick()
        # expect(page.locator("#dropdown-basic")).to_contain_text("Sucre")
