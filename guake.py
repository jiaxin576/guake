#http://npm.taobao.org/mirrors/chromedriver将下载的.exe文件放置在python根目录即可
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


#获取当前页面的链接地址
url=driver.current_url
driver.get("http://baike.so.com")
#后退
driver.back()
#前进
driver.forward()
#刷新
driver.refresh()
#浏览器退出
ele=driver.switch_to.active_element
driver.find_element_by_link_text("良医")
driver.find_element_by_partial_link_text("医")
#获取元素的大小
ele_size=input_element.size
#获取该元素的子元素
input_element.find_element()
#判断元素是否显示
input_element.is_displayed()
#判断元素是否可以使用
input_element.is_enabled()
#判断元素是否是选中状态
input_element.is_selected()

from selenium.webdriver.support.wait import WebDriverWait
WebDriverWait(driver,最大等待时间，检查频率).until()

记得要把浏览器调到100%，否则控件找的不准确。
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.baidu.com/") #打开


两种方式获取cookIe
打开网页手工输入登录信息
driver.get('http://udm')  # 打开界面
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
driver.delete_all_cookies()
for cookie in listCookies:
    driver.add_cookie({
        'domain': '.zte.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })

读取cookie实现免登陆访问
time.sleep(5)
driver.refresh()

抓包
def cookies_parse(cookies):
    parsed_cookies = []
    #cookies = urllib.unquote(cookies)  # urldecode
    cookies = cookies.split(';')
    for cookie in cookies:
        cookie = cookie.strip()
        name = cookie.split('=')[0]  # 将空格替换为+
        value = cookie.split('=')[1]
        parsed_cookies.append({'name': name, 'value': value})
    return parsed_cookies

driver.delete_all_cookies()

for cookie in cookies_parse(Cookie):
    driver.add_cookie(cookie)
