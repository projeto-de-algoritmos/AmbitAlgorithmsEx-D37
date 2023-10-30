# Integrantes

|                         Nome                         | Matrícula |
| :--------------------------------------------------: | :-------: |
|  [Pedro Torreão](https://github.com/PedroTorreao21)  | 190036761 |
|  [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421 |

# Introdução

Este repositório foi criado para o desenvolvimento do segundo módulo sobre Algoritmos Ambiciosos da disciplina Projeto de Algoritmos do Professor Maurício Serrano.

# Apresentação

[Link para a apresentação da dupla]()

# Foram feitos os exercícios no LeetCode

## [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)

Neste método, os intervalos são organizados em ordem crescente com base em seus tempos de término (a[1]). Em seguida, percorremos os intervalos a partir do segundo intervalo, verificando se há alguma sobreposição com o intervalo anterior. Se houver sobreposição, aumentamos o contador count. Caso contrário, atualizamos o tempo de término end para o tempo de término do intervalo atual. Após a conclusão do loop, o valor de count representa o número mínimo de intervalos a serem excluídos para evitar sobreposições. Essa abordagem faz uso do algoritmo de Agendamento de Intervalos para selecionar o conjunto máximo de intervalos sem sobreposição.

![Non-overlapping Intervals](/images/435.jpeg)

## [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/)

Esta solução utiliza o algoritmo "Agendamento para Minimizar Atrasos" com o objetivo de maximizar o número de cursos concluídos dentro dos prazos estabelecidos. O algoritmo percorre a lista de cursos, avaliando a possibilidade de concluir cada curso no prazo máximo determinado. Se não for viável, o algoritmo realiza uma substituição, trocando um curso com um prazo máximo maior pelo curso atual, desde que isso resulte em um atraso total menor.

![Course Schedule III](/images/630.jpeg)

# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do Leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.

# Uso

## Passo 1: Copiar o código

Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício

Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão.

## Passo 3: Alterar linguagem

Selecione a linguagem.

## Passo 4: Colar o código

Cole o código copiado no editor.

## Passo 5: Rodar o código

Abaixo do editor de código, clique em Run para executar o código.