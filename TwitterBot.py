#!python 3
# Takes password as string from command line
# send tweet of the strs  to be downloaded

import sys, time
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# this part is just incase user isn't logged in
def browserLogin():
    print('logging into E-mail')
    loginEmailInput = browser.find_element(by=By.XPATH, value=sign_in_xpath)
    loginEmailInput.click()
    time.sleep(5)
    loginEmailInput.send_keys('')  # username goes here
    loginEmailClick = browser.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
    loginEmailClick.click()
    time.sleep(2)
    password_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    browser.find_element(by=By.XPATH, value=password_xpath).send_keys(sys.argv[1:])
    login_button = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span'
    browser.find_element(by=By.XPATH, value=login_button).click()


def tweeting():
    tweetSign = '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    tweetMessage = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    tweetButtonXpath = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span'
    time.sleep(10)
    browser.find_element(by=By.XPATH, value=tweetSign).click()
    time.sleep(5)
    browser.find_element(by=By.XPATH, value=tweetMessage).send_keys(input('type in your Tweet! \n'))
    time.sleep(4)
    browser.find_element(by=By.XPATH, value=tweetButtonXpath).click()


browser = webdriver.Firefox()
browser.get('https://www.twitter.com/login')
time.sleep(20)
sign_in_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
loginEmailInput = browser.find_element(by=By.XPATH, value=sign_in_xpath)
if loginEmailInput.is_displayed():
    browserLogin()
    tweeting()
else:
    tweeting()

# find a way to make it log in on its own and tweet on its own
# use the argument thingy to solve all these bulky arguments
