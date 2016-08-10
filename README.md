# desafio-gupy
Projeto feito com o objetivo de resolver o desafio proposto pelo pessoal da Gupy, que era desenvolver um encurtador de URLs com um backend em Python. O encurtador também deveria contar com um contador de quantas vezes o link foi clicado.

# Como usar

Primeiro, o framework Tornado deve ser instalado. Para isso, digite "pip install tornado" (sem as aspas) no terminal. Após isso, basta usar "python controller.py" e o serviço já estará no ar! É só abrir o navegador e ir até "localhost:8080".

# Tecnologias usadas

No front-end foi usado o framework Bootstrap, do Twitter. Tudo muito básico, inspirado no exemplo do Jumbotron, dado por eles mesmos.
No back-end, foi usado o Tornado. A intenção inicial era usar o Flask, mas houveram problemas no uso dele, e por falta de tempo, achei melhor usar um outro framework que funcionasse "de primeira". Testei o Tornado e ele funcionou.
Como banco de dados, usei o SQLite, pois este já vem instalado por padrão junto com o interpretador do Python. Novamente, a intenção inicial era usa ro MySQL, mas havia uma diversidade imensa de caminhos a seguir, o que complica um pouco para uma pessoa inciante no Python como eu.

# Bugs conhecidos

Às vezes, não existe nenhum arquivo que contenha o banco de dados do SQLite, mas ainda sim, o software exibe as informações, como se eles as retirasse de um "banco de dados fanstasma" ou um banco de dados na memória RAM, eu não sei. É preciso investigar com mais calma.
Outro problema conhecido é com o contador de quantas vezes o link foi clicado. Ele funciona quando o link nunca foi clicado (Portanto marca zero) e passa a ser clicado (E o contador vai a um), mas dai em diante ele não funciona. Novamente, é preciso uma investigação um pouco mais apurada.

# Conclusão

Foi um desafio muito legal de se fazer, principalmente porque eu não conhecia Python, sua sintaxe ou ecossistema. Tudo foi aprendido na prática, com base na sua necessidade. Portanto, ainda há muito para evoluir neste código.
