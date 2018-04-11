
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

    def test_func(self):
        bh = HomePage(self.driver)
        bh.time_sleep(2)
        #bh.mouse_right_click("link_text=>新闻")
      #  bh.time_sleep(2)
       # print(bh.get_text("name=>tj_trnews"))
       # print(bh.get_window_title())
       # print(bh.element_get_attribute("link_text=>新闻","class"))
        #bh.time_sleep(2)
       # bh.browser_back()
       # bh.time_sleep(2)
       # bh.browser_forward()
       # bh.time_sleep(2)
       # bh.browser_back()



        bh.get_add_login_cookies("445e2903f353a1568694cb0b155ad912","lc4OFh5dU9xMGtlR1lsVX5ZWWxmdzVuMDJ-MFJwYS00ZjQtdGhqb3RpMGp-UE5hQVFBQUFBJCQAAAAAAAAAAAEAAAC2XlBn0fLR-tH60foAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACNvzFojb8xaR")
        bh.F5()
        bh.a_click_element("link_text=>新闻")
        bh.time_sleep(2)
        index_handle=bh.get_current_window_handle()
        handles = bh.get_window_handles()
        for handle in handles:
             if handle!=index_handle:
                 bh.switch_to_other_window(handle)
             bh.time_sleep(2)
        new_handle=bh.get_current_window_handle()
        bh.a_click_element("p=>亚洲论坛")
        bh.time_sleep(2)
        handles = bh.get_window_handles()
        for handle in handles:
            if handle != index_handle and handle != new_handle:
                bh.switch_to_other_window(handle)
            bh.time_sleep(2)
        a = bh.element_get_attribute("xpath=>//div[@class='main-aticle']/p[4]","innerText")
        print(a)

        bh.time_sleep(2)