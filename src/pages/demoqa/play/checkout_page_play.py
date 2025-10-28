from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay
import random 

class CheckoutPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.completar_compra : Locator = page.get_by_role("button", name="COMPLETAR LA COMPRA")
        self.iniciar_sesion: Locator = page.locator("button").filter(has_text="Iniciar sesión")
        self.email: Locator = page.locator("input[name=\"email\"]")
        self.password: Locator = page.locator("input[name=\"password\"]")

        # success toast: 
        self.success_toast : Locator = page.get_by_text("* El campo Email no puede estar vacío* El campo Contraseña no puede estar vacío✖")

        # checkout form:
        self.datos_personales_form: Locator = page.locator(".shippingCard").first 

    def navigate(self):
        self.navigate_url(url="https://www.casaideas.com.bo/checkout/cart#formstep1")

    def click_on_completar_compra(self):
        self.click_element(self.completar_compra)
    
    def click_iniciar_sesion(self):
        self.click_element(self.iniciar_sesion)
    
    def enter_email(self, email):
        self.enter_text(self.email, email)
    
    def enter_password(self, password):
        self.enter_text(self.password, password)
    
