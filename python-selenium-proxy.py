### Selenium Remote WebDriver with proxy coded by thuannvn (Skype)
### For security i changed ip_selenium_server, proxy. You can input yours to make it works

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time 
import pprint

from BeautifulSoup import BeautifulSoup
import urllib2
import re

# Global configuration
se_server = 'http://ip_selenium_server:4444/wd/hub'
proxy = 'ip:port'
start_url = 'http://www.domain.com'

# Initialize Firefox Browser
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy":proxy,
    "ftpProxy":proxy,
    "sslProxy":proxy,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

driver = webdriver.Remote(command_executor=se_server, desired_capabilities=DesiredCapabilities.FIREFOX)
driver.delete_all_cookies()

# Navigate to start_url
driver.get(start_url)
html_page = driver.page_source

soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	url = link.get('href')
	if (url.startswith( 'http://www.domain.com/abc/' )):
		print url
		driver.get(url)

driver.quit()
