# ES3_Cotações

Projeto feito em Python 3.6.2 (incompatível com Python2), com arquitetura MVC (Model-View-Controller), 
para buscar valores das cotações de diversas moedas, minérios e da IBOVESPA.
O projeto utiliza o framework PyDev, que pode ser utilizado na IDE Eclipse. De fato, a versão do Eclipse
utilizada no projeto foi Oxygen.


                                         ..:: MANUAL ::..                                         
                                                                                                  
    Em primeiro lugar, é válido lembrar que o código se encontra todo comentado.                  
                                                                                                  
    Em primeiro lugar, é importante lembrar que o programa é inicializado através do módulo Main.py; e, uma vez 
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

Desenvolvido por Rafael Marinho, estudante de Engenharia de Software III no curso de 
Tecnologia em Análise e Desenvolvimento de Sistemas, sob a tutela de 
Me. Giuliano Araújo Bertoti.

# FATEC SJC - Prof. Jessen Vidal.
# São José dos Campos, SP - Brazil.
