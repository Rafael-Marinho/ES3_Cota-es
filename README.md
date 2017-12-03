# ES3_Cotações

Projeto feito em Python 3.6.2 (incompatível com Python2), com arquitetura MVC (Model-View-Controller), 
para buscar valores das cotações de diversas moedas, minérios e da IBOVESPA.
O projeto utiliza o framework PyDev, que pode ser utilizado na IDE Eclipse. De fato, a versão do Eclipse
utilizada no projeto foi Oxygen.

# ÍNDICE:
#
# [1] Manual;
# [2] Imagens;
# [3] Sobre.


                                         ..:: MANUAL ::..                                         
                                                                                                  
    Em primeiro lugar, é válido lembrar que o código se encontra todo comentado.                  
                                                                                                  
    Também é importante lembrar que o programa é inicializado através do módulo Main.py; e, uma vez 
    inicializado, o usuário pode realizar três operações distintas, mais duas relacionadas à manutenção dos dados 
    e finalização do tempo de execução do programa:                                                                                                                   
    [1] Buscar valores das cotações de moedas;                                                    
    [2] Buscar valores da IBOVESPA;                                                               
    [3] Conversão de moedas;                                                                      
    [4] Atualizar dados;                                                                          
    [5] Encerrar programa.                                                                        
                                                                                                  
    [1] A função de buscar cotações recebe a entrada de uma string. A partir dessa busca, é retornado as informações 
    de todas as moedas com algum dado correspondente à essa string. Os dados envolvem: o símbolo da moeda; o o nome 
    da moeda por extenso e o nome do país, também por extenso.   
    Além de moedas, há também valores de onça de alguns minérios, moedas virtuais (como o Bitcoin) e outros valores 
    disponíveis.
    Todos os valores retornados são a conversão do valor da respectiva moeda já convertida para o real (BRL). 
    DICA: inserir a string "ALL" retorna todos os dados de cotações disponíveis.                  
                                                                                                  
    [2] A função de buscar valores da IBOVESPA não recebe parâmetros. Uma vez chamada, são retornados valores 
    completos sobre o indicador. Se houver dados, eles serão retornados.
                                                                                                  
    [3] A conversão de moedas exige três parâmetros: uma moeda de entrada; uma moeda de saída e o valor da conversão. 
    Os parâmetros inseridos são strings de tamanho 3, o que é o tamanho dos símbolos das moedas. Não são aceitos 
    parâmetros de moeda de entrada e saída que não sejam os símbolos das moedas, e o Programa persiste exigindo até 
    que uma string de tamanho 3 seja inserida. O terceiro parâmetro é um valor float do quanto da moeda de entrada 
    deve ser convertido para a moeda de saída.
    O retorno dessa função tem o formato de "a tal quantidade da moeda de entrada equivale a uma certa quantidade 
    da moeda de saída. 
    Se o usuário não inserir nenhum valor no terceiro parâmetro, tal parâmetro será 1 por padrão. 
    
    [4] A atualização de valores permite, claro, que o usuário faça uma requisição de HTTP/HTTPS para atualizar os 
    dados tanto das cotações quanto da IBOVESPA. É requisitado ao usuário que insira um comando para atualizar os 
    dados das cotações, da IBOVESPA, de ambas ou de nenhuma, através de números (como no menu principal). 
    Os dados da IBOVESPA são livres, acessados através da URL <http://g1.globo.com/economia/mercados/cotacoes/bmf-bovespa/>. 
    Os dados das cotações, no entanto, são fornecidos por um serviço de API da Open Exchanges Rates e dependem de 
    assinatura - a assinatura gratis permite até 1000 acessos mensais. Acesse o site do provedor pela URL 
    <https://openexchangerates.org/> para assinar o serviço. 
    Se os dados estiverem disponíveis, os dados já disponíveis serão sobrescritos por esses novos dados. Se os 
    dados não estiverem disponíveis, o usuário é notificado e nada mais acontece, deixando os dados já disponíveis 
    intactos. 
    [5] A função de encerrar o programa faz exatamente o que sugere o nome: uma vez chamada, o tempo de execução do 
    programa é encerrado.


[2] Imagens:

![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/Diagrama%20MVC.png)

1ª IMAGEM - MVC.png: Primeiramente, temos acima o diagrama de classes em formato UML-Python sobre a arquitetura MVC. Não poderia ser mais simples.
Segue abaixo a legenda das imagens, em ordem didática para demosntação de execução e funcionamento do programa (Eclipse Oxygen):


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/Menu%20principal.png)

2ª IMAGEM - Menu principal.png: Essa imagem mostra a tela inicial do programa. De fato, esse menu se repete a cada interação;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/1%20USD.png)

3ª IMAGEM - 1 USD.png: A imagem demonstra a função 1, com a busca do símbolo da moeda (USD);


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/1%20D%C3%B3lar.png)

4ª IMAGEM - 1 Dólar.png: Demonstra a função 1, com a busca de um nome simples (Dólar), demonstrando também que retorna todas as moedas correspondentes, uma vez que não especificou qual dólar se tratava;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/1%20Bosnia.png)

5ª IMAGEM - 1 Bosnia.png: Ainda sobre a função 1, busca apenas parte do nome de um país e sem acentuação: "Bosnia", retornando os valores correspondentes do Marco da Bósnia e Herzegovina;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/1%20oNCA.png)

6ª IMAGEM - 1 oNCA.png: Mais um exemplo da função 1, buscando dessa vez valores de minérios (cujo o valor é mensurado pela quantidade de onças - uma grama equivale a cerca de 28,35 onças) e demonstrando que os erros de case-sensitive e simbolos ASCII estão tratados na mecânica de buscas. Retorna, é claro, os valores de todos os minérios que são medidos por essa unidade de pesagem;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/2.png)

7ª IMAGEM - 2.png: Exemplo da função 2. Como não exige parâmetros, retorna sem fazer exigências;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/3%20GBP%20BRL%20650.png)

8ª IMAGEM - 3 GBP BRL 650.png: Exemplo da função 3, convertendo 650 libras esterlinas em seu respectivo valor em reais. Essa função aceita apenas símbolos de moedas, ao invés de seus nomes e respectivos países, como na função 1;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/4%203%20FAIL.png)

9ª IMAGEM - 4 3 FAIL.png: Exemplo da função 4, responsável pela atualização dos dados. Como os dados já haviam sido acessados na inicialização do programa, considerei mais pertinente demonstrar que os dados já acessados não são sobrescritos com valores nulos em caso de falha, tanto para as cotações quanto para a IBOVESPA. Isso pode ser visto na imagem seguinte;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/P%C3%B3s%20Fail.png)

10ª IMAGEM - Pós Fail.png: Após a busca falha para atualização dos dados, os dados já então presentes não são sobrescritos. Isso é atestado ao se chamar a função 1 e 2.


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/5.png)

11ª IMAGEM - 5.png: Demonstra a função 5, responsável pelo encerramento do tempo de execução do programa. Não tem segredo, faz como sugere o nome;


![alt text](https://github.com/Rafael-Marinho/ES3_Cota-es/blob/master/Imagens/Falha%20inicial.png)

12ª IMAGEM - Falha inicial.png: Demonstra a inicialização do programa com falhas no acesso dos dados acerca das cotações e da IBOVESPA. Mostra também como a chamada das funções 1 e 2 funcionam quando não há dados acessados e a chamada da função 4, dessa vez acessando os dados com sucesso. Após isso, as funções 1 e 2 são chamadas, afim de demonstrar que os dados foram, de fato, acessados e armazenados com sucesso.


[3] Créditos:

Desenvolvido por Rafael Marinho, estudante de Engenharia de Software III no curso de 
Tecnologia em Análise e Desenvolvimento de Sistemas, sob a tutela de 
Me. Giuliano Araújo Bertoti.

# FATEC SJC - Prof. Jessen Vidal.
# São José dos Campos, SP - Brazil.
