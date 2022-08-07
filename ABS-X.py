from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#\\CONFIG\\

#beta v0.0.1

#dm a person#2664 if something doesnt work

#chromedriver path
dpath ='C:/driver/path'

#extensions path
ABS = 'C:/extension/path.zip'
ABS_VPN = 'C:/extension/path.zip'
MS = 'C:/extension/path.zip'

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

#giftcard link
giftcard = 'microsoft.com/example/giftcard/'

#no need to worry about the code below but u can read it if u like its not organized at all, i will do it later

#\\END OF CONFIG\\


#object of Options class
op = Options()
#set .zip file path of extension
op.add_extension(ABS_VPN)
op.add_extension(ABS)
op.add_extension(MS)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,
options=op)
driver.maximize_window()
#launch browser
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
time.sleep(0.1)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.1)
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
mssbutton.click()
time.sleep(1.5)
driver.find_element(By.ID, "i0118").send_keys(password1)
driver.find_element(By.ID, "idSIButton9").click()
driver.get('https://rewards.microsoft.com/welcome/')
rbbutton = driver.find_element("xpath", '//*[@id="start-earning-rewards-link"]')
rbbutton.click()
time.sleep(1)
window_before = driver.window_handles[0]

time.sleep(2)
driver.get('https://rewards.microsoft.com/')
time.sleep(2)
driver.get('https://bing.com/')
time.sleep(2)
driver.get('https://rewards.microsoft.com/')
time.sleep(5)
driver.get('https://rewards.microsoft.com/welcometour')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button").click()
time.sleep(1.5)
driver.execute_script('''document.body.style.zoom = "100%";''')
reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward1.click()
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward2.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward3.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward4.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward5.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward6.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward7 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[5]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward7.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward8 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[9]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward8.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
s = driver.find_element("xpath", '/html/body/div[6]/div[2]/button')
s.click()
time.sleep(1.9)
reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward9.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward10.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward11.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward12.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward13.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()

time.sleep(45)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
vpnagain = driver.find_element("xpath", '/html/body/div/div[3]/ul/li[3]')
vpnagain.click()
#2
time.sleep(1.9)
driver.get('https://rewards.microsoft.com/welcometour')
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button").click()
time.sleep(1.5)
reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward1.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward2.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward3.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward4.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward5.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward6.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward7 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[5]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward7.click()
time.sleep(1.5)
driver.find_element(By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button").click()
time.sleep(1.9)
reward8 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[9]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward8.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward9.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward10.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward11.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward12.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward13.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
time.sleep(120)
driver.get('https://bing.com/')
time.sleep(45)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get('chrome-extension://nhiphjnpfaoagnfffcihodojonieglkk/popup.html')
vpnagain = driver.find_element("xpath", '/html/body/div/div[3]/ul/li[4]')
vpnagain.click()
#3
time.sleep(1.9)
driver.get('https://rewards.microsoft.com/welcometour')
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button").click()
time.sleep(1.5)
reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward1.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward2.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
reward3.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward4.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward5.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward6 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[3]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
driver.find_element(By.CSS_SELECTOR, "#modal-host > div:nth-child(2) > button").click()
time.sleep(1.9)
reward7 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[5]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward8 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[9]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward8.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
reward9 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[10]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward9.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward10 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[11]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward10.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward11 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward11.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward12 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[13]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward12.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
reward13 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[12]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
reward13.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(42)
driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
time.sleep(120)
driver.get('https://bing.com/')
sout = driver.find_element("xpath", '/html/body/div[1]/div/div[3]/header/div[2]/div/a[1]')
sout.click()
sout2 = driver.find_element("xpath", '/html/body/div[1]/div/div[3]/header/div[2]/div/span[1]/ul/li/a/span[2]')
sout2.click()
#end of account #1 i just gonna copy and paste cus lazy
