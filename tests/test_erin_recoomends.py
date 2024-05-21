import allure
import pytest

from pages.erin_recommends_page import * #please refactor
from pages import erin_recommends_page
from pages.main_page import MainPage


@allure.suite("US_001.002 | Testing Erin Recommends Page")
class TestErinRecommends: #please refactor
    @allure.title("TC_001.002.002 | Check redirection to 'Shop Erin Recommends' page by clicking block")
    def test_erin_block_link_redirection(self):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert Erin recommends block presence and Click"):
            page.is_erin_block_present().click()
            page = ErinRecommendsPage(browser=browser)
        with allure.step("Assert current url == Erin Recommends Page url"):
            assert page.get_current_url() == ERIN_RECOMMENDS_URL
        with allure.step("Find header"):
            header = page.is_header_present()
        with allure.step("Assert header contains text 'Erin Recommends'"):
            page.is_element_text_correct(header, "Erin Recommends")

    @allure.title("TC_001.002.003 | Main Page > Erin Recommendations > Paginated Product Catalog Display")
    def test_pagination_controls(self):
        with allure.step("Open Erin Recommends page"):
            page = ErinRecommendsPage(browser=browser)
            page.open_page()
        with allure.step("Scroll to the bottom of controls presence"):
            page.scroll_to_footer()
        with allure.step("Assert pagination control include at least two page numbers and a 'Next' button"):
            assert page.verify_minimum_page_numbers(2), "Less than two page numbers are present."
            page.is_next_button_visible()
        with allure.step("Assert the functionality of the pagination control"):
            page.click_next()
            browser.should(have.url_containing("p=2"))

    @allure.title("TC_001.002.004 | Main Page > Erin Recommendations > Select Number of Products Displayed")
    def test_show_per_page(self):
        with allure.step("Open Erin Recommends page"):
            page = ErinRecommendsPage(browser=browser)
            page.open_page()
        with allure.step("Scroll to and expand the 'Show Per Page' dropdown"):
            page.scroll_to_footer()
            page.expand_show_per_page_dropdown()
        with allure.step("Select a different number to display product per page"):
            page.select_per_page_option(24)
        with allure.step("Assert number of product displayed matches to selection"):
            page.verify_number_of_product_displayed(13,24)

    @pytest.mark.skip
    @allure.title("TC_001.002.005 | Main Page > Erin Recommendations > Arrangement of Products Display")
    def test_switch_to_list_view(self):
        with allure.step("Open Erin Recommends page"):
            page = ErinRecommendsPage(browser=browser)
            page.open_page()
        with allure.step("Switch to list view"):
            page.switch_to_list_view()
        with allure.step("Assert that the layout is now in list view"):
            assert page.is_list_view_activate(), "The product layout did not switch to list view."


@allure.title("TC_001.002.015_1 | Main Page > Erin Recommendations > Adding an Item for Comparison")
def test_add_item_to_compare():
    with allure.step("Open Erin Recommends page"):
        erin_recommends_page.open_page()
        erin_recommends_page.hover_click_item()
        erin_recommends_page.assert_text_of_element(ERL.MESSAGE_ADD_TO_COMPARE, "You added product Jade Yoga Jacket to the ")
        erin_recommends_page.click_text_compare_products()
        erin_recommends_page.assert_text_of_element(ERL.ITEM_JADE_YOGA_JACKET,"Jade Yoga Jacket")