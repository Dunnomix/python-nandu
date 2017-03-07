#!/usr/bin/python3
# coding: utf-8

# Main module
from selenium import webdriver

# Some common exceptions
# Raised when the element is no longer attached to the DOM
from selenium.common.exceptions import StaleElementReferenceException

# Raised when the element is not displayed for the user to interact with
from selenium.common.exceptions import ElementNotVisibleException

# Raised when the element is not found
from selenium.common.exceptions import NoSuchElementException

# Element helper locator
from selenium.webdriver.common.by import By

# Module for sendking keyboard-like events
from selenium.webdriver.common.keys import Keys

# Module for waiting, used with expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

# this will help us find the profile path folder
import os

# Dict dumping
import json

# To call a browser we just simply
# driver = webdriver.Firefox()  # selenium.webdriver.Firefox

# There are other drivers available
# driver.webdriver.Chrome() # Eats RAM
# driver = webdriver.PhantomJS()  # You're just gonna love this, advanced
#
# Everytime you create a webdriver instance like this
# at least for Firefox or Chrome, a new profile folder is created.
# This is done in order to provide a clean, preferences-free browser
# No addons, no history, no nothing.
#
# This can be good if you want it, but keep in mind that a temporal
# new folder will be created.
# doing experiments on windows i filled a few GB with these folders
# so whatch out for that.
#
# In order to avoid that you can tell the webdriver to use a profile folder
# To find our your profiles folder in firefox simply call the program
# $ firefox -p
#
# With that tool you can manage your profile folders
#
# For chrome
# I.O.U
#
# With this snippet of code i'm able to locate the profile folders for firefox
# in windows/linux platforms (not tested on osx)
# You can even know if there are severall profiles and be able to select one
#
# Mozilla firefox profile
# if using linux
# ~/.mozilla/firefox/something.default
# if using windows
# %appdata%\\mozilla\\firefox\\profiles\\something.default
#
# If turns out we are on windows
if os.name == "nt":

    # locate the profile, no mistery here
    prodir = os.path.join(
        os.getenv('APPDATA'), "mozilla", "firefox", "profiles"
        )
    profiles = os.listdir(
        os.path.join(prodir, "profiles")
        )

    # Multi profile filtering
    if len(profiles) > 1:
        print "Several profiles:"

        # present to the user
        for i, profile in enumerate(profiles):
            print "{}: {}".format(i, profile)
        print "Selecting the first"
        profilepath = os.path.join(prodir, profiles[0])
    else:
        profilepath = os.path.join(prodir, profiles[0])

# If we are on UNIX
else:

    # Get the profile folder from the user folder
    prodir = os.path.join(os.path.expanduser('~'), ".mozilla", "firefox")
    profiles = []

    # Determine if its a profile folder, or a file
    for d in os.listdir(prodir):
        if os.path.isdir(os.path.join(prodir, d)):
            profiles.append(d)

    # Multi profile filtering
    if len(profiles) > 1:
        print " Several profiles:"

        # filter crash reports
        for i, profile in enumerate(profiles):
            if "Crash" in profile:
                profiles.pop(i)

        # present to the user
        for i, profile in enumerate(profiles):
            print "{}: {}".format(i, profile)
        print "Selecting the first"
        profilepath = os.path.join(prodir, profiles[0])
    else:
        profilepath = os.path.join(prodir, profiles[0])

# Great now i have your firefox profile path, lets load it up
driver.webdriver.Firefox(profilepath)

# now lets open a webpage
driver.get("http://en.wikipedia.org")

# Find an element (singular)
# TIP: id on html elements must be unique, preffer id before class, name or any
search = driver.find_element_by_xpath("//input[@id='searchInput']")
# This is xpath, i find it more useful than any other locating method
# You may also use:
search = driver.find_element_by_id("searchInput")

# We are now able to send some keys
search.send_keys("selenium webdriver" + Keys.ENTER)

# Finding elements (Plural)
# Here i give you two ways, i always preffer xpath way
# altough you have to type a little bit more
results = driver.find_element_by_xpath("//ul[@class='mw-search-results']")
results = driver.find_element_by_class_name("mw-search-results")

# Notice the dot in the xpath, it indicates 'from this element'
# and not from the <html> element (global search)
# results.find_elements_by_xpath(".//li")

__results = []
# without xpath
for result in results.find_elements_by_tag_name("li"):
    # now lets get scraping
    anchor = result.find_element_by_tag_name("a")
    link = anchor.get_attribute("href")
    title = anchor.get_attribute("title")
    #
    matched_word = result.find_element_by_xpath(".//span").text
    description = result.find_element_by_class_name("searchresult").text
    meta = result.find_element_by_class_name("mw-search-result-data").text
    #
    # Sometimes an element won't return anything with text, you can use this
    meta_xpath = ".//div[@class='mw-search-result-data']"
    meta_item = result.find_element_by_xpath(meta_xpath)
    meta = meta_item.get_attribute("innerHTML")
    #
    _result = {
        "link": link,
        "title": title,
        "matched_word": matched_word,
        "description": description,
        "meta": meta
    }
    print json.dumps(_result, indent=4)
    __results.append(_result)

csvline = "{};{};{};{}"
for _result in __results:
    print csvline.format(
        _result["title"],
        _result["link"],
        _result["matched_word"],
        _result["meta"]
        )