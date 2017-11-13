#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2017

@author: Rafael Marinho
'''

'''
# BIBLIOTECAS UTILIZADAS NO PROJETO (TODAS APENAS NO MODEL):
#
# URLLIB:      Requisições de acesso à Internet, permite acessar as fontes dos dados;
# JSON:        Os dados das cotações estão numa API organizada em notação JSON, e essa biblioteca 
#              permite que os dados sejam resgatados em formato de dicionário;
# DATETIME:    Realiza a conversão de timestamps em formato UNIX para o formato gregoriano;
# TIME:        Busca o horário do sistema, permitindo a obtenção de timestamps;
# UNIDECODE:   Reformula strings, transformando caracteres especiais em caracteres ASCII, o que 
#              facilita nas buscas por dados pertinentes.
'''

import urllib.request as urllib;
import json;
import datetime
import time
import unidecode



'''
@class Subject: Trata-se da Interface do Model.
''' 

class Subject:
    
    
    
    '''
    @class Model():  Classe que extende a Interface "Subject", contendo as classes herdeiras 
                     referentes às moedas e da IBOVESPA. Também conta com os endereços-fonte HTTP 
                     dos dados como variáveis globais protegidas.
    '''
    
    class Model():
        
        global c_Adr
        global IBOV_Adr
        
        c_Adr = 'https://openexchangerates.org/api/latest.json?app_id=6fa1d62264a04c2dafad182cb62a4903'
        IBOV_Adr = 'http://g1.globo.com/economia/mercados/cotacoes/bmf-bovespa/'
    
    
    
        '''
        @class Moeda(): classe referente às cotações.
        '''
    
        class Moeda():
            
            '''
            @var DATA:         Vetor contendo dados ordenados e organizados das cotações, tal qual o 
                               dicionário da API onde os dados foram uma vez obtidos;
            @var names:        Vetor contendo os nomes de todas as moedas, devidamente ordenado em 
                               função de ordem alfabética dos símbolos das moedas;
            @var countries:    Vetor contendo os nomes dos países, tal como na variável "names";
            @var cotacao:      Variável análoga à variável "DATA", sendo uma versão mais primitiva da 
                               mesma, uma vez que recebe os dados da fonte e passa por um tratamento 
                               para que os dados sejam, então, alocados na variável "DATA";
            @var cot_timestamp:Variável do tipo int que guarda o timestamp UNIX da obtenção dos dados,
                               passando por um tratamento de conversão para o formato gregoriano.
            '''
            
            global DATA
            global names
            global countries
            global cotacao;         cotacao = None
            global cot_timestamp;   cot_timestamp = "000000000"
            
            DATA = []
    
            names = ['Dirham dos Emirados Árabes Unidos', 'Afegani afegão', 'Lek albanês', 
                    'Dram armênio', 'Florim holandês', 'Kwanza angolano', 'Peso argentino', 
                    'Dólar australiano', 'Florin arubano', 'Mahat azerbaijane', 
                    'Marco da Bósnia e Herzegovina', 'Dólar barbadiano', 'Taka bengalês', 
                    'Lev búlgaro', 'Dinar baremita', 'Franco burundês', 'Dólar bermudense', 
                    'Dólar bruneano', 'Peso boliviano', 'Real brasileiro', 'Dólar bahamense', 
                    'Bitcoin', 'Ngultrum butanês', 'Pula botswano', 'Rublo bielorrusso', 
                    'Dólar belizenho', 'Dólar canadense', 'Franco congolês', 'Franco suíço', 
                    'Unidade de Fomento do Chile', 'Peso chileno', 'Yuan Reinminbi de Hong Kong',
                    'Yuan Reinminbi chinês', 'Peso colombiano', 'Colón da Costa Rica', 
                    'Peso conversível cubano', 'Peso cubano', 'Escudo do Cabo Verde', 
                    'Coroa da República Tcheca', 'Franco djiboutiano', 'Coroa dinamarquesa', 
                    'Peso dominicano', 'Dinar argelino', 'Libra egípcia', 'Nafka da Eritreia',
                    'Birr etíope', 'Euro', 'Dólar de Fiji', 'Libra das Malvinas', 
                    'Libra Esterlina', 'Lari da Geórgia', 'Libra de Guernsey', 'Cedi de Gana', 
                    'Libra do Gibraltar', 'Dalasi da Gâmbia', 'Franco guianense', 
                    'Quetzal da Guatemala', 'Dólar guianesne', 'Dólar de Hong Kong', 
                    'Lempira de Honduras', 'Coroa da Croácia', 'Gourde de Haiti', 
                    'Florim húngaro', 'Rúpia indonésia', 'Novo shekel israelense', 
                    'Libra da Ilha de Man', 'Rúpia indiana', 'Dinar iraquiano', 'Rial iraniano', 
                    'Coroa da Islândia', 'Libra de Jersey', 'Dólar jamaicano', 
                    'Dinar Jordaniano', 'Iene japonês', 'Xelim queniano', 'Som quirguiz', 
                    'Riel cambojano', 'Franco comorense', 'Won norte-coreano', 'Won sul-coreano',
                    'Dinar kwaitiano', 'Dólar das Caymans', 'Tenge do Cazaquistão', 
                    'Quipe do Laos', 'Libra libanesa', 'Rúpia do Sri Lanka', 'Dólar liberiano', 
                    'Loti de Lesoto', 'Dinar da Líbia', 'Dirham marroquino', 'Leu moldávio', 
                    'Ariary de Madagascar', 'Dinar macedônio', 'Quiat do Myanmar', 
                    'Tugrik da Mongólia', 'Pataca de Macau', 'Ougukya da Mauritânia', 
                    'Rúpia da Maurícia', 'Rúpia maldívia', 'Kwacha malawiana', 'Peso mexicano', 
                    'Ringgit da Malásia', 'Nova metical do Moçambique', 'Dólar namibiano', 
                    'Naira nigeriana', 'Córdoba da Nicarágua', 'Coroa da Noruega', 
                    'Rúpia nepalesa', 'Dólar neozelandês', 'Rial do Omã', 'Balboa panamaense', 
                    'Novo sol peruano', 'Kina da Papua-Nova Guiné', 'Peso filipino', 
                    'Rúpia paquistanesa', 'Zloty polonês', 'Guarani paraguaio', 'Rial do Qatar',
                    'Leu romeno', 'Dinar sérvio', 'Rublo russo', 'Franco ruandês', 
                    'Rial da Arábia Saudita', 'Dólar das Ilhas Salomão', 'Rúpia de Seychelles', 
                    'Dinar sudanês', 'Coroa da Suécia', 'Dólar de Singapura', 
                    'Libra de Santa Helena', 'Leone de Serra Leoa', 'Xelim somaliano', 
                    'Dólar do Suriname', 'Libra sul-sudanesa', 'Dobra de São Tomé', 
                    'Cólon de El Salvador', 'Libra síria', 'Lilangeni suazi', 'Baht tailandês', 
                    'Somoni do Tadjiquistão', 'Manat novo do Turcomenistão', 'Dinar tunez', 
                    "Pa'anga de Tonga", 'Lira turca', 'Dólar de Trinidad e Tobago', 
                    'Dólar de Taiwan', 'Chelin da Tanzânia', 'Hryvnia ucraniana', 
                    'Xelim de Uganda', 'Dólar estadunidense', 'Peso uruguaio', 'Som uzbeque', 
                    'Bolívar venezuelano', 'Dong vietname', 'Vatu vanuatu', 'Tala de Samoa', 
                    'Franco CFA (BEAC)', 'Onça da prata', 'Onça do ouro', 
                    'Dólar do Caribe Oriental', 'Direitos de saque especiais do FMI', 
                    'Franco CFA (BCEAO)', 'Onça do paládio', 'Franco da Polinésia Francesa', 
                    'Onça da platina', 'Rial iemenita', 'Rand sul-africano', 'Kwacha zambiano', 
                    'Dólar do Zimbabuê']
            
            countries = ['Emirados Árabes Unidos', 'Afeganistão', 'Albânia', 'Armênia', 
                        'Holanda', 'Angola', 'Argentina', 'Austrália', 'Aruba', 'Azerbaijão', 
                        'Bósnia e Herzegovina', 'Barbados', 'Bengala', 'Bulgária', 'Barém', 
                        'Burundi', 'Bermudas', 'Brunei', 'Bolívia', 'Brasil', 'Bahamas', 
                        'Bitcoin', 'Butão', 'Botswana', 'Bielorrússia', 'Belize', 'Canadá', 
                        'Congo', 'Suíça', 'Chile', 'Chile', 'Hong Kong', 'China', 'Colombia', 
                        'Costa Rica', 'Cuba', 'Cuba', 'Cabo Verde', 'República Tcheca', 
                        'Djibouti', 'Dinamarca', 'República Dominicana', 'Argélia', 'Egito', 
                        'Eritreia', 'Etiópia', 'Europa', 'Fiji', 'Malvinas', 'Reino Unido', 
                        'Geórgia', 'Guernsey', 'Gana', 'Gibraltar', 'Gâmbia', 'Guiana Francesa',
                        'Guatemala', 'Guiana', 'Hong Kong', 'Honduras', 'Croácia', 'Haiti', 
                        'Hungria', 'Indonésia', 'Israel', 'Ilha de Man', 'Índia', 'Iraque', 'Irã', 
                        'Islândia', 'Jersey', 'Jamaica', 'Jordânia', 'Japão', 'Quênia', 
                        'Quirguistão', 'Camboja', 'Camarões', 'Coréia do Norte', 'Coréia do Sul',
                        'Kuwait', 'Ilhas Cayman', 'Cazaquistão', 'Laos', 'Líbano', 'Sri Lanka', 
                        'Libéria', 'Lesoto', 'Líbia', 'Marrocos', 'Moldávia', 'Madagascar', 
                        'Macedônia', 'Myanmar', 'Mongólia', 'Macau', 'Mauritânia', 'Maurícia', 
                        'Maldivas', 'Malawi', 'Mexico', 'Malásia', 'Moçambique', 'Namíbia', 
                        'Nigéria', 'Nicarágua', 'Noruega', 'Nepal', 'Nova Zelândia', 'Omã', 
                        'Panamá', 'Peru', 'Papua-Nova Guiné', 'Filipinas', 'Paquistão', 
                        'Polônia', 'Paraguai', 'Qatar', 'Romênia', 'Sérvia', 'Rússia', 
                        'Ruanda', 'Arábia Saudita', 'Ilhas Salomão', 'Seychelles', 'Sudão', 
                        'Suécia', 'Singapura', 'Santa Helena', 'Serra Leoa', 'Somália', 
                        'Suriname', 'Sudão do Sul', 'São Tomé e Principe', 'El Salvador', 
                        'Síria', 'Suazilândia', 'Tailândia', 'Tadjiquistão', 'Turcomenistão', 
                        'Tunísia', 'Tonga', 'Turquia', 'Trinidad e Tobago', 'Taiwan', 'Tanzânia',
                        'Ucrânia', 'Uganda', 'Estados Unidos da América', 'Uruguai', 
                        'Uzbequistão', 'Venezuela', 'Vietnã', 'Vanuatu', 'Samoa', 
                        'África Ocidental', 'Prata', 'Ouro', 'Caribe Oriental', 
                        'Fundo Monetário Internacional', 'África Ocidental', 'Paládio', 
                        'Polinésia Francesa', 'Platina', 'Iemen', 'África do Sul', 'Zamíbia', 
                        'Zimbabuê']
    
    
            
            '''
            @func getValue(): Função para obtenção de dados das cotações, com tratamento de excessões 
                              que permite que os dados não sejam sobrescritos com valores nulos em caso
                              de uma falha em que os dados seriam uma vez válidos.
            @return:          Vetor "DATA".
            '''
            
            def getValue(self):
                global DATA
                global cot_timestamp
                global cotacao
    
                try:
                    url = urllib.urlopen(c_Adr)
                    data = json.load(url)
                
                    cotacao = str(data['rates']).split(', ')
                    cot_timestamp = str(data['timestamp'])
                except ((urllib.URLError) or (ConnectionAbortedError)):
                    print ("Incapaz de acessar <https://openexchangerates.org/>; dados inacessíveis.")
                    if (cotacao == False):
                        cotacao = None
                        cot_timestamp = "0000000000"
    
                DATA = []
                COT = []
                
                
    
                try:
                    cot_timestamp = datetime.datetime.fromtimestamp(
                        int(cot_timestamp)
                        ).strftime('%d/%m/%Y, %H:%M:%S')
                except (OSError):
                    cot_timestamp = "31/12/1969, 23:59:59"
                except (ValueError):
                    pass
    
                try:
                    for x in cotacao:
                        Cotacao = x.replace('{', '')
                        Cotacao = Cotacao.replace('}', '')
                        Cotacao = Cotacao.replace("':", ':')
                        Cotacao = str(Cotacao.split("'"))
                        Cotacao = Cotacao.replace("['', '", '')
                        Cotacao = Cotacao.replace ("']", '')
                        DATA.append(Cotacao)
                except ((TypeError) or (OSError)):
                    None
    
    
                for x in DATA:
                    x = x.split(': ')
                    x[1] = float(x[1])
                
                    COT.append(x)
                DATA = []
    
                a = 0
                for x in COT:
                    y = []
                    y.append(x[0])
                    y.append(names[a])
                    y.append(countries[a])
                    y.append(COT[19][1] / x[1])
                    DATA.append(y)
                    a += 1
    
                return (DATA)
    
    
    
            '''
            @fun getQuotes(a): RECEBE COMO PARÂMETRO "a" UMA STRING PARA REFERENTE À MOEDA CUJA COTAÇÃO 
                               SERÁ BUSCADA -- Busca no vetor "DATA" as moedas cujo nome, símbolo ou 
                               país corresponder com o parâmetro do tipo str "a".
            '''
    
            def getQuotes(self, a):            
                exists = False
                
                print ("(Valores obtidos em %s) \n" %(cot_timestamp))
                
                if (a == 'ALL'):
                    a = ''
                else:
                    a = unidecode.unidecode(a)
    
                for x in DATA:
                    if ((a in unidecode.unidecode(x[0]).upper()) or 
                        (a in unidecode.unidecode(x[1]).upper()) or 
                        (a in unidecode.unidecode(x[2]).upper())):
                        print ('%s    -    %s (%s)\n\t    R$ %.4f \n' 
                               %(x[0], x[1], x[2], x[3]))
                        exists = True
                if (exists == False):
                    print ("Nenhuma moeda encontrada.")
    
    
    
            '''
            @func convert(a, b, x): RECEBE COMO PARÂMETRO AS STRINGS "a" E "b", E O NÚMERO FLOAT "x", 
                                    REFERENTES ÀS MOEDAS DE ENTRADA, DE SAÍDA, E DO VALOR DA CONVERSÃO
                                    Busca no vetor "DATA" as moedas cujo o símbolo corresponder às 
                                    variáveis "a" (moeda de entrada) e "b" (moeda de saída) e converte 
                                    quanto da moeda "b" é necessário para equivaler ao valor "x" da 
                                    moeda "a".
            @return:                String com a conversão já realizada.
            '''
            
            def convert(self, a, b, x):
                global DATA
                entry = ''
                out = ''
    
                for i in DATA:
                    if (a == i[0]):
                        entry = i[3]
                        break
                    
                for i in DATA:
                    if (b == i[0]):
                        out = i[3]
                        break
    
                if ((entry == '') or (out == '')):
                    print ("Parâmetros inválidos ou dados inacessíveis.", 
                    "\nConsulte os símbolos das moedas através da instrução [1]")
                    return ('')
    
                resp = ((entry / out) * x)
    
                return ("\n%s$ %.4f = %s$ %.4f \n" %(a, x, b, resp))
            
            
            
            '''
            @func getTimestamp(): Busca a variável global "cot_timestamp", e sua importância está em 
                                  torná-la uma variável pública.
            @return:              String "cot_timestamp".
            '''
            
            def getTimestamp(self):
                global cot_timestamp
                
                return (cot_timestamp)
            
                    
    
        '''
        @class IBOVESPA(): Classe referente aos dados da IBOVESPA.
        '''
    
        class IBOVESPA():
            
            '''
            @var value:    Variável do tipo "str" referente ao valor da IBOVESPA;
            @var vector:   Variável do tipo "str" referente ao sentido do vetor de variação dos, 
                           isto é, se a soma das variações são positivas ou negativas.
            @var var:      Variável do tipo "str" referente à porcentagem da variação dos valores da 
                           IBOVESPA.
            @var close:    Variável do tipo "str" referente ao valor de fechamento da IBOVESPA;
            @var changes:  Variável do tipo "str" referente à variação dos valores da IBOVESPA;
            @var resp:     Variável do tipo "str" referente aos dados brutos obtidos pela fonte dos 
                           dados.
            '''
            
            global value
            global vector
            global var
            global close
            global changes
            global resp;    resp = None
            
    
    
            '''
            @func getValues(): Função para obtenção de dados da IBOVESPA, com tratamento de excessões 
                               que permite que os dados não sejam sobrescritos com valores nulos em caso
                               de uma falha em que os dados seriam uma vez válidos.
            @return:           Vetor "returnable".
            '''
            
            def getValues(self):
                global value
                global vector
                global var
                global close
                global changes
                global IBOV_timestamp
                global resp
    
                
                try:
                    resp = urllib.urlopen(IBOV_Adr).read().decode('utf-8')
                    IBOV_timestamp = time.time()
                
                except (urllib.URLError):
                    print ("Incapaz de acessar <http://g1.globo.com/>; dados inacessíveis.")
                    if (resp == None):
                        resp = None
                        IBOV_timestamp = "0000000000"
                    
                try:
                    IBOV_timestamp = datetime.datetime.fromtimestamp(
                        int(IBOV_timestamp)
                        ).strftime('%d/%m/%Y, %H:%M:%S')
                except (OSError):
                    IBOV_timestamp = "31/12/1969, 23:59:59"
                except (ValueError):
                    pass
                
                if (resp != None):
                    value = (resp[resp.index('span class="label">') + 19:
                                 resp.index('span class="label">') + 25])
                    
                    vector = (resp[resp.index('span class="signal">') + 20:
                                  resp.index('span class="signal">') + 21])
                    
                    var = (vector + "     " + resp[resp.index('span class="signal">') + 28:
                                                  resp.index('span class="signal">') + 32] + "%")
                                                  
                    close = (resp[resp.index('span class="value">') + 19:
                                 resp.index('span class="value">') + 25])
    
                    if (float(value) >= float(close)):
                        changes = (vector + " R$  " + str(round(float(value) - float(close), 3)))
                    elif (float(value) < float(close)):
                        changes = (float(close) - float(close))
                        changes = (vector + " R$  " + str(round(changes, 3)))
                
                else:
                    value = 0
                    close = 0
                    changes = 0
                    var = 0
                    
                returnable = [value, close, changes, var]
                return (returnable)
    
    
            
            '''
            @fun getIBOV():  Função para formação de uma string que contém os dados da IBOVESPA.
            @return:         Retorna o valor da IBOVESPA e todos seus outros dados pertinentes.
            '''
            
            def getIBOV(self):
                global valeu
                global close
                global changes
                global var
                
                try:            
                    IBOV = ('''(Valores obtidos em %s)
                    
IBOV   -    IBOVESPA (Brasil)
            Valor:                  R$ %s
            Último fechamento:      R$ %s
            Variação              %s
            Taxa de variação:     %s
            ''' % (IBOV_timestamp, value, close, changes, var))
                
                except(NameError):
                    IBOV = "Dados indisponíveis."
                
                return (IBOV)
            
            
            
            '''
            @func getTimestamp(): Busca a variável global "IBOV_timestamp", e sua importância está em 
                                  torná-la uma variável pública.
            @return:              String "IBOV_timestamp".
            '''
            
            def getTimestamp(self):
                global IBOV_timestamp
                
                return (IBOV_timestamp)
