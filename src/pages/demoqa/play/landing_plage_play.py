from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay
from pages.demoqa.play.accesorios_page_play import AccesoriosPagePlay
from pages.demoqa.play.checkout_page_play import CheckoutPagePlay
import random

class LandingPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # city option locators
        self.lapaz_option : Locator = page.get_by_text("LA PAZ", exact=True)
        self.cbba_option : Locator = page.get_by_text("COCHABAMBA", exact=True)
        self.scz_option : Locator = page.get_by_text("SANTA CRUZ", exact=True)
        self.sucre_option : Locator = page.get_by_text("SUCRE", exact=True)
        self.otros_option : Locator = page.get_by_text("OTRAS CIUDADES", exact=True)

        # menu option locatos 
        self.espacios : Locator = page.get_by_role("link", name="ESPACIOS DE LA CASA ")
        self.accesorios : Locator = page.get_by_role("link", name="Accesorios PersonalesAccesorios Personales")

        # dropdown locators 
        self.dropdown : Locator = page.locator("#dropdown-basic")

        # header locators 
        self.shop_cart : Locator = page.get_by_role("button", name="Shop Cart")
        self.completar_compra : Locator = page.get_by_role("button", name="COMPLETAR LA COMPRA")

        # Map city option locators for random selection in dictionary
        self.city_buttons = {
            "LA PAZ": self.lapaz_option,
            "COCHABAMBA": self.cbba_option,
            "SANTA CRUZ": self.scz_option,
            "SUCRE": self.sucre_option,
            "OTRAS CIUDADES": self.otros_option,
        }

    def navigate(self):
        self.navigate_url(url="https://casaideas.com.bo/")

    # Randomly select option from landscape and click it.
    # Returns the name of the random selection
    def click_random_city(self):
        city = random.choice(list(self.city_buttons.keys()))
        self.city_buttons[city].click()
        return city

    def click_on_la_paz_option(self):
        self.click_element(self.lapaz_option)

    def click_on_espacios(self):
        self.click_element(self.espacios)

    def click_on_accesorios(self):
        self.click_element(self.accesorios)
        return AccesoriosPagePlay(self.page)
    
    def click_on_item_1(self):
        self.click_element(self.item_1)

    def click_on_item_2(self):
        self.click_element(self.item_2)

    def click_on_item_3(self):
        self.click_element(self.item_3)

    def click_on_shop_cart(self):
        self.click_element(self.shop_cart)    

    def click_on_completar_compra(self):
        self.click_element(self.completar_compra)
        return CheckoutPagePlay(self.page)