import re
from playwright.sync_api import Page, expect
from pages.demoqa.play.accesorios_page_play import AccesoriosPagePlay

def test_example(page: Page) -> None:
    accesorios_page = AccesoriosPagePlay(page)
    accesorios_page.navigate()
    accesorios_page.click_on_la_paz_option()
    accesorios_page.click_on_espacios()
    accesorios_page.click_on_accesorios()
    accesorios_page.click_on_item_1()
    accesorios_page.click_on_item_2()
    accesorios_page.click_on_item_3()
    accesorios_page.click_on_shop_cart()
    accesorios_page.click_on_completar_compra()
