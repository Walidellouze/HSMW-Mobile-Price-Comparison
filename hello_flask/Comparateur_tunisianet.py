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
    Time.sleep(1)
    elem = driver.find_element(identifier_type, identifier)
    return elem


def find_elements(identifier,driver,identifier_type=By.XPATH,time=10):
    WebDriverWait(driver, time).until(
    EC.presence_of_element_located((identifier_type, identifier))
    )
    Time.sleep(1)
    elem = driver.find_elements(identifier_type, identifier)
    return elem



def scrap_comparateur_tunisianet(nom):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tunisianet.com.tn/")
    driver.maximize_window()
    
    # 1) chercher la liste des telephones selon le nom du telephone
    search_bar = find_element('//*[@id="search_query_top"]',driver)
    search_bar.send_keys(nom)
    search_bar.submit() #entrer =click()
    try:
        telephoneMytek= []
        j=1
        Telephon_element= find_elements("item-product",driver,By.CLASS_NAME)
        for i in Telephon_element:
            nom_telephone=find_element("product-title",i,By.CLASS_NAME).text                              
            prix_telephone=find_element('//*[@id="js-product-list"]/div/div['+str(j)+']/article/div/div[4]/div[2]/span[1]',i).text
            image_telephone = find_element("second-img",i,By.CLASS_NAME)
            image = image_telephone.get_attribute('src')
            lien_telephone = find_element("product-thumbnail",i,By.CLASS_NAME)
            lien_url = lien_telephone.get_attribute('href')
            telephoneMytek.append({"nom_telephone":nom_telephone,"prix_telephone":prix_telephone,"disponiblite_telephone":"En stock","image":image,"nom_site":"tunisianet","lien_url":lien_url})
            j=j+1
        return telephoneMytek
    except:
        return {}