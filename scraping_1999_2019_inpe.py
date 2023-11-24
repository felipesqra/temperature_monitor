from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_data_selenium(year):
    url = "http://sinda.crn.inpe.br/PCD/SITE/novo/site/historico/index.php"

    # Initialize a headless browser (you may need to download the appropriate driver for your browser)
    driver = webdriver.Chrome(executable_path='chromedriver')

    try:
        driver.get(url)


        # Fill in the form data using JavaScript
        script = f'''
            document.getElementsByName("id")[0].value = '32546';
        '''
        driver.execute_script(script)

# ...
        # Wait for the "Continuar >>" button to be present on the next page
        continue_button_present = EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))
        WebDriverWait(driver, 10).until(continue_button_present)

        # Click on the "Continuar >>" button to go to the next page
        continue_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
        continue_button.click()


# ...   # Wait for the date fields to be present on the page
        date_fields_present = EC.presence_of_element_located((By.NAME, "dia_inicial"))
        WebDriverWait(driver, 5).until(date_fields_present)


        # Add code here to fill in the form data on the second page using JavaScript or other methods
        script2 = f'''
            document.getElementsByName("dia_inicial")[0].value = '01';
            document.getElementsByName("mes_inicial")[0].value = '01';
            document.getElementsByName("ano_inicial")[0].value = '{year}';
            document.getElementsByName("dia_final")[0].value = '30';
            document.getElementsByName("mes_final")[0].value = '12';
            document.getElementsByName("ano_final")[0].value = '{year}';
        '''
        driver.execute_script(script2)
        
        continue_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
        continue_button.click()
        
        
        time.sleep(5)


    finally:
        # Close the browser
        driver.quit()

# Set the range of years you want to download
start_year = 1999
end_year = 2019

# Call the function to download data using Selenium
for year in range(start_year, end_year+1):
    download_data_selenium(year)
