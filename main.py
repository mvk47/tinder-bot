from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
a = ""

chrome_driver_path = # enter your chrome path
my_email = '# your Email id'
my_password = #tinder password
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div'
                             '/div[2]/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)
main_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
time.sleep(3)
email = driver.find_element_by_name(name="email")
email.send_keys(my_email)
password = driver.find_element_by_name(name="pass")
password.send_keys(my_password)
driver.find_element_by_name(name='login').click()
driver.switch_to.window(main_window)
time.sleep(5)

driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

for i in range(0, 90):
    try:

        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]'
                                     '/div/div/div[1]/div/div[2]/div[4]/button').click()
        time.sleep(2)

        button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
        driver.execute_script("arguments[0].click();", button)
        button2 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        driver.execute_script("arguments[0].click();", button2)
        a = button2
    except NoSuchElementException:
        print("They did not ask")
        continue
    except ElementClickInterceptedException:

        time.sleep(2)
        a = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        driver.execute_script("arguments[0].click();", a)
        continue
driver.quit()