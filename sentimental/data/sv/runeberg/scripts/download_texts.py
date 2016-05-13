from bs4 import BeautifulSoup
import requests, zipfile, io
import re


def extract_text_from_html(html):
    return ''.join(BeautifulSoup(html, 'html.parser').findAll(text=True))


def download_html_zip(zip_file_url, output_file):
    r = requests.get(zip_file_url)
    try:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        for f in z.namelist():
            if f.endswith('.html') and f != 'index.html':
                html = z.read(f).decode('UTF-8')
                text = extract_text_from_html(html)
                corpus_file.write(text + '\n')
        return True
    except Exception as e:
        return False


def site_link_to_html_zip_link(site_link):
    runeberg_id = site_link[1:-1]
    download_url = 'http://runeberg.org/download.pl?mode=html&work=%s' % runeberg_id
    return download_url


def get_swedish_runeberg_downloads():
    url = 'http://runeberg.org/katalog-l.html'
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    links = []
    for row in soup.find_all('tr'):
        tds = list(row.children)
        if len(tds) > 15:
            flag_col = tds[15].contents[0].__str__()
            if 'se.gif' in flag_col:
                links.append((tds[6].get_text(), tds[6].find('a')['href']))
    return links

corpus_file = open('corpus.txt', 'w')

links = get_swedish_runeberg_downloads()
i = 1
for (name, link) in links:
    zip_link = site_link_to_html_zip_link(link)
    if download_html_zip(zip_link, corpus_file):
        print('%i - %s (%s)' % (i, name, link))
        i = i + 1

corpus_file.close()
