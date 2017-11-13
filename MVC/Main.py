#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''

from MVC import View
from MVC import Controller



'''
# O "Main" tem a função de iniciar o programa, 
# e pra isso ele busca os valores das cotações 
# das moedas e da IBOVESPA, e prontamente 
# chama a interface principal do usuário.
'''

Controller.ControllerSearch.Sources.ControllerSources(None, '3')
View.Observer.View.menu(None)
