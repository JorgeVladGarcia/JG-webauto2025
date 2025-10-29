import pytest
from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_plage_play import LandingPagePlay
from soft_assert import check, verify
import json

# Utility to load users from JSON file
def load_users(file_name="usernames.json"):
    with open(f"tests/data/{file_name}", encoding="utf-8") as file:
        return json.load(file)

class TestCheckOut:
    @pytest.mark.parametrize("user_data", load_users())
    def test_user_login(self, page: Page, user_data, log_test_name) -> None:
        """
        Test that user can checkout cart after sign in with existing credentials 
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        landing_page.click_random_city()
        landing_page.click_on_espacios()
        accesorios_page = landing_page.click_on_accesorios()
        accesorios_page.click_random_item()

        # Go to checkout page
        landing_page.click_on_shop_cart()
        checkout_page = landing_page.click_on_completar_compra()
        checkout_page.click_on_completar_compra()
        
        # Fill credentials
        checkout_page.enter_email(user_data["email"])
        checkout_page.enter_password(user_data["password"])
        checkout_page.click_iniciar_sesion()
        checkout_page.click_on_completar_compra()
        expect(checkout_page.datos_personales_form).to_be_visible()

    def test_no_user_login(self, page: Page) -> None:
        """
        Test that user cannot checkout cart after sign in with non-existent credentials 
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
        # fill out info: pending 
        checkout_page.click_iniciar_sesion()
        # verify toggle exists 
        expect(checkout_page.success_toast).to_be_visible()