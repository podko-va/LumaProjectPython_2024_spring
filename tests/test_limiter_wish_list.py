import allure
from pages import limiter_item

@allure.link('https://trello.com/c/zKMpEsGc')
@allure.feature('Limiter "Show on Page"')
@allure.title('Verify filter “Show on page')
def test_limiter_options():
    limiter_item.preconditions()
    limiter_item.change_limit_to_20()
    limiter_item.items_number()

