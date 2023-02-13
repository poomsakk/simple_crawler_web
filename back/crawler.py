import requests
from bs4 import BeautifulSoup
import re
import csv


def starts_with_wat(text):
    return bool(re.match(r'^วัด.*', text))


def getData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result_data = []
    for tag in soup.find_all('a'):
        text_each_tag = str(tag.contents[0])
        if (starts_with_wat(text_each_tag)):
            result_data.append(text_each_tag)
    result_data = result_data[:-4]
    return result_data


def createFile(fileName, url):
    data = getData(url)
    filename = fileName + '.csv'
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for item in data:
            writer.writerow([item])
