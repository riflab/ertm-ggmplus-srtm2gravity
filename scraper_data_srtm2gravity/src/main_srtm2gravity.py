'''

SRTM2GRAVITY data scraping
by arif.darmawan@riflab.com
https://github.com/riflab

'''

from bs4 import BeautifulSoup as soup
import requests
import os

def parse_url(url):
    response = requests.get(url)
    page_soup = soup(response.text, "html.parser")
    page = page_soup.find_all('a', href=True)

    list = [item['href'] for item in page]

    return list

def download_file(url, path):
    response = requests.get(url)
    open(path, "wb").write(response.content)

def main(url, path, f_log):
    pages_1 = parse_url(url) 
    download_file(url + pages_1[-1], path + pages_1[-1])
    for i in pages_1[5:]:
        url_1 = url + i
        pages_2 = parse_url(url_1)
        path_2 = path + i

        if not os.path.exists(path_2):
            os.makedirs(path_2)

        for j in pages_2[5:]:
            url_2 = url_1 + j
            print(' >> ' + url_2)
            path_save = path_2 + str(j)
            download_file(url_2, path_save)
            f_log.write(path_save + '\t' + url_1 + '\n')

if __name__ == '__main__':
    
    urls = [
        'https://ddfe.curtin.edu.au/gravitymodels/SRTM2gravity2018/data/FullScaleGravity/',
        'https://ddfe.curtin.edu.au/gravitymodels/SRTM2gravity2018/data/ResidualGravity/'
    ]

    path_save_to = [
        '../data/FullScaleGravity/',
        '../data/ResidualGravity/'
    ]


    f_log = open('../data/log.txt', 'w')

    for url, path in zip(urls, path_save_to):
        if not os.path.exists(path):
            os.makedirs(path)
        main(url, path, f_log)