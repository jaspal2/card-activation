from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from hello import tokenGenerator
from csvread import CsvReader
#--------------Locators-------------------
btnCaptch="//span[@id='recaptcha-anchor']"
btnSubmit="//input[@value='Submit']"
iframCaptch="//iframe[@title='reCAPTCHA']"
txtCardCode="//input[@id='name']"
txtCardID="//input[@id='email']"

#----------------Read CSV------------------------
csv_path="/Users/jsin0034/dev/Docker-practice/seleniumdocker/cardDetails.csv"

csv= CsvReader()
df=csv.read_csv(csv_path)
listCarNum=df["ID"].values
listCardCode=df["PIN"].values

#--------------------------------------

def solve():
    import sys
    from twocaptcha import TwoCaptcha
    result = None

    sitekey = '6LcwdZ8UAAAAACzsqVmYcPjLMOXfpUZoXP2dL_HV'
    api_key = '8be6cdc9b0bb51ec36925f6c77f33c09'
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url='https://2captcha.com/demo/recaptcha-v2'
        )

    except Exception as e:
        sys.exit(e)
    return result

driver = webdriver.Chrome(executable_path="/Users/jsin0034/dev/Drivers/chromedriver")
driver.maximize_window()
driver.get("https://www.a1activate.com.au/monashuniversityactivationpage")
for index in range(listCarNum.size):
    time.sleep(2)
    txtCardNum=driver.find_element(By.XPATH,txtCardID)
    txtCardNum.clear()
    txtCardNum.send_keys(listCarNum[index])
    time.sleep(2)
    txtCodeElement=driver.find_element(By.XPATH, txtCardCode)
    txtCodeElement.clear()
    txtCodeElement.send_keys(str(listCardCode[index]))
    time.sleep(5)
    print("Getting captcha code")
    textarea = driver.find_element(By.ID, 'g-recaptcha-response')
    solution = solve()
    code = solution['code']
    print("code is" +  str(code))
    driver.execute_script(f"var ele=arguments[0]; ele.innerHTML = '{code}';", textarea)
    time.sleep(2)
    driver.switch_to.parent_frame()
    submit=driver.find_element(By.XPATH, btnSubmit)
    submit.click()
    time.sleep(10)

