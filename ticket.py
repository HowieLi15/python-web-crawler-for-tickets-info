""" Train Tickets query via cli

Usage:
    tickets [-gdtkz] <from> <to> <date>


Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
"""
from tkinter import *
from docopt import docopt;
import re
from pprint import pprint
import requests
import json
from Traincollection import Traincollection



def GUI():
    top = Tk()
    top.geometry('500x300+500+200')
    f='北京'
    t='上海'
    dat='2019-09-20'
    L1 = Label(top, text="出发站: ").grid(row=1,column=0)
    L2 = Label(top, text="到达站: ").grid(row=2,column=0)
    L3 = Label(top, text="日期: ").grid(row=3,column=0)
    E1 = Entry(top, bd =5,textvariable=f).grid(row=1,column=1)
    E2 = Entry(top, bd =5,textvariable=t).grid(row=2,column=1)
    E3 = Entry(top, bd =5,textvariable=dat).grid(row=3,column=1)
    B = Button(top, text ="查询", command =cli(f,t,dat)).grid(row=4,column=0)#, command = )
    top.mainloop()


def cli(fr, t,dat):
    #get dict
    urls='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9109'
    r=requests.get(urls,verify=False)
    r.encoding = 'UTF-8'
    pattern=u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    stations=re.findall(pattern,r.text)
    #pprint(dict(stations), indent=4)
    stations=dict(stations)

    #arguments=docopt(__doc__)
    #from_station=stations.get(arguments.get('<from>'),None)
    # to_station=stations.get(arguments.get('<to>'),None)
    #date=arguments.get('<date>')
    from_station=stations.get(fr,None)
    to_station=stations.get(t,None)
    date=dat
    url=('https://kyfw.12306.cn/otn/leftTicket/queryA?'
         'leftTicketDTO.train_date={}&'
         'leftTicketDTO.from_station={}&'
         'leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date,from_station,to_station)
    print(url)
    w = requests.get(url, verify=False)
    available_trains = w.json()['data']['result']
    available_place=w.json()['data']['map']
    #options = ''.join([
    #    key for key, value in arguments.items() if value is True
    #])

    Traincollection(available_trains,available_place).pretty_table()

if __name__=='__main__':
    GUI()