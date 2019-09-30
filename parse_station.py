import requests
import re
from pprint import pprint
import json

def main():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9109'
    r=requests.get(url,verify=False)
    r.encoding = 'UTF-8'
    pattern=u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    stations=re.findall(pattern,r.text)
    pprint(dict(stations), indent=4)





if __name__=='__main__':
    main();