from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException, NoAlertPresentException
from pypresence import Presence
import time

    
#\\CONFIG\\

#beta v1.2.0

#dm a person#2664 if something doesnt work

#chromedriver path
dpath ='C:\\path'

#extensions path
ABS = 'C:\\extension\\path'
ABS_VPN = 'C:\\extension\\path'
MS = 'C:\\extension\\path'

#accounts:
account1 = 'example@gmail.com'
account2 = 'example@gmail.com'
account3 = 'example@gmail.com'
account4 = 'example@gmail.com'
account5 = 'example@gmail.com'

#passwords:
password1 = 'example'
password2 = 'example'
password3 = 'example'
password4 = 'example'
password5 = 'example'

#DISCORD RPC
Heading1 = "using a bot to"
Heading2 = "grind microsoft rewards"

#no need to worry about the code below but u can read it if u like its not organized at all, i will do it later

#\\END OF CONFIG\\

while True:  # The presence will stay on as long as the program is running
    rpc = Presence("1006684699042775153")
    rpc.connect()
    rpc.update(details=Heading1,state=Heading2,large_image="abs-x2",start=int(1),buttons=[{"label": "Source", "url": "https://github.com/apersongithub/ABS-X"}, {"label": "Server", "url": "https://discord.gg/TFkNuXzGGx"}])
    break
print('finished with rpc')

#object of Options class
op = Options()
#set .zip file path of extension
op.add_extension(ABS_VPN)
op.add_extension(ABS)
op.add_extension(MS)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
time.sleep(0.9)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.9)
vpn1button = driver.find_element("xpath", '//*[@id="_fastdefult"]/li[2]')
vpn1button.click()
#1
time.sleep(2)
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1button = driver.find_element("xpath", '//*[@id="random-search"]')
abs1button.click()
abs1text = driver.find_element("xpath", '//*[@id="random-search-iterations-min"]')
abs1text.clear()
abs1text.send_keys(42) 
abs2text = driver.find_element("xpath", '//*[@id="random-search-iterations-max"]')
abs2text.clear()
abs2text.send_keys(50) 
abs3text = driver.find_element("xpath", '//*[@id="random-search-delay-min"]')
abs3text.clear()
abs3text.send_keys(500) 
abs4text = driver.find_element("xpath", '//*[@id="random-search-delay-max"]')
abs4text.clear()
abs4text.send_keys(3500)
abs2button = driver.find_element("xpath", '//*[@id="blitz-search"]')
abs2button.click()
driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')
signintext = driver.find_element("xpath", '//*[@id="i0116"]')
signintext.send_keys(account1)
time.sleep(1.5)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
time.sleep(1.5)
mssbutton.click()
time.sleep(1.5)
driver.find_element(By.ID, "i0118").send_keys(password1)
time.sleep(1.5)
driver.find_element(By.ID, "idSIButton9").click()

time.sleep(1)
window_before = driver.window_handles[0]

time.sleep(2)
driver.get('https://rewards.microsoft.com/')
time.sleep(2)
driver.get('https://bing.com/')
driver.get('https://rewards.microsoft.com/')
time.sleep(5)
driver.execute_script('''document.body.style.zoom = "100%";''')

try:
    reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward1.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward2.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward3.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward4.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward412 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[4]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward412.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward5.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward6.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward7 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[5]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward7.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

print('ok0')

try:
    reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward9.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward10.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward11.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


try:
    reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward12.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


#1.5 
print('ok')

time.sleep(1.9)

try:
    reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward13.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
except IndexError:
    print('weather button has been found')


time.sleep(1.9)
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()

time.sleep(190)

driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
vpnagain = driver.find_element("xpath", '/html/body/div/div[3]/ul/li[3]')
vpnagain.click()
#2 
print('nice')
time.sleep(1.9)
driver.get('https://rewards.microsoft.com/')

try:
    reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward1.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


try:
    reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward3.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward4.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward5.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


try:
    reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward6.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward7 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[5]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward7.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward8 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[9]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward8.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward9.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward10.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward11.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward12.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[17]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward13.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()

time.sleep(190)
driver.get('https://bing.com/')
time.sleep(45)
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
time.sleep(1.9)
vpnagain = driver.find_element("xpath", '/html/body/div/div[3]/ul/li[3]')
vpnagain.click()
#2 
print('nice')

driver.get('https://bing.com/')
time.sleep(1.5)
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
vpnagain = driver.find_element("xpath", '/html/body/div/div[3]/ul/li[4]')
vpnagain.click()
#3
print('nice32') 
time.sleep(1.9)
driver.get('https://rewards.microsoft.com/')
time.sleep(1.9)

try:
    reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward1.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward2.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward3.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward4.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')


try:
    reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward5.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward6.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward8 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[9]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward8.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
except IndexError:
    print('weather button has been found')


try:
    reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward9.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward10.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward11.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward12.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

try:
    reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward13.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

try:
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(42)
    driver.close()
    driver.switch_to.window(window_before)
    time.sleep(1.9)
except IndexError:
    print('weather button has been found')

driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
time.sleep(190)
print('done!')
try:
    driver.get('https://support.microsoft.com/en-us/authentication/signout')
    time.sleep(3)
    sout = driver.find_element("xpath", '/html/body/div/form/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div')
    sout.click()
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

#end of account #1 i just gonna copy and paste cus lazy
