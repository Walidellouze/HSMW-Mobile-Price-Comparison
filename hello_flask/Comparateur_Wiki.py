from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as Time

def click_button(identifier,driver,identifier_type=By.XPATH,time=10):
    WebDriverWait(driver, time).until(
    EC.presence_of_element_located((identifier_type,identifier))
    )
    Time.sleep(2)#badlna time
    button = driver.find_element(identifier_type,identifier)
    button.click()

def find_element(identifier,driver,identifier_type=By.XPATH,time=10):

    WebDriverWait(driver, time).until(
    EC.presence_of_element_located((identifier_type, identifier))
    )
    Time.sleep(2)
    elem = driver.find_element(identifier_type, identifier)
    return elem


def find_elements(identifier,driver,identifier_type=By.XPATH,time=10):
    WebDriverWait(driver, time).until(
    EC.presence_of_element_located((identifier_type, identifier))
    )
    Time.sleep(2)
    elem = driver.find_elements(identifier_type, identifier)
    return elem


def scrap_comparateur_wiki(nom):
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://www.wiki.tn/")
    driver.maximize_window()
    
    # 1) chercher la liste des telephones selon le nom du telephone
    search_bar = find_element('//*[@id="search_query_top"]',driver)
    search_bar.send_keys(nom)
    search_bar.submit() #entrer =click()
    try:
        # 2) extraire de cette liste les informations necessaire des telephones 
        telephoneMytek= []
        Telephon_element= find_elements("last-item-of-mobile-line",driver,By.CLASS_NAME)
        for i in Telephon_element:
            nom_telephone=find_element("product-name",i,By.CLASS_NAME).text
            prix_telephone=find_element("product-price",i,By.CLASS_NAME).text
            image_telephone = find_element("replace-2x",i,By.CLASS_NAME)
            image = image_telephone.get_attribute('src')
            lien_telephone = find_element("product-name",i,By.CLASS_NAME)
            lien_url = lien_telephone.get_attribute('href')
            telephoneMytek.append({"nom_telephone":nom_telephone,"prix_telephone":prix_telephone,"disponiblite_telephone":"dispo","image":image,"nom_site":"Wiki","lien_url":lien_url})
        
        return telephoneMytek 
    except:
        return {}
#scrap_comparateur_wiki("Apple Iphone 11 Noir 128 GO 4 GO RAM")