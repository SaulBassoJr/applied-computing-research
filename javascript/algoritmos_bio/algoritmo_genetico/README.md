# Genetic Algorithm (Algoritmo Genético)

<h2 align="center">
Introdução
</h2>
<p align="justify">
Código desenvolvido durante o estudo de Computação Bioinspirada, mas especificamente algoritimos genéticos!
</p>
<p align="justify">
Esse código gera strings aleatórias e evolui a população até encontrar "PARALELEPIPEDO" através de seleção, mutação e recombinação. Cada geração traz indivíduos melhores, até que a solução seja alcançada.
</p>

<h2 align="center">
Computação Bioinspirada
</h2>
<p align="justify">
Computação bioinspirada é uma importante área de pesquisa da Ciência de Computação que foca na investigação 
do aprendizado de máquina e técnicas de otimização, geralmente inspiradas por princípios biológicos, 
os quais podem ser utilizados para resolver problemas complexos através do uso de sistemas inteligentes.
</p>
<p align="justify">
Algoritimos evolutivos são exelentes exemplos, eles imitam processos naturais, como seleção natural, mutação e recombinação 
genética, para resolver problemas complexos.
E dentre eles temos alguns tipos:
  <ol>
    <li>Algoritmos Genéticos (AG).</li>
    <li>Programação Evolutiva (EP).</li>
    <li>Estratégias Evolutivas (ES).</li>
    <li>Evolução Diferencial (DE).</li>
    <li>Programação Genética (GP.)</li>
  </ol>
</p>
<div align="center">
<img src=https://github.com/user-attachments/assets/c3f440d1-54af-41e3-98f4-ec05855ca606 width="600px"/>
</div>

<h2 align="center">
Algoritmos Genéticos
</h2>
<p align="justify">
São técnicas de busca que utilizam processos biológicos para resolver problemas complexos.
</p>
<h3>Como funcionam?</h3>
<p align="justify">
  <ol>
    <li>Cria-se aleatoriamente uma população inicial de indivíduos;</li>
    <li>Avalia-se o quão adaptado cada indivíduo está ao problema (Fitness function - Função de Aptidão);</li>
    <li>Selecionam-se os indivíduos mais adaptados para reproduzir;</li>
    <li>Os indivíduos mais adaptados reproduzem-se através de crossover e mutação;</li>
    <li>Repetem-se os passos 2 a 4 até atingir um critério de parada ou alcançar o objetivo.</li>
  </ol>
</p>

<h2 align="center">
O código!
</h2>
<p align="justify">
O código segue a estrutura básica de um AG, incluindo:
  <ol>
    <li>Geração de população.</li>
    <li>Avaliação da aptidão dos indivíduos.</li>
    <li>Seleção dos melhores indivíduos para reprodução.</li>
    <li>Crossover e mutação para gerar novos indivíduos.</li>
    <li>Critério de parada quando encontra a solução.</li>
  </ol>
</p>

<h3 align="center">
Fitness function - Função de Aptidão
</h3>
<p align="justify">
A função avaliarAptidao(individuo) mede o quão próximo um indivíduo está da solução desejada (a string ALVO). 
</p>
<p align="justify">
A função recebe um indivíduo (string aleatória) e o compara letra por letra com a string alvo. Ela conta quantos caracteres estão corretos e retorna esse número como a pontuação de aptidão.
 <ol>
    <li>O código percorre cada posição da string individuo.</li>
    <li>Ele verifica se o caractere nessa posição é igual ao da string ALVO.</li>
    <li>Para cada correspondência correta, soma 1 à pontuação final.</li>
    <li>Retorna a soma total, que representa a aptidão do indivíduo.</li>
 </ol>
</p>
<p align="justify">
Exemplo Prático:
  <ul>
    <li>ALVO = "PARALELEPIPEDO"</li>
    <li>individuo = "PBRALXLEPIAEDQO"</li>
 </ul>
 Agora, comparamos cada caractere posição por posição:
</p>
<div align="center">
<img src=https://github.com/user-attachments/assets/60c24fff-1999-4dc2-89aa-57ad11b90abe width="600px"/>
</div>
<p align="justify">
  O indivíduo tem 9 caracteres corretos na posição correta.
  Assim, a função avaliarAptidao(individuo) retorna 9.
</p>

<h3 align="center"> Interpretação Matemática </h3>
<p align="justify">
  A função implementa a seguinte fórmula matemática:
</p>
<div align="center">
<img src=https://github.com/user-attachments/assets/3ce4777f-aa80-42eb-9dd3-acb8168aa8c8 width="300px" />
</div>
<p align="justify">
 Onde f(i) é definida como:
</p>
<div align="center">
<img src=https://github.com/user-attachments/assets/a129db87-01b7-4791-86b1-92ffdbadfedf width="300px" />
</div>
<p align="justify">
 Suponha que a string ALVO seja: PARALELEPIPEDO
  <ul>
    <li>ALVO="PARALELEPIPEDO"</li>
  </ul>
  E um indivíduo qualquer seja: PBRALXLEPIAEDQO
  <ul>
    <li>individuo="PBRALXLEPIAEDQO"</li>
  </ul>
  Agora aplica-se a função f(i) para cada posição i da string.
</p>
<div align="center">
<img src=https://github.com/user-attachments/assets/651856c7-3f18-451a-87f1-c8fcda3fb0df width="600px" />
</div>




