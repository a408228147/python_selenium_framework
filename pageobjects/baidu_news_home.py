from framework.base_page import BasePage

class NewsHomePage(BasePage):
    # 点击体育新闻入口
    sports_link = "link_text=>体育"

    def click_sports(self):
        self.a_click_element(self.sports_link)
        self.time_sleep(2)