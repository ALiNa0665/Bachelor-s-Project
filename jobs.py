
import numpy as np
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

load_url_from_csv = False
idxs = np.arange(0,920,10) # change 920 based on Vestas job page (e.g., if the # jobs becomes 846, change to 840, etc)
def get_urls(idxs, save=True):
    ''' A function to get all urls from the general Vestas jobs page '''
    urls = []
    for i in idxs:
        print(f'From row {i} of {max(idxs)}')
        url = f'https://careers.vestas.com/search?q=&sortColumn=referencedate&sortDirection=desc&startrow={i}'
        req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'})
        response = urlopen(req)
        html = BeautifulSoup(response)
        table = html.find(lambda tag: tag.name=='table') # find the table
        c_urls = 0
        for a in table.find('tbody').find_all('a', href=True): # find all the urls that contain "job"
            if ('/job' in a['href']):
                c_urls += 1
                if c_urls % 2 != 0:
                    urls.append('https://careers.vestas.com' + a['href'])
        print(len(urls))
    if save:
        pd.DataFrame(urls, columns=['url']).to_csv('job_urls.csv') # store it so we don't have to compute that again
    return urls

def return_data(url):
    ''' A function to return requisition id and competencies from specific job page (url) '''
    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'})
    response = urlopen(req)
    html = BeautifulSoup(response)
    if 'requisition id' in html.get_text().lower() and 'competencies' in html.get_text().lower(): # check that the fields we look for are in there
        req_id = int(html.get_text().lower().split('requisition id')[1].split('\n')[2]) # get req id
        competencies = html.get_text().lower().split('competencies')[1].split('what we offer')[0].split('\n\xa0')[0] # get whatever is between competencies and "what we offer"
        return req_id, competencies
    else:
        print(f'Not working: {url}')
        return None


if __name__=='__main__':
    if load_url_from_csv:
        urls = pd.read_csv('job_urls.csv')['url']
    else:
        urls = get_urls(idxs, save=True)
    data = []
    for i, u in enumerate(urls):
        print(f'{i} out of {len(urls)-1}')
        outs = return_data(u)
        if outs is not None:
            data.append(outs)
    pd.DataFrame(data, columns=['req_id', 'competencies']).to_excel('job_ads.xlsx')