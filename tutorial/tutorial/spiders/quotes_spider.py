# -*- coding: utf-8 -*-

import scrapy
import re

import os
from selenium import webdriver
import time

class QuotesSpider(scrapy.Spider):
    name = "nfl"
    start_urls = [
        'https://mobile.betonline.ag/sports/offerings?s=Football&l=NFL&p=0',
    ]

    def parse(self, response):

        teams = []
        lines = []
        ids = []
        dates = []

        for t in response.css('td.team'):
            t1 = t.css('span::text').extract_first()
            if t1 not in teams:
                teams.append(t1)


        for l in response.css('td.point-line'):
            l1 = l.css('span::text').extract_first()
            lines.append(l1)


        databindfile = open('databinds.txt', 'w')





        for name in response.xpath('//a[@href="#"]/@data-bind').extract():

            result1 = re.split("\{", name)
            if len(result1) < 2:
                continue
            result2 = re.split("\}", result1[1])

            result3 = re.split(":", result2[0], 1)
            result4 = re.split("\'", result3[1])
            finalResult = re.split("\|", result4[1])
            print finalResult
            if finalResult[2] in ids:
                continue
            else:
                #print( finalResult[2] + "   " + finalResult[17])
                ids.append(finalResult[2])
                dates.append(finalResult[17])
                #ids.append(finalResult[2])
                #dates.append(finalResult[17])



        databindfile.close()

        comboStr = []

        f = open('teams.txt', 'w')
        f.truncate()




        i = 0
        while i < len(ids):
            line = lines[i]



            line = line.replace(u"½", ".5")

            f.write(teams[i] + "," + line + "," + ids[i] + "," + dates[i] + "\n")
            i += 1


        f.close()




class LoginSpider(scrapy.Spider):
    name = 'login'
    start_urls = [
        'https://mobile.betonline.ag/login'

    ]

    def __init__(self):
        chromedriver = "/Users/creich/Downloads/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def parse(self, response):
        self.driver.get('https://mobile.betonline.ag/login')



        nextPage = self.driver.find_element_by_xpath('//input[@value="Login"]')

        user = self.driver.find_element_by_xpath('//input[@id="Username"]')
        user.send_keys("christopherl.reich@gmail.com")
        time.sleep(2)
        password = self.driver.find_element_by_xpath('//input[@id="password"]')
        password.send_keys("7897897Qq")
        time.sleep(2)
        nextPage.click()
        time.sleep(2)
        url = 'https://mobile.betonline.ag/reports/pending-wagers'


        self.driver.get(url)

        time.sleep(2)





        self.driver.close()


    def parse2(self, response):
        print "Made it here"



    def after_login(self, response):
        # check login succeed before going on

        if "Invalid Login" in response.body:
            self.logger.error("Login failed")
            return

        else:

            return Request(url="https://mobile.betonline.ag/reports/pending-wagers",
               callback=self.parse_pending)



    def parse_pending(self, response):
        arrs = []
