from selenium import webdriver
import chromedriver_binary
import time
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
from selenium.webdriver.common.by import By

def check(key_request):
    browser = webdriver.Chrome()
    browser.get('https://rabota.by/')

    search_input = browser.find_element(By.ID, 'a11y-search-input')
    search_input.send_keys(key_request)
    search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
    search_button.click()

    links = browser.find_elements(By.CSS_SELECTOR, '[class="bloko-header-section-3"] a')
    vacancy_name = browser.find_elements(By.CLASS_NAME, 'serp-item__title')
    employers = browser.find_elements(By.CLASS_NAME, 'vacancy-serp-item__meta-info-company')

    count = 0
    vacancies = ''
    for name, employer, res_link in zip(vacancy_name, employers, links):
        if count < 5:
            vacancy = str(f'Найдена вакансия "{name.text}" от {employer.text}. Для просмотра перейдите по ссылке {res_link.get_attribute("href")}.')
            vacancies += vacancy + '\n\n'
            count += 1
    return vacancies

    time.sleep(100)
    browser.close()

