import os
import logging
from datetime import datetime
from selenium.webdriver.common.by import By

# 配置日志
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def setup_logger():
    return logging.getLogger()

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    logging.info(f"截图保存至: {screenshot_path}")
    return screenshot_path