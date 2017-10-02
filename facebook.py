#-*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import sys
import codecs
import os
import cStringIO

reload(sys)
sys.setdefaultencoding('utf-8')

__facebook_PRIVATE_FILE_NAME__ = "idpw.txt"
__facebook_DATA_FILE_NAME__    = "result.txt"
__facebook_EMAIL__    = ""
__facebook_PASSWORD__ = ""
facebook_data_file = codecs.open(__facebook_DATA_FILE_NAME__, "w", "utf-8")
driver = webdriver.Firefox()

def quit():
	driver.quit()
def is_facebook_login_page_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
def is_facebook_login_done(driver):
	return driver.find_element_by_id('logoutMenu') != None
def make_string_pretty(string):
	return string.strip(' \t\n\r')
def get_facebook_email_password():
	print("START get_facebook_email_password")
	facebook_private_file = open(__facebook_PRIVATE_FILE_NAME__, 'r')
	global __facebook_EMAIL__
	global __facebook_PASSWORD__
	__facebook_EMAIL__ = facebook_private_file.readline()
	__facebook_PASSWORD__ = facebook_private_file.readline()
	__facebook_EMAIL__ = make_string_pretty(__facebook_EMAIL__)
	__facebook_PASSWORD__ = make_string_pretty(__facebook_PASSWORD__)
	facebook_private_file.close()
	os.remove(__facebook_PRIVATE_FILE_NAME__) #### 
	print(__facebook_PRIVATE_FILE_NAME__ + " was deleted")
	print("END get_facebook_email_password")
def facebook_login():
	print("START facebook_login")
	get_facebook_email_password()

	driver.get('https://www.facebook.com/')
	wait = ui.WebDriverWait(driver, 10)
	wait.until(is_facebook_login_page_loaded)
	email_element = driver.find_element_by_id("email")
	email_element.send_keys(__facebook_EMAIL__)
	password_element = driver.find_element_by_id("pass")
	password_element.send_keys(__facebook_PASSWORD__)
	password_field = driver.find_element_by_id("pass")
	password_field.send_keys(Keys.RETURN)

	wait = ui.WebDriverWait(driver, 10)
	wait.until(is_facebook_login_done)
	page_source = driver.page_source
	profile_idx = page_source.find("title=\"Profile\"")
	if profile_idx < 0:
		print("ERR ON LOGIN FUNCTION 1")
		sys.exit(-1)
	profile_string = page_source[(profile_idx-70):profile_idx]
	profile_idx = profile_string.find('href=\"https://www.facebook.com/')
	if profile_idx < 0:
		print("ERR ON LOGIN FUNCTION 2")
		sys.exit(-1)
	global profile_name
	profile_name = ""
	profile_idx += len('href=\"https://www.facebook.com/')
	while '"' != profile_string[profile_idx]:
		profile_name += profile_string[profile_idx]
		profile_idx += 1
	print("END facebook_login")
def facebook_notifications_off():
	print("START facebook_notifications_off")
	sleep(10)
	actions = ActionChains(driver)
	actions.send_keys(Keys.TAB).perform()
	actions.send_keys(Keys.SPACE).perform()
	print("END facebook_notifications_off")
def facebook_please_off():
	print("Please Turn Notifications Off")
	sleep(10)
def facebook_activity_log():
	print("START facebook_activity_log")
	if len(profile_name) < 1:
		print("ERR ON ACTIVITY LOG FUNCTION 1")
		sys.exit(-1)
	print("YOUR PROFILE NAME : ")
	print(profile_name)
	activity_link = 'https://www.facebook.com/' + profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
	driver.get(activity_link)
	sleep(2)
	print("END facebook_activity_log")
def facebook_scroll_down_once():
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	sleep(1)
def facebook_scroll_down():
	print("START facebook_scroll_down")
	count = 0
	while count < 20:
		facebook_scroll_down_once()
		count += 1
		print(count)
	print("END facebook_scroll_down")
def facebook_mining():
	print("START facebook_mining")
	all_children_by_css = driver.find_elements_by_css_selector("*")
	all_children_by_xpath = driver.find_elements_by_xpath(".//*")
	for ele in all_children_by_css:
		#print(ele.get_attribute("innerHTML"))
		isprinted = 0
		try:
			facebook_data_file.write(str(ele.get_attribute("innerHTML")).decode("UTF-8"))
			isprinted = 1
		except:
			print("Try again to print source code")
		try:
			if 1 != isprinted:
				facebook_data_file.write(str(ele.get_attribute("innerHTML")))
			isprinted = 1
		except:
			print("Failed to print source code")
	for ele in all_children_by_xpath:
		#print(ele.get_attribute("innerHTML"))
		isprinted = 0
		try:
			facebook_data_file.write(str(ele.get_attribute("innerHTML")).decode("UTF-8"))
			isprinted = 1
		except:
			print("Try again to print source code")
		try:
			if 1 != isprinted:
				facebook_data_file.write(str(ele.get_attribute("innerHTML")))
			isprinted = 1
		except:
			print("Failed to print source code")
	facebook_data_file.close()
	print("END facebook_mining")

facebook_login()
facebook_activity_log()
#facebook_notifications_off()
facebook_please_off()
facebook_scroll_down()
facebook_mining()
quit()
print("FIN")
