#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''

import urllib.request as urllib2
import urllib
import json

class Controller:

    def ControllerSearchIBOVESPA(self):
        try:
            url = 'http://g1.globo.com/economia/mercados/cotacoes/bmf-bovespa/'
            resp = urllib.request.urlopen(url).read().decode('utf-8');

            return (resp)
        
        except (urllib.error.URLError):
            print ("Incapaz de acessar <http://g1.globo.com/>; dados inacessíveis.")



    def ControllerSearchMoeda(self):
        try:
            url_COT = urllib2.urlopen('https://api.vitortec.com/currency/quotation/v1.2/');
            data_COT = json.load(url_COT);

            return (data_COT)
        
        except (urllib.error.URLError):
            print ("Incapaz de acessar <https://api.vitortec.com/>; dados inacessíveis.")



    def ControllerSearchBitcoin(self):
        try:
            url_BTC = urllib2.urlopen('https://www.mercadobitcoin.net/api/ticker/');
            data_BTC = json.load(url_BTC);

            return (data_BTC)
        
        except (urllib.error.URLError):
            print ("Incapaz de acessar <https://www.mercadobitcoin.net/>; dados inacessíveis. \n\n")
