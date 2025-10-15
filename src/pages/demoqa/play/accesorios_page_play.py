from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay

class AccesoriosPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.lapaz_option : Locator = page.get_by_text("LA PAZ", exact=True)
        self.espacios : Locator = page.get_by_role("link", name="ESPACIOS DE LA CASA ")
        self.accesorios : Locator = page.get_by_role("link", name="Accesorios PersonalesAccesorios Personales")
        self.item_1 : Locator = page.locator("button[name=\"add__22763\"]")
        self.item_2 : Locator = page.locator("button[name=\"add__22762\"]")
        self.item_3 : Locator = page.locator("button[name=\"add__22764\"]")
        self.shop_cart : Locator = page.get_by_role("button", name="Shop Cart")
        self.completar_compra : Locator = page.get_by_role("button", name="COMPLETAR LA COMPRA")

    def navigate(self):
        self.navigate_url(url="https://casaideas.com.bo/")

    def click_on_la_paz_option(self):
        self.click_element(self.lapaz_option)

    def click_on_espacios(self):
        self.click_element(self.espacios)

    def click_on_accesorios(self):
        self.click_element(self.accesorios)

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