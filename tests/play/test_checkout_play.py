import pytest
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay
import time

class TestCheckOut:
    @pytest.mark.parametrize("read_data", ["usernames"], indirect=True)
    def test_user_login(self, page: Page, read_data) -> None:
        """
        Test that user can checkout cart after sign in with existing credentials 
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        landing_page.click_random_city()
        landing_page.click_on_espacios()
        accesorios_page = landing_page.click_on_accesorios()
        accesorios_page.click_random_item()
        # go to checkout page
        landing_page.click_on_shop_cart()
        checkout_page = landing_page.click_on_completar_compra()
        checkout_page.click_on_completar_compra()
        # fill out sign in info
        for data in read_data:
            checkout_page.enter_email(data["email"])
            checkout_page.enter_password(data["password"])
            checkout_page.click_iniciar_sesion()
            checkout_page.click_on_completar_compra()
            # verify: form Datos personales is visible 
            expect(checkout_page.datos_personales_form).to_be_visible()

        # checkout_page.enter_email("vlad.garciaperez@gmail.com")
        # checkout_page.enter_password("casaideasPWD1!")
        # checkout_page.click_iniciar_sesion()
        # checkout_page.click_on_completar_compra()
        # # verify: form Datos personales is visible 
        # expect(checkout_page.datos_personales_form).to_be_visible()

    # def test_no_user_login(self, page: Page) -> None:
    #     """
    #     Test that user cannot checkout cart after sign in with non-existent credentials 
    #     """
    #     landing_page = LandingPagePlay(page)
    #     landing_page.navigate()
    #     landing_page.click_random_city()
    #     landing_page.click_on_espacios()
    #     accesorios_page = landing_page.click_on_accesorios()
    #     accesorios_page.click_random_item()
    #     # go to checkout page
    #     landing_page.click_on_shop_cart()
    #     checkout_page = landing_page.click_on_completar_compra()
    #     checkout_page.click_on_completar_compra()
    #     # fill out info: pending 
    #     checkout_page.click_iniciar_sesion()
    #     # verify toggle exists 
    #     expect(checkout_page.success_toast).to_be_visible()