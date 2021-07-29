
import schedule
import webbrowser
import time
from pykeyboard import PyKeyboard

from selenium import webdriver
from getpass import getpass


username = ["20021648","20021095"]
password = ["Siddh@cybertron12","Siddh@cybertron12"]
k = 0
while k!=2:
    li = ['http://45.116.207.203/moodle/mod/attendance/view.php?id=5431']

    

    driver = webdriver.Chrome(
        "C:\\Users\\ashub\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
    driver.get("http://45.116.207.203/moodle/login/index.php")

    username_textbox = driver.find_element_by_id("username")
    username_textbox.send_keys(username[k])

    password_textbox = driver.find_element_by_id("password")
    password_textbox.send_keys(password[k])

    k = k+1


    login_button = driver.find_element_by_id("loginbtn")
    login_button.submit()

    driver.get(li[0])

    submit_button = driver.find_element_by_link_text(
        "Submit attendance").click()

    checkbox = driver.find_element_by_name('status') # locate checkbox
    if not checkbox.is_selected():  # check if checkbox is already selected
        checkbox.click()


    save_button = driver.find_element_by_id("id_submitbutton")
    save_button.submit()

    driver.close()
