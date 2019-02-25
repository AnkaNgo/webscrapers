from selenium import webdriver #Allows you to launch/initialise a browser.
from selenium.webdriver.common.by import By #Allows you to search for things using specific parameters
from selenium.webdriver.support.ui import WebDriverWait#Allows you to wait for a page to load
from selenium.webdriver.support import expected_conditions as EC #
from selenium.common.exceptions import TimeoutException #Handling a timeout situation

 
option = webdriver.ChromeOptions()
   
browser = webdriver.Chrome('chromedriver.exe', chrome_options=option)
wait = WebDriverWait(browser, 20)
browser.get("https://www.foody.vn/ho-chi-minh/quan-an?CategoryGroup=food&c=quan-an&page=1")
  
 
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='btn-load-more full-width']")))
#wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))

 

restaurants_list = browser.find_elements_by_xpath("//a[@data-bindhref]")

restaurants = [x.text for x in restaurants_list]
print('TITLES:')
print(restaurants, '\n')
browser.execute_script("window.stop();")
browser.quit() # Closes the browser   
 
