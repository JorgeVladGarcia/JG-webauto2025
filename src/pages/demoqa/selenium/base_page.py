from selenium.webdriver.common.by import By
import time
import logging
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Base page creates methods for actions over elements in webpage
'''

logger = get_logger(__name__)

class BasePage:
	# método para explicit wait de 10 segundos
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)
	
    # crear metodos para acciones sobre elementos 
	## encontrar elemento 
	def find_element(self, by_locator):
		# usar logger para cuando se encuentra elemento
		logger.info(f"Finding element:  {by_locator}")
		# encontrar elemento
		return self.wait.until(EC.visibility_of_element_located(by_locator))
		
    ## clickear elemento 
	def click_element(self, by_locator):        
		# resaltar cuando clickeamos un elemento 
		self.highlight(self.driver, self.find_element(by_locator))
		# clickear elemento 
		self.find_element(by_locator).click()		
		# usar loggger: cuando clickeamos 
		logger.info(f"Clicking element:  {by_locator}")
	
    ## enter text en elemento
	def enter_text(self, by_locator, text):         
		# input text 
		self.find_element(by_locator).send_keys(text)
		# usar logger: cuando hacemos input de texto 
		logger.info(f"Entering text:  {text} on {by_locator}")
	
    ## resaltar elemento encontrado 
	def highlight(self, driver, element, effect_time=2, color="blue", border=5):
		"""
		Highlights (blinks) a Selenium Webdriver element
		"""
		def apply_style(s):
			driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
		
		original_style = element.get_attribute('style')
		apply_style("border: {0}px solid {1};".format(border, color))
		time.sleep(effect_time)
		apply_style(original_style)
	
    ## hacer scroll en pantalla 
	def scroll_to_element(self, by_locator):
		element = self.find_element(by_locator)
		self.driver.execute_script("arguments[0].scrollIntoView();", element)
		