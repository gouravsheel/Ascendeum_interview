from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_element(driver, by, selector, timeout=15):
    """Wait for an element to be clickable and click it."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )
    element.click()
    print(f"Clicked element: {selector}")

def print_difficulty_status(driver):
    """Find and print the difficulty level text."""
    status = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "GamePostStart_info__Rwi7G"))
    )
    for stat in status:
        level = stat.text
        if "Difficulty" in level:
            print(level.replace("Difficulty", "").strip())

try:
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # Uncomment to enable headless
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    difficulty_buttons = {
        "easy": '#__next > div.container.game-container > div > div.CrossBits_game-view-flex-container__X4OLG > div > div > div.GamePostStart_game-flex-wrapper__A8EB6.GamePostStart_game-paused__QbUfP > div.GamePostStart_game-play-wrapper__AuWHX.game-play-wrapper > div.GamePostStart_new-game-difficulty-container__lCCK9 > div > div.GamePostStart_difficulty-wrapper__p6RQ4 > ul > li.GamePostStart_difficulty-selected__WbDcN',
        "medium": '#__next > div.container.game-container > div > div.CrossBits_game-view-flex-container__X4OLG > div > div > div.GamePostStart_game-flex-wrapper__A8EB6.GamePostStart_game-paused__QbUfP > div.GamePostStart_game-play-wrapper__AuWHX.game-play-wrapper > div.GamePostStart_new-game-difficulty-container__lCCK9 > div > div.GamePostStart_difficulty-wrapper__p6RQ4 > ul > li:nth-child(2)',
        "hard": '#__next > div.container.game-container > div > div.CrossBits_game-view-flex-container__X4OLG > div > div > div.GamePostStart_game-flex-wrapper__A8EB6.GamePostStart_game-paused__QbUfP > div.GamePostStart_game-play-wrapper__AuWHX.game-play-wrapper > div.GamePostStart_new-game-difficulty-container__lCCK9 > div > div.GamePostStart_difficulty-wrapper__p6RQ4 > ul > li:nth-child(3)'
    }

    for i in range(10):
        driver.get("https://mathup.com/")
        time.sleep(5)

        click_element(driver, By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]')

        click_element(driver, By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]')

        click_element(driver, By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]')

        for level, selector in difficulty_buttons.items():
            click_element(driver, By.CSS_SELECTOR, selector)
            time.sleep(3)
            print(f"Selected {level} difficulty")
            print_difficulty_status(driver)
            time.sleep(2)

except Exception as e:
    print("An error occurred:", e)

finally:
    try:
        driver.quit()
    except:
        pass
