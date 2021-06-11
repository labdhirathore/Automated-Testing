from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\nTestCases\n")

# TestCase 1: Title
print("TestCase 1: Title")
if(driver.title):
    print("Title Verification Successful: ", driver.title, "\n")
else:
    print("Title Verification Failed!\n")

# TestCase 2: Home button
print("TestCase 2: Home button")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")


# TestCase 3: Testing the media icons
print("TestCase 3: Testing the media icons")

try:
    driver.execute_script("arguments[0].scrollIntoView()",
                               driver.find_element_by_xpath("//div[@class='top-header-agile-right']"))

    icon1 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[1]/a")
    icon2 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[2]/a")
    icon3 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[3]/a")
    icon4 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[4]/a")
    icon5 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[5]/a")
    icon6 = driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[6]/a")
    time.sleep(3)
    if ((icon1.is_displayed() and icon1.is_enabled()) and (icon2.is_displayed() and icon2.is_enabled()) and
            (icon3.is_displayed() and icon3.is_enabled()) and (icon4.is_displayed() and icon4.is_enabled()) and
            (icon5.is_displayed() and icon5.is_enabled()) and (icon6.is_displayed() and icon6.is_enabled())):
        print("Media Icons are verified  successful")
except NoSuchElementException:
    print("Verification Unsuccessful!")


# TestCase 4: Check if navbar appears
print("TestCase 4: Check if navbar appears")
try:
    driver.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 5: About Us Page
print("TestCase 5: About Us Page")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Vision, Mission and Values').click()
    time.sleep(3)
    print(' About Us Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 6: Internship Positions Page
print("TestCase 6: Internship Positions Page")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Internship Positions').click()
    time.sleep(3)
    driver.find_element_by_link_text('Management Volunteer').click()
    time.sleep(3)
    print('Internship Positions Page verified Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)


#TestCase 7: Check the Form
print("TestCase 7: Check the Form")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    driver.find_element_by_name('Name').send_keys('Labdhi Rathore')
    time.sleep(3)
    driver.find_element_by_name('Email').send_keys('labdhirathore@gmail.com')
    time.sleep(3)
    select =Select(driver.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    driver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

#TestCase 8: Check If Logo Exists
print('TestCase 8: Check If Logo Exists')
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

# TestCase 9: Check the Contact us Page
print("TestCase 9: Check the Contact us Page")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if (info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('Contact Information Correct!')
    else:
        print('Contact Information Incorrect!')

    # assert driver.page_source.find("+65-8402-859, info@thesparksfoundation.sg")
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")



# TestCase 10: Testing the footer content
print("TestCase 10: Testing the footer content")

try:
    (driver.execute_script("arguments[0].scrollIntoView()",driver.find_element_by_xpath("//div[@class='copyright-wthree']/p")))
    driver.find_element_by_xpath("//div[@class='copyright-wthree']/p").text
    time.sleep(2)
    driver.back()
    print("Footer verified successfully")
except NoSuchElementException:
    print("Cannot found any footer")

#TestCase 11: Workshop page
print('TestCase 11: Workshop page')
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    driver.find_element_by_link_text('LEARN MORE').click()
    driver.back()
    time.sleep(3)
    print('Workshop Page Verified Successfully!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')


#TestCase 12: Links Page
print("TestCase 12: Links Page")
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    driver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    driver.find_element_by_link_text('Visit LINKS @TSF').click()
    driver.back()
    time.sleep(3)
    print('LINKS Verfication Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 13: Testing display of iframe "embedded youtube"
print('TestCase 13: Testing display of iframe embedded youtube')

try:

    (driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_tag_name("iframe")))
    if driver.find_element_by_tag_name("iframe").is_displayed():
        driver.switch_to.frame("youtube-video")
        driver.find_element_by_class_name("ytp-large-play-button").click()
        time.sleep(6)
        print("Embedded youtube display verification successful")
except NoSuchElementException:
    print("Cannot found any iframe")



# driver.close()