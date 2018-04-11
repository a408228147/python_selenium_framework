from framework.base_page import BasePage


class SportNewsHomePage(BasePage):
    # NBA入口
    nba_link = "xpath=>//div[@class='schedule clearfix']/ul/li/a"

    def click_nba_link(self):
        self.a_click_element(self.nba_link)
        self.time_sleep(2)