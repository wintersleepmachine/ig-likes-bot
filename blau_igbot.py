from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class IgBot:
    links_list = None

    def __init__(self, username, password):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.username = username
        self.password = password

    def get_links(self):
        # Start with a set as this will avoid duplicates link entries
        lst = set()
        with open('links', 'r') as file:
            for line in file:
                if line != '\n' and 'https://instagram.com/p/' in line:
                    lst.add(line.split()[1])

        # Set the links_list atribute to the list
        self.links_list = list(lst)

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)
        username_input = driver.find_element_by_xpath("//input[@aria-label='Phone number, username, or email']")
        password_input = driver.find_element_by_xpath("//input[@aria-label='Password']")

        username_input.clear()
        username_input.send_keys(self.username)

        password_input.clear()
        password_input.send_keys(self.password)

        try:
            login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
            login_btn.click()
            time.sleep(2)
        except:
            print('Error logging in')

    def likes(self, start=0):
        driver = self.driver
        count = 1

        for i in range(start, len(self.links_list)):
            link = self.links_list[i]

            try:
                print(f'Getting Link {count} out of {len(self.links_list)} {link}')
                driver.get(link)
                time.sleep(random.randint(3,7))
                like_button = driver.find_element_by_css_selector('.fr66n .wpO6b')
                like_button.click()
                count += 1
            except:
                continue

        print(f'Finished {len(self.links_list)} links')



# Input login and password credentials when instantiating the class
# myBot = IgBot(username, password)
#
# my_Bot.get_links()

# Login
# myBot.login()

# Commence likes, takes a start paramter which is default set to zero.
# If there was a problem during the loops, can start at ith position.
# myBot.likes()






# TESTING PURPOSES
# myBot = IgBot()
#
# myBot.get_links()
#
# # Login
# myBot.login()
#
# # Commence likes, takes a start paramter which is default set to zero.
# # If there was a problem during the loops, can start at ith position.
# myBot.likes()





