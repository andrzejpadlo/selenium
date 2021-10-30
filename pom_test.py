from selenium import webdriver
from training_ground_page import TrainingGroundPage
from trial_page import TrialPage

browser1 = webdriver.Chrome()

# Trial Page
trial_page = TrialPage(driver=browser1)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

#Training Grounds

trng_page = TrainingGroundPage(driver=browser1)
trng_page.go()
assert trng_page.button1.text == 'Button1'
trng_page.button1.click()

# driver.close #  close 1 tab

browser1.quit()  # close the browser

# driver.title # get webpage title
