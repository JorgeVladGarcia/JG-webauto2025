from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay
import random 

class AccesoriosPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.item_1 : Locator = page.locator("button[name=\"add__22763\"]")
        self.item_2 : Locator = page.locator("button[name=\"add__22762\"]")
        self.item_3 : Locator = page.locator("button[name=\"add__22764\"]")
        self.shop_cart : Locator = page.get_by_role("button", name="Shop Cart")
        self.completar_compra : Locator = page.get_by_role("button", name="COMPLETAR LA COMPRA")

        # success toast: 
        self.success_toast : Locator = page.get_by_text("Agregado Correctamente al carro✖")

        # Map locators for random product seleciton 
        self.item_selection = {
            "item_1": self.item_1,
            "item_2": self.item_2,
            "item_3": self.item_3
        }

    def navigate(self):
        self.navigate_url(url="https://casaideas.com.bo/")

    # Randomly select item from accesorios page and click it

    def click_random_item(self):
        item = random.choice(list(self.item_selection.keys()))
        self.item_selection[item].click()

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
    
