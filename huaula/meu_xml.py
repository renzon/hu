import requests
import xmltodict


def cds():
    response = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')
    response.text
    ret = []
    for cd in xmltodict.parse(response.text)['CATALOG']['CD']:
        ret.append(cd['TITLE'])
    return ret


if __name__ == '__main__':
    print(cds())
