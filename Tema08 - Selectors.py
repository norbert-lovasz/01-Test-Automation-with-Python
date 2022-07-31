# Tema 8 - SELECTORS


from time import sleep
from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select





"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ID """ 
#s = Service(ChromeDriverManager().install())
# chrome.get('http://automationpractice.com/index.php?controller=contact')
#chrome.maximize_window()


# searchBar = chrome.find_element(By.ID,"search_query_top")
# searchBar.send_keys("Printed Summer Dress")

# chrome.find_element(By.ID,"newsletter-input").send_keys("test@email.com")

# subjectHeading = Select(chrome.find_element(By.ID,"id_contact"))
# subjectHeading.select_by_value('2')

# chrome.quit()

"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Link text """ 
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
# sleep(2)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.LINK_TEXT,"Buttons").click()
# sleep(3)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(4)
# chrome.find_element(By.LINK_TEXT,"Enabled and disabled elements").click()
# sleep(3)
# chrome.quit()

"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Partial Link text """ 

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Autocompl").click()
# sleep(2)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"ttons").click()
# sleep(3)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(4)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Enabled and ").click()
# sleep(3)
# chrome.quit()

"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: name """ 

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# chrome.find_element(By.ID,"ez-accept-all").click()
# sleep(2)
# chrome.find_element(By.NAME,"firstname").send_keys("Lovasz")
# chrome.find_element(By.NAME,"lastname").send_keys("Norbert")
# Continent = Select(chrome.find_element(By.NAME,"continents"))
# Continent.select_by_visible_text("Asia")

# sleep(5)
# chrome.quit()



"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Tag """ 

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# chrome.find_element(By.ID,"ez-accept-all").click()
# sleep(2)
# tag = chrome.find_elements(By.TAG_NAME, 'input')
# print(tag)
# tag[0].send_keys('Lovasz')
# tag[1].send_keys('Norbert')
# tag[2].click()
# tag[7].click()
# sleep(5)

"""Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Class name """ 

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# clasa=chrome.find_elements(By.CLASS_NAME, 'form-control')
# clasa[0].send_keys("Lovasz")
# sleep(2)
# clasa[1].send_keys("Norbert")
# sleep(2)
# clasa[2].send_keys("Engineer")
# sleep(2)
# Select(clasa[3]).select_by_visible_text("2-4")
# sleep(2)
# clasa[4].send_keys("04/04/2020")
# sleep(2)

