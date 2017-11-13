#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''

from MVC import Controller, Model



'''
@class Observer: Trata-se da Interface da View.
'''

class Observer:
    
    
    
    '''
    @class View(): Classe que extende a Interface "Observer" e contem, de fato, as intefaces do usuário e lida 
                   com todas as interações com o mesmo.
    '''
    
    class View():
    
        
    
        '''
        @func seekMoeda(): Pede para que o usuário insira uma string (a) e retorna a função que pesquisa a 
                           cotação de uma ou mais moedas condissentes com tal string.
        @return:           Função "getQuotes()" da classe "Moeda" (Model) com parâmetro "a".
        '''
    
        def seekMoeda(self):
            a = ''
    
    
            while (a == ''):
                a = str(input("Símbolo; país ou nome da moeda a ser pesquisada: ")).upper()
    
                return (Model.Subject.Model.Moeda.getQuotes(None, a))
    
        
    
        '''
        @func seekIBOV(): Acessa a função "getIBOV()", o que chama uma longa string com os dados da IBOVESPA.
        @return:          Exibe o retorno da função "getIBOV()" da classe "IBOVESPA" (Model) - sem parâmetros.
        '''
        
        def seekIBOV(self):
            return (print (Model.Subject.Model.IBOVESPA.getIBOV(None)))
            
    
    
        '''
        @func convertMoedas(): Pede para que o usuário insira duas strings de tamanho 3 (x, y) e um número do 
                               tipo "float" (m) para que seja a realizada a conversão de um valor entre duas 
                               moedas.
        @return:               Função "convert()" da classe "Moeda" (Model) com parâmetros "x", "y", e "m".
        '''
        
        def convertMoedas(self):
            x = ''
            y = ''
            m = 1
    
            while (len(x) != 3):
                x = str(input("Digite o simbolo da moeda de entrada: ")).upper()
    
                if (len(x) != 3):
                    print ("Por favor, insira um simbolo válido.\n")
                    
            while (len(y) != 3):
                y = str(input("Digite o simbolo da moeda de saída: ")).upper()
    
                if (len(y) != 3):
                    print ("Por favor, insira um simbolo válido.\n")
            
            
            try:
                m = float(input("Digite a quantidade de %s$ você quer converter: " %(x)))
            except (ValueError):
                m = 1
    
            print (Model.Subject.Model.Moeda.convert(None, x, y, m))
    

    
        '''
        @func update(): Interface do usuário que dispõe a escolha de atualizar os dados tanto da cotação das 
                        moedas quanto da IBOVESPA (inclusive ambas), explicitando os limites de cada um.
        @return:        Função "ControllerSources" da classe "Sources" (Controller) - sem parâmetros.
        '''
        
        def update(self):
            x = ''
            
            while (x not in ['1', '2', '3', '0']):
                print ('''
                 Λ         Λ
                /!\ AVISO /!\ 
               -----     -----  
* AS MOEDAS SÃO PRÉ-CARREGADAS NA INICIALIZAÇÃO 
  DO PROGRAMA;
* A API UTILIZADA PARA OBTENÇÃO DAS COTAÇÕES DE 
  MOEDAS É UM SERVIÇO PAGO E TEM LIMITE DE ATÉ 
  1000 USOS MENSAIS, E A ATUALIZAÇÃO DE SEUS 
  DADOS É A CADA UMA HORA;
* OS DADOS DA IBOVESPA SÃO LIVRES E ILIMITADOS.

--> Os dados atuais das cotações são de 
    %s;
--> Os dados atuais da IBOVESPA são de 
    %s. 
            
            [1] Atualizar cotações;
            [2] Atualizar IBOVESPA;
            [3] Atualizar ambos;
            [0] Apenas voltar ao menu inicial.
            ''' %(Model.Subject.Model.Moeda.getTimestamp(None), 
                  Model.Subject.Model.IBOVESPA.getTimestamp(None)))
                x = str(input(""))
                
                if (x == '0'):
                    break
                
                return (Controller.ControllerSearch.Sources.ControllerSources(None, x))
            
            
            
        '''
        @func menu(): Principal interface do usuário, permitindo-o acessar cada opção que o programa dispõe ao 
                      inserir um número do tipo "str" (parâmetro "a") correspondente à cada opção.
        @return:      Função "ControllerOptions()" da classe "Options" (ControllerSearch) com parâmetro "a".
        '''
        
        def menu(self):
            a = ''
            while (a != '5'):
                a = ''
                a = str(input('''INSTRUÇÕES:
                [1] Consultar cotação de moedas;
                [2] Consultar valor da IBOVESPA;
                [3] Converter moedas;
                [4] Atualizar dados;
                [5] Encerrar programa. \n\n'''))
    
                Controller.ControllerSearch.Options.ControllerOptions(None, a)
