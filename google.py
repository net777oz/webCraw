import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import urllib.request
from urllib import parse
from scrollDown import scrollDown
import undetected_chromedriver as uc
if __name__ == "__main__":
    extList = {'png', 'gif', 'PNG', 'GIF'}

    keyWord = "jav rara anzai rion cumshot"

    dts = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    # options = webdriver.ChromeOptions()
    # options.add_argument("--ignore-certificate-errors-spki-list")
    # options.add_argument("--ignore-ssl-errors")
    # options.add_argument('log-level=3')
    # driver = uc.Chrome(options=options)
    driver = uc.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=en&authuser=0&ogbl")
    WebDriverWait(driver, 10)
    elem = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[2]/span/span/g-popup/div[1]/div").click()
    WebDriverWait(driver, 10)
    elem = driver.find_element(
        By.XPATH, "/html/body/div[2]/div[1]/div/g-menu/g-menu-item[1]/div/a").click()
    WebDriverWait(driver, 10)
    elem = driver.find_element(
        By.CSS_SELECTOR, "#regiontAU").click()
    WebDriverWait(driver, 10)
    elem = driver.find_element(
        By.XPATH, "/html/body/div[4]/form/div/div[2]/div[2]/div/div[1]").click()
    WebDriverWait(driver, 10)
    # Accept the alert (Click Ok button)
    Alert(driver).accept()
    WebDriverWait(driver, 10)
    elem = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a").click()
    WebDriverWait(driver, 10)

    # driver.get("https://www.google.co.kr/imghp?hl=en&authuser=0&ogbl")
    # WebDriverWait(driver, 10)
    # time.sleep(10)
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(keyWord+' filetype:gif')
    elem.send_keys(Keys.RETURN)

    # scrollDown(driver)
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    WebDriverWait(driver, 10)
    count = 1
    for image in images:
        tabs = driver.window_handles
        driver.switch_to.window(tabs[0])
        try:
            image.click()
            WebDriverWait(driver, 10)
            elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[3]/c-wiz/div/div/div/div[2]/a")))
            sebUrl = elem.get_attribute("href")
            driver.execute_script('window.open("about:blank", "_blank");')
            WebDriverWait(driver, 10)
            tabs = driver.window_handles
            driver.switch_to.window(tabs[-1])
            driver.get(sebUrl)
            WebDriverWait(driver, 10)
            scrollDown(driver)
            subImages = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
            WebDriverWait(driver, 10)
            for img in subImages:
                try:
                    img.click()
                    if count == 1:
                        # time.sleep(3)
                        pass
                    time.sleep(2)
                    WebDriverWait(driver, 10)
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img")))
                    imgUrl = elem.get_attribute("src")
                    file_ext = imgUrl.split('.')[-1]  # 확장자 추출
                    print('확장자 : ' + file_ext)
                    mch = False
                    for ext in extList:
                        if file_ext == ext:
                            mch = True
                            break

                    if mch == False:
                        file_ext = 'jpg'

                    opener = urllib.request.build_opener()
                    opener.addheaders = [
                        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                    urllib.request.install_opener(opener)

                    if mch == True:
                        try:
                            # opener = urllib.request.URLopener()
                            # opener.addheader('User-Agent', 'whatever')
                            # opener.retrieve(imgUrl, "./downloaded_images/" + keyWord +
                            #                 '/' + str(dts) + '_' + str(count) + '.' + file_ext)

                            # r = requests.get(imgUrl)
                            # uuu = "./downloaded_images/" + keyWord + '/' + str(dts) + '_' + str(count) + '.' + file_ext
                            # with open(uuu, 'wb') as outfile:
                            #     outfile.write(r.content)

                            # urllib.request.urlretrieve(
                            #     imgUrl, "./downloaded_images/" + keyWord + '/' + str(dts) + '_' + str(count) + '.' + file_ext)

                            urllib.request.urlretrieve(
                                imgUrl, "./downloaded_images/" + keyWord + '/' + str(dts) + '_' + str(count) + '.' + file_ext)
                            print('저장성공!')

                        except Exception as e:
                            print(str(imgUrl) + ' 저장실패!')
                            print(e)
                    else:
                        try:
                            urllib.request.urlretrieve(
                                imgUrl, "./downloaded_images/" + keyWord + '/' + str(dts) + '_' + str(count) + '.' + 'jpg')
                            print('저장성공!')
                        except Exception as e:
                            print(str(imgUrl) + ' 저장실패!')
                            print(e)
                    count = count + 1
                except:
                    pass
            driver.close()
        except Exception as e:
            print(e)
    driver.close()
