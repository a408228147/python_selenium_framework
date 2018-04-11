
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()#关闭当前页面
        cls.driver.quit()#关闭浏览器

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.a_click_news()
        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        newshome.click_sports()
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.click_nba_link()



'''
if __name__ == '__main__':
        unittest.main()
'''