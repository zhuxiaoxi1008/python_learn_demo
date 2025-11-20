# Python示例（适合测试集成）
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://tutorial.iecube.local/resource/20250522214938999_e21572b146d34b37820538dadf04bccd.html")
driver.save_screenshot("./screenshot.png")  # 支持所有浏览器