import pandas as pd
from selenium import webdriver
from time import sleep
from login_info import email_id, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):

        # Open Website
        self.driver.get('https://tinder.com/')

        #Wait for Website to fully load and popups to appear
        sleep(4)

        try:
            # Click on Login from Facebook on the popup
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
        except Exception:
            # If Login from Facbook is not there then click on more options and then click on it
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button').click()
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Wait for new windows to load fully 
        sleep(2)

        ## Facebook Login
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email_id)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()

        ## Switching back to main window
        self.driver.switch_to.window(base_window)
        sleep(6)

        # Close Prompts
        ## Location prompt
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

        ## Notification prompt
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

        ## Privacy Policy Accpet
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

        sleep(2)

    def get_profile_info(self):
        all_profiles = []
        # Open Profile
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button').click()

        # Get Information
        profile_name = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div').text

        # Check if there's no Bio
        try:
            profile_bio = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div').text
        except Exception:
            profile_bio = ''
        
        # Check if there's no age
        try:
            profile_age = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/span').text
        except Exception:
            profile_age = ''

        # Store that info
        all_profiles.append([profile_name,profile_age, profile_bio])

        # Close Profile
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[1]').click()

        return all_profiles

    def like(self):
        # Clicking on the right swipe button
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        # Clicking on the left swipe button
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    
    def add_home_screen_popup(self):
        # Close the "Add Tinder to your homescreen" popup
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()

    def close_match(self):
        # If you get match then close that popup
        self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a').click()

    def auto_swipe(self):
        # Wait for the Tinder animation to complete
        sleep(4)
        profile_data = []

        # Run infinitely
        while True:
            sleep(1)
            try:
                # Store profile data
                profile_data.extend(self.get_profile_info())
                sleep(1)

                # Like the profile
                self.like()
            except Exception:
                try:
                    # If Home screen popup arrives
                    self.add_home_screen_popup()
                    sleep(2)
                except Exception:
                    try:
                        # If we get a match (Luck factor)
                        self.close_match()
                    except Exception:
                        try:
                            # If we finished all the likes
                            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div')
                            print("Finished LIKES!!!")
                            break
                        except Exception as e:
                            print(e)
                            break
        return profile_data

# Run the bot and open Chrome
bot = TinderBot()

# Log via Facebook
bot.login()

# Get profile's info
profile_info = bot.auto_swipe()

# Export it into a csv
df = pd.DataFrame(profile_info, columns=['Name','Age','Bio'])
df.to_csv('Bios_Collected.csv', mode='a')