'''

GGMPLUS data scraping
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
    print(pages_1[5:])
    
    for i in pages_1[5:]:
        url_1 = url + i
        print(' >> ' + url_1)
        path_save = path + str(i)
        download_file(url_1, path_save)
        f_log.write(path_save + '\t' + url_1 + '\n')

if __name__ == '__main__':

    urls = [
        'https://ddfe.curtin.edu.au/gravitymodels/GGMplus/data/eta/',
        'https://ddfe.curtin.edu.au/gravitymodels/GGMplus/data/xi/',
        'https://ddfe.curtin.edu.au/gravitymodels/GGMplus/data/dg/',
        'https://ddfe.curtin.edu.au/gravitymodels/GGMplus/data/geoid/',
        'https://ddfe.curtin.edu.au/gravitymodels/GGMplus/data/ga/'
    ]

    path_save_to = [
        '../data/eta/',
        '../data/xi/',
        '../data/dg/',
        '../data/geoid/',
        '../data/ga/'
    ]
    
    f_log = open('../data/log.txt', 'w')

    for url, path in zip(urls, path_save_to):
        if not os.path.exists(path):
            os.makedirs(path)
        main(url, path, f_log)