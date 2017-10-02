#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''
import MVC.Model as Model
import MVC.Controller as Controller

class View:
    op = None

    print ('''..:: B O L S A ::..
    
Bem vindo, siga as intruções para prosseguir: \n''')

    while (op != 0):
    
        op = str(input('''[1] Para visualizar o valor da IBOVESPA;
[2] Para visualizar o valor de alguma moeda federal;
[3] Para visualizar o valor do Bitcoin;
[4] Para atualizar valores;
[0] Para sair.
    
'''))

        while (op not in ['0', '1', '2', '3', '4']):
            if (op == ''):
                op = str(input())
            else:
                print ("\nComando inválido.")
                op = str(input("Por favor, insira um comando válido: "))

        if (op == '0'):
            print ("\nPrograma encerrado.")
            break
    
        print (Model.getTime())

        if (op == '1'):
            Model.IBOVESPA.getIBOV(None)

        if (op == '2'):
            Model.Moeda.getMoeda(None)

        if (op == '3'):
            Model.Bitcoin.getBTC(None)
            
        if (op == '4'):
            Controller
            print ("Valores atualizados. \n")
