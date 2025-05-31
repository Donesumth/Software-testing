import keyword

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from utils import setup_logger, take_screenshot
import time

# 日志
logger = setup_logger()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # 或 webdriver.Firefox()
    driver.implicitly_wait(10)  # 隐式等待
    yield driver
    driver.quit()


def test_search_valid_keyword(driver):
    logger.info("开始测试：有效关键词搜索")
    driver.get("https://book.douban.com/")

    # 定位搜索框，输入关键词
    search_box = driver.find_element(By.XPATH, "//input[@name='search_text']")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.ENTER)

    # 等待结果加载
    time.sleep(2)

    # 断言结果
    results = driver.find_elements(By.XPATH, "//div[@class='item']")
    assert len(results) > 0, "未找到搜索结果"
    assert "Python" in driver.page_source, "搜索结果不包含关键词"
    logger.info("有效关键词搜索测试通过")


def test_search_invalid_keyword(driver):
    logger.info("开始测试：无效关键词搜索")
    driver.get("https://book.douban.com/")

    # 输入无效关键词
    search_box = driver.find_element(By.XPATH, "//input[@name='search_text']")
    search_box.send_keys("@#$%")
    search_box.send_keys(Keys.ENTER)

    # 等待结果加载
    time.sleep(2)

    # 断言无结果或提示
    no_result = driver.find_elements(By.XPATH, "//div[contains(text(), '没有找到')]")
    assert len(no_result) > 0 or len(driver.find_elements(By.XPATH, "//div[@class='item']")) == 0, "无效关键词应无结果"
    logger.info("无效关键词搜索测试通过")


def test_search_empty_keyword(driver):
    logger.info("开始测试：空关键词搜索")
    driver.get("https://book.douban.com/")

    # 输入空关键词
    search_box = driver.find_element(By.XPATH, "//input[@name='search_text']")
    search_box.send_keys("")
    search_box.send_keys(Keys.ENTER)

    # 等待结果加载
    time.sleep(2)

    # 断言提示
    no_result = driver.find_elements(By.XPATH, "//div[contains(text(), '请输入')]")
    assert len(no_result) > 0 or len(driver.find_elements(By.XPATH, "//div[@class='item']")) == 0, "空关键词应无结果"
    logger.info("空关键词搜索测试通过")

    logger.info(f"搜索关键词：{keyword}")