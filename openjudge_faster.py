import time
import asyncio
import pyppeteer as pyp
async  def antiAntiCrawler(page):
    await page.setUserAgent('Mozilla/5.0(Windows NT 6.1;\
        Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/78.0.3904.70 Safari/537.36          ')
    await page.evaluateOnNewDocument(
        '() =>{ Object.defineProperties(navigator,\
        webdriver:{ get: () => false}})}')
async def getOjSourceCode(loginUrl):
    width,height=1400,800
    browser=await pyp.launch(headless=False,userdataDir="C:\vscode\All kinds of\
                              projects\python\python_spider",\
                             args=[f'--window-size={width},{height}'])
    page=await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width':width,'height':height})
    await page.goto(loginUrl)
    element=await page.querySelector("#email")
    await element.type("983710920@qq.com")
    element=await page.querySelector("#password")
    await element.type("8881122wdm")
    element=await page.querySelector("#main > form > div.user-login > p:nth-child(2) > button")
    await element.click()
    await page.waitForSelector("#main>h2",timeout=3000)
    
    element=await page.querySelector("#userMenu > li:nth-child(2) > a")
    await element.click()
    await page.waitForNavigation()
    elements=await page.querySelectorAll(".result-right")
    page2=await browser.newPage()
    await antiAntiCrawler(page2)
    for element in elements[:2]:
        obj=await element.getProperty("href")
        url=await obj.jsonValue()
        await page2.goto(url)
        element=await page2.querySelector("pre")
        obj=await element.getProperty("innerText")
        text=await obj.jsonValue()
        print(text)
        print('-------------------')
    await browser.close()
def main():
    url='http://openjudge.cn/auth/login/'
    asyncio.get_event_loop().run_until_complete(getOjSourceCode(url))
main()