import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
import threading
from faker import Faker
import faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
from random import uniform
import string

multi=int(input('Number of thread:'))
#process=int(input('Which process you need to Run? 1-Registration. 2-Login. 3-Both.'))

class othread(threading.Thread):
    def __init__(self):

        threading.Thread.__init__(self)

    def run(self):

       try :   
           letters =string.ascii_uppercase
           options= webdriver.ChromeOptions()
           options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #    options.add_argument("--headless")
           options.add_argument("--lang=en-US")
           options.add_argument("--disable-blink-features=AutomationControlled")
           options.add_argument("--incognito")
           options.add_argument('--no-sandbox')
           options.add_argument('--disable-setuid-sandbox')
           options.add_argument('--disable-dev-shm-usage')
           options.add_argument('--disable-accelerated-2d-canvas')
           options.add_argument('--disable-gpu')
        #    driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
           driver = webdriver.Chrome('chromedriver.exe', options=options)
        #    driver.set_window_size(620, 720)
        #    driver.delete_all_cookies()
        #    driver.implicitly_wait(10)
        
           driver.get ('https://demo.nopcommerce.com/register?returnUrl=%2F')
           sleep(1)
           WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.ID,'gender-male')))
           A=driver.find_element(By.ID,'gender-male')
           driver.execute_script("arguments[0].click();",A)
           f=Faker()
           name=(f.name()).split()
           FirstName= name[0]
           driver.find_element(By.ID,'FirstName').send_keys(FirstName)
           LastName = name[1]
           driver.find_element(By.ID,'LastName').send_keys(LastName)
           selectDay = Select(driver.find_element(By.NAME,'DateOfBirthDay'))
           selectDay.select_by_visible_text('24')
           selectMonth = Select(driver.find_element(By.NAME,'DateOfBirthMonth'))
           selectMonth.select_by_visible_text('June')
           selectYear = Select(driver.find_element(By.NAME,'DateOfBirthYear'))
           selectYear.select_by_visible_text('2000')

           e=(f.email())
           driver.find_element(By.ID,'Email').send_keys(e)
           
           companyname = ''.join(random.choice(letters) for i in range(random.randint(9,12))  )
           driver.find_element(By.ID,'Company').send_keys(companyname)
           driver.find_element(By.ID,'Password').send_keys("Test1234$$")
           driver.find_element(By.ID,'ConfirmPassword').send_keys("Test1234$$")
           sleep(1)
           driver.find_element(By.ID,'register-button').click()
           WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.buttons > a')))
           driver.find_element(By.CSS_SELECTOR,'body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.buttons > a').click()
           sleep(1)
           with open(r'emils_list.txt','a') as abood :
               AA=FirstName+' / '+LastName+' / '+e+' / '+companyname
               abood.write(f"[{AA}]\n")
           driver.get('https://demo.nopcommerce.com/login?returnUrl=%2F')
           WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.ID,'Email')))
           driver.find_element(By.ID,'Email').send_keys(e)
           driver.find_element(By.ID,'Password').send_keys('Test1234$$')
           sleep(1)
           driver.find_element(By.CSS_SELECTOR,'body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.customer-blocks > div.returning-wrapper.fieldset > form > div.buttons > button').click()


           sleep(5455)
        #    select = Select(driver.find_element(By.XPATH,''))
        #    f=Faker()
        # o=(f.name()).split()
        # WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,'')))
        #  cemail = ''.join(random.choice(letters) for i in range(random.randint(9,12))  )
        # driver.execute_script("arguments[0].click();",A)


        
        # sleep(random.uniform(1,5))
        # with open(r'C:\python1\numberf.txt','r') as fin:
        #     PHONE = fin.readline()

        # with open(r'C:\python1\numberf.txt', 'r+') as file:
        #     lines = file.readlines()
        #     file.seek(0)
        #     file.writelines(lines[1:])
        #     file.truncate()
                


       except :
             print('Erorr')
             global multi
            
             sleep(1)
             multi = multi + 1
             run_script(multi)           

x = 0
def run_script(lop) :
    global x
    looops = lop-x
    for i in range(looops):
        if x < lop:
            othread().start()
        else:
            break
        x = x + 1
    
    

run_script(multi)

