import requests
import re
import csv


def getData(url):
    response = requests.get(url)
    # find all 'a' tag and keep in a_tag_list
    a_tag_list = re.findall(r'<a\s.*?</a>', response.text)
    content_list = []
    for tag in a_tag_list:
        # find content between <a> and </a>
        match = re.search(r'<a[^>]*>(.*?)</a>', tag)
        if match:
            content_list.append(match.group(1))  # keep content in content_list
    result = []
    for content in content_list:
        # find content that start with วัด
        match = re.search(r'^วัด.*', content)
        if match:
            result.append(match.group(0))  # keep result
    result = result[:-4]  # The last 4 result are unneeded.
    return result


def createFile(fileName, url):
    data = getData(url)
    filename = fileName + '.csv'
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for item in data:
            writer.writerow([item])
