#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''


import MVC



'''
@class ControllerSearch: Trata-se da Interface do Controller.
'''

class ControllerSearch:
    
    
    
    '''
    @class Sources(): Classe que extende a Interface "ControllerSearch" e é responsável por acessar as fontes dos 
                      dados referentes tanto às cotações das moedas quanto da IBOVESPA, permitindo que sejam 
                      acessados pelo Model.
    '''
    
    class Sources():
        
        
        
        '''
        @func ControllerSources(): Função que permite acessar as fontes dos dados das cotações de moedas e da 
                                   IBOVESPA. Trabalha em função da função "getValue()" e "getValues()" do Model, 
                                   podendo acessar as duas em uma única chamada dessa função, estando de acordo com
                                   o parâmetro "x".
        '''
        
        def ControllerSources(self, x):
            if ((x == '1') or (x == '3')):
                MVC.Model.Subject.Model.Moeda.getValue(None)
            if ((x == '2') or (x == '3')):
                MVC.Model.Subject.Model.IBOVESPA.getValues(None)



    '''
    @class Options(): Classe que extende a Interface "ControllerSearch" e é responsável pelo controle das 
                      principais opções que o usuário acessa (a partir do menu principal da inteface do mesmo).
    '''
    
    class Options():
        
        
        
        '''
        @func ControllerOptions(): Função que controla as princpais opções do usuário para com o programa, então 
                                   referente ao menu principal, através do parâmetro "x", responsável pela escolha
                                   de alguma das várias opções de retorno.
        @return                    Parâmetro "x" como '1': função "seekMoeda()" da classe View (Observer) - sem 
                                                           parâmetros;
                                   Parâmetro "x" como '2': função "seekIBOV()" da classe View (Observer) - sem 
                                                           parâmetros;
                                   Parâmetro "x" como '3': função "convertMoedas()" da classe View (Observer) - 
                                                           sem parâmetros;
                                   Parâmetro "x" como '4': função "update()" da classe View (Observer) - sem 
                                                           parâmetros;
                                   Parâmetro "x" como '5': exibe uma string que notifica o fim do tempo de 
                                                           execução do programa, prontamente fazendo o mesmo;
                                   Parâmetro "x" com outros valores: notifica o parâmetro como contendo um valor
                                                                     inválido.
        '''
        
        def ControllerOptions(self, x):
            if (x == '1'):
                return (MVC.View.Observer.View.seekMoeda(None))
                    
            elif (x == '2'):
                return (MVC.View.Observer.View.seekIBOV(None))
                    
            elif (x == '3'):
                return (MVC.View.Observer.View.convertMoedas(None))
                    
            elif (x == '4'):
                return (MVC.View.Observer.View.update(None))
                    
            elif (x == '5'):
                return (print ("Programa encerrado."))
                
            else:
                return (print ("Instrução inválida."))
