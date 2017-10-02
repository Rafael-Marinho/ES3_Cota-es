#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''

from time import gmtime, strftime

from MVC.Controller import Controller



class Moeda():
    global cotacao
    global moeda
    data_COT = Controller.ControllerSearchMoeda(None)
    x = 0
    cotacao = []

    while(x < 153):
        moeda = []
        
        if (data_COT != None):
            moeda.append(str(data_COT["data"]["currency"][x]["name"]));
            moeda.append(str(data_COT["data"]["currency"][x]["code"]));
            moeda.append(float(data_COT["data"]["currency"][x]["buying"]));
            moeda.append(float(data_COT["data"]["currency"][x]["selling"]));
        
            cotacao.append(moeda)
        else:
            cotacao = [['', '', 0, 0]]
        x += 1

    def getMoeda(self):  
        a = str(input("\nDigite o nome ou o símbolo da moeda a ser buscada: "))
        a = a.upper()

        Break = False
        for x in cotacao:
            if (Break == True):
                break
            for y in x:
                y = str(y)
                if (a == y.upper()):
                    moeda = ('''\n%s - %s
        Compra:               R$  %.4f
        Venda:                R$  %.4f
''' % (x[1], x[0], x[2], x[3]))
                    Break = True
                    break
                else:
                    moeda = "Não encontrado."

        return (print (moeda))



class IBOVESPA():
    global value
    global vector
    global var
    global close
    global changes
    
    resp = Controller.ControllerSearchIBOVESPA(None)
    
    if (resp != None):
        value = resp[resp.index('span class="label">') + 19:resp.index('span class="label">') + 25]
        vector = resp[resp.index('span class="signal">') + 20:resp.index('span class="signal">') + 21]
        var = vector + "     " + resp[resp.index('span class="signal">') + 28:resp.index('span class="signal">') + 32] + "%"
        close = resp[resp.index('span class="value">') + 19:resp.index('span class="value">') + 25]

        if (float(value) >= float(close)):
            changes = vector + " R$  " + str(round(float(value) - float(close), 3))
        elif (float(value) < float(close)):
            changes = (float(close) - float(close))
            changes = vector + " R$  " + str(round(changes, 3))
    
    else:
        value, close, changes, var = 0, 0, 0, 0

    def getIBOV(self):

        IBOV = ('''IBOV - IBOVESPA
        Valor:                  R$ %s
        Último fechamento:      R$ %s
        Variação              %s
        Taxa de variação:     %s
''' % (value, close, changes, var))
        
        return (print (IBOV))



class Bitcoin():
    global btcn

    data_BTC = Controller.ControllerSearchBitcoin(None)

    btcn = []

    if (data_BTC != None):
        btcn.append(float(data_BTC["ticker"]["buy"]));
        btcn.append(float(data_BTC["ticker"]["sell"]));
    else:
        btcn.append(0)
        btcn.append(0)

    btcn = ('''BTC - Bitcoin
        Compra:               R$  %.d
        Venda:                R$  %.d
''' % (btcn[0], btcn[1]))

    def getBTC(self):
        return (print (btcn))



def getTime():
    seconds = (strftime("%S", gmtime()))
    minutes = (strftime("%M", gmtime()))
    hour = str(int(strftime("%H", gmtime())) - 3)

    if (int(hour) < 0):
        hour = (int(hour) + 21)

    time = ("%s:%s:%s" % (hour, minutes, seconds))

    return ("\nValores obtidos em: " + time + '\n')
