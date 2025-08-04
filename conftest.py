
import pytest
from utils.base_driver import get_driver
from utils import config

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(config.BASE_URL)
    yield driver
    driver.quit()
