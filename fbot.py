import discord
from discord.ext import commands
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


custom = commands.Bot(command_prefix='.')


@custom.command()
async def gg(ctx, arg):  # .bot reads on gg pref
    await ctx.send("looking for " + arg)

    # local chromedriver path
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # changing site will break the selenium part
    driver.get("https://fitgirlrepacks.co/")
    print(driver.title)

    s1 = driver.find_element_by_class_name("search-toggle")
    s1.click()

    search = driver.find_element_by_class_name("search-field")
    search.clear()

    name = arg
    gamepage = 'f'
    search.send_keys(name)
    search.send_keys(Keys.RETURN)

    sp = driver.find_element_by_class_name("page-title")
    temp = str(sp.text)
    print(temp)
    if '0' in temp:
        await ctx.send('not found')
        driver.quit()

    gamepage = driver.find_element_by_class_name("entry-title")

    main = driver.window_handles[0]
    gamepage.click()
    time.sleep(3)

    magnet = driver.find_element_by_link_text("magnet")
    link = [magnet.get_attribute('href')]

    await ctx.send('found magnet converting to link')
    mag = link[0]
    driver.get("https://tormag.ezpz.work/")  # changing will break the code
    em = driver.find_element_by_class_name('magnetLinks')

    em.send_keys(mag)
    time.sleep(3)

    ah = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/button')
    ah.click()
    time.sleep(2)
    c2 = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/div/p[2]/textarea")

    # driver.get("final")

    text = c2.get_attribute('value')
    await ctx.send('here is your link ||' + text + '||')
    driver.quit()


# token dorime
custom.run('YOUR TOKEN HERE')
