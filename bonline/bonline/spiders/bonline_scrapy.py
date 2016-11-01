import scrapy

class LoginSpider(scrapy.Spider):
    name = 'bonline_login'
    start_urls = ['https://www.betonline.ag/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'CustomerID': 'christopherl.reich@gmail.com', 'Password': '7897897Q'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
