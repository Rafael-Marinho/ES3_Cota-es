Segue abaixo a legenda das imagens, em ordem didática para demosntação de execução e 
funcionamento do programa:

1ª IMAGEM - MVC.png:
    Trata-se do diagrama de classes do projeto, feito em arquitetura MVC (Model-View-Controller).
    Vale lembrar que este é um projeto feito em Python, então o diagrama é organizado como o tal.

2ª IMAGEM - Menu principal.png:
    Essa imagem mostra a tela inicial do programa. De fato, esse menu se repete a cada interação;
    
3ª IMAGEM - 1 USD.png:
    A imagem demonstra a função 1, com a busca do símbolo da moeda (USD);

4ª IMAGEM - 1 Dólar.png:
    Demonstra a função 1, com a busca de um nome simples (Dólar), demonstrando também que retorna 
    todas as moedas correspondentes, uma vez que não especificou qual dólar se tratava;
    
5ª IMAGEM - 1 Bosnia.png:
    Ainda sobre a função 1, busca apenas parte do nome de um país e sem acentuação: "Bosnia",
    retornando os valores correspondentes do Marco da Bósnia e Herzegovina;

6ª IMAGEM - 1 oNCA.png:
    Mais um exemplo da função 1, buscando dessa vez valores de minérios (cujo o valor é mensurado
    pela quantidade de onças - uma grama equivale a cerca de 28,35 onças) e demonstrando que os 
    erros de case-sensitive e simbolos ASCII estão tratados na mecânica de buscas. Retorna, é 
    claro, os valores de todos os minérios que são medidos por essa unidade de pesagem;
    
7ª IMAGEM - 2.png:
    Exemplo da função 2. Como não exige parâmetros, retorna sem fazer exigências;
    
8ª IMAGEM - 3 GBP BRL 650.png:
    Exemplo da função 3, convertendo 650 libras esterlinas em seu respectivo valor em reais. Essa 
    função aceita apenas símbolos de moedas, ao invés de seus nomes e respectivos países, como na
    função 1;
    
9ª IMAGEM - 4 3 FAIL.png:
    Exemplo da função 4, responsável pela atualização dos dados. Como os dados já haviam sido 
    acessados na inicialização do programa, considerei mais pertinente demonstrar que os dados já
    acessados não são sobrescritos com valores nulos em caso de falha, tanto para as cotações 
    quanto para a IBOVESPA. Isso pode ser visto na imagem seguinte;
    
10ª IMAGEM - Pós Fail.png:
    Após a busca falha para atualização dos dados, os dados já então presentes não são 
    sobrescritos. Isso é atestado ao se chamar a função 1 e 2.
    
11ª IMAGEM - 5.png:
    Demonstra a função 5, responsável pelo encerramento do tempo de execução do programa. Não tem
    segredo, faz como sugere o nome;
    
12ª IMAGEM - Falha inicial.png:
    Demonstra a inicialização do programa com falhas no acesso dos dados acerca das cotações e da
    IBOVESPA. Mostra também como a chamada das funções 1 e 2 funcionam quando não há dados 
    acessados e a chamada da função 4, dessa vez acessando os dados com sucesso. Após isso, as 
    funções 1 e 2 são chamadas, afim de demonstrar que os dados foram, de fato, acessados e 
    armazenados com sucesso.
