import selenium.webdriver
from scrapy.http import HtmlResponse
import scrapy
class seleniummiddleware(object):
    
    def process_request(self,request,spider):
        driver = selenium.webdriver.Chrome()
        #print(request.url)
        #print("你好")
        driver.get(request.url)
        content = driver.page_source.encode('utf-8')
        url = request.url
        driver.quit()
        return HtmlResponse(url, encoding='utf-8', body=content, request=request)
       
