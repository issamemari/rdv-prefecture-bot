import argparse
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def try_guichet(driver: webdriver.Chrome, *, prefecture_url: str, index: int) -> bool:
    driver.get(f"{prefecture_url}/booking/create/989/1")

    radio_elements = driver.find_elements(value="//input[@type='radio']", by=By.XPATH)
    submit = driver.find_element(value="//input[@type='submit']", by=By.XPATH)

    if index > len(radio_elements):
        logger.error(f"Index {index} out of range")
        return

    radio_element = radio_elements[index]
    radio_element.click()
    submit.click()
    driver.implicitly_wait(10)

    if "Il n'existe plus de plage horaire libre" in driver.page_source:
        return False

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prefecture-url", type=str, default="https://pprdv.interieur.gouv.fr"
    )
    args = parser.parse_args()

    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))

    for guichet in [0, 1, 2]:
        if try_guichet(driver, prefecture_url=args.prefecture_url, index=guichet):
            logger.info(f"Guichet {guichet} is available")
            return

    logger.info("No guichet available")


if __name__ == "__main__":
    SystemExit(main())
