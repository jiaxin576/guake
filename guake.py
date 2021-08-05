#http://npm.taobao.org/mirrors/chromedriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
        
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(30)
driver.get("https://fb.me/") #打开
time.sleep(20)
#driver.maximize_window()

driver.get_screenshot_as_file("D:\\AutoJx\\"+str(link[14::])+"all"+".png")
driver.find_element_by_xpath("//*[@id='marketing_name']/div[1]/div/div/div/div/span[1]").click()
driver.switch_to.frame(driver.find_element_by_id("iframe"))
        try:
            driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/span[1]").click()

        except Exception as e:
            print(e,project,"没有找到情况1的All Customers")
            
from selenium.webdriver.support.select import Select
#binary = FirefoxBinary(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#profile =FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\v3y1rz8g.AutoJx')
#driver =webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)
from selenium.webdriver.support import expected_conditions as EC
driver =webdriver.Ie()

driver.switch_to.frame(driver.find_element_by_xpath("html/frameset/frameset/frameset[2]/frame[2]"))
   
if mes.text !="审核":
 
#获取当前页面句柄
    current_handle = driver.current_window_handle
    driver.switch_to.default_content()
#接下来会有新的窗口打开，获取所有窗口句柄
    all_handles =driver.window_handles
#循环判断，把当前句柄从所有句柄中移除，剩下的就是你想要的新窗口
    for handle in all_handles:
	    if handle!=current_handle:
	        driver.switch_to.window(handle)
#接下来在新页面进行操作
    sel = driver.find_element_by_name("CTL1$ddlProperty_1307")
    Select(sel).select_by_index(3)  #未审核
    driver.find_element_by_id("btnFinish1").click()
    if EC.alert_is_present()(driver):
        alert=driver.switch_to_alert()#是否完成任务
        alert.accept()
        
#关闭当前窗口，主要使用close而不是quite
    time.sleep(10)
    driver.switch_to.window(current_handle)
