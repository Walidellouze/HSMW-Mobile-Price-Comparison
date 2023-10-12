from Comparateur_Wiki import *

def scrap_comparateur_jumia(nom):
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://www.jumia.com.tn/")
    driver.maximize_window()
    
    # 1) chercher la liste des telephones selon le nom du telephone
    search_bar = find_element('//*[@id="fi-q"]',driver)
    search_bar.send_keys(nom)
    search_bar.submit()
    button = find_element("//*[@id='search']/button",driver)
    button.click()
    
    try:
        # 2) extraire de cette liste les informations necessaire des telephones 
        telephone= []
        Telephon_element= find_elements("c-prd",driver,By.CLASS_NAME)
        for i in Telephon_element:
            nom_telephone=find_element("name",i,By.CLASS_NAME).text
            prix_telephone=find_element("prc",i,By.CLASS_NAME).text
            image_telephone = find_element("img",i,By.CLASS_NAME)
            image = image_telephone.get_attribute('src')
            lien_telephone = find_element("core",i,By.CLASS_NAME)
            lien_url = lien_telephone.get_attribute('href')
            telephone.append({"nom_telephone":nom_telephone,"prix_telephone":prix_telephone,"disponiblite_telephone":"En stock","image":image,"nom_site":"Jumia","lien_url":lien_url})
            
        return telephone 
    except:
        return {}

#scrap_comparateur_jumia("Apple Iphone 11 Noir 128 GO 4 GO RAM")

