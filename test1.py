#import selenium
#print("hello world")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = webdriver.Firefox()
browser.get('https://charming-custard-8270f9.netlify.app/')

pesel_elem = browser.find_element(By.ID, 'Pesel')
pesel_elem.send_keys('88092316746')

name_elem = browser.find_element(By.ID, 'Name')
name_elem.send_keys('Asia')

email_elem = browser.find_element(By.ID, 'Email')
email_elem.send_keys('asia@test.pl')

pass_elem = browser.find_element(By.ID, 'Password')
pass_elem.send_keys('123456')

nip_elem = browser.find_element(By.ID, 'Nip')
nip_elem.send_keys('87654321')

idcard_elem = browser.find_element(By.ID, 'Id card number')
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
