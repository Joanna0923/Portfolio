#import selenium
#print("hello world")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker


def test_form(first_name):
    faker = Faker('pl_PL')  # ustawienie generatora w języku polskim

    browser = webdriver.Firefox()
    browser.get('https://charming-custard-8270f9.netlify.app/')

    pesel_elem = browser.find_element(By.ID, 'pesel')
    pesel_elem.send_keys(faker.pesel())

    name_elem = browser.find_element(By.ID, 'name')
    name_elem.send_keys(first_name)

    email_elem = browser.find_element(By.ID, 'email')
    email_elem.send_keys('asia@test.pl')

    pass_elem = browser.find_element(By.ID, 'password')
    pass_elem.send_keys('123456')

    nip_elem = browser.find_element(By.ID, 'nip')
    nip_elem.send_keys('87654321')

    idcard_elem = browser.find_element(By.ID, 'id_card_number')
    idcard_elem.send_keys('111122223333444455556666')

    dropdown_elem = browser.find_element(By.ID, 'dropdown')
    select_elem = Select(dropdown_elem)
    select_elem.select_by_visible_text('Option 2')


# zrobić resztę - napisać kod selenium który wejdzie na tą stronkę wystawioną i wpisze coś w formularzu
# dodawanie zależności na video się klikało tutaj się robi poetry add <nazwa paczki>
# np `pip install Faker` zamianiamy na `poetry add Faker`
# jak uruchomisz od nowa vscode to żeby wejść do środowiska wirtualnego trzeba wspiać `poetry shell`` (znajdując się w katalogu głównym projektu)
# aby przejść do katalogu głównego projektu wpisz `cd /home/joanna/Portfolio/portfolio`
# (portfolio-py3.10) przed zielonym oznacza że jestś w środowisku wirtualnym
# wykonanie kodu: python portfolio/main.py (poza środowiskiem wirtualnym może nie działać)

#kolejność
#1. `cd /home/joanna/Portfolio/portfolio`
#2. `poetry shell
#3. python portfolio/main.py

names = ["Asia","basia","kasia","zosia"]

for first_name in names:
    test_form(first_name)