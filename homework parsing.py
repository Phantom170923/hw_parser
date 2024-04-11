from bs4 import BeautifulSoup
import csv
import requests


def write_cmc_top(url):

    list_name_crypt = []
    list_capitalization = []
    list_capitalization_int = []
    list_percent = []

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        list_name = soup.find_all('p', class_='sc-4984dd93-0 kKpPOn')
        list_cap = soup.find_all('span', class_='sc-7bc56c81-1 bCdPBp')
        for name, cap in zip(list_name, list_cap):
            list_name_crypt.append(name.text)
            list_capitalization.append(cap.text)

    for i in list_capitalization:
        cap_int = i.split(',')
        cap_int = ''.join(cap_int)
        cap_int = cap_int.replace('₽', '')
        cap_int = int(cap_int)
        list_capitalization_int.append(cap_int)

    total = sum(list_capitalization_int)

    for j in list_capitalization_int:
        percent = j/total * 100
        list_percent.append(str(int(percent)) + '%')

    with open("11.45 11.04.2024.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=" ", lineterminator="\r")
        file_writer.writerow(["Name", "MC", "MP"])
        for i in range(len(list_name_crypt)):
            file_writer.writerow([list_name_crypt[i], list_capitalization[i], list_percent[i]])


write_cmc_top('https://coinmarketcap.com/ru/')



