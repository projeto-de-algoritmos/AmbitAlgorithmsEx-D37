# Integrantes

|                         Nome                         | Matrícula |
| :--------------------------------------------------: | :-------: |
|  [Pedro Torreão](https://github.com/PedroTorreao21)  | 190036761 |
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421 |

# Introdução

Este repositório foi criado para o desenvolvimento do segundo módulo sobre Algoritmos Ambiciosos da disciplina Projeto de Algoritmos do Professor Maurício Serrano.

# Apresentação

[Link para a apresentação da dupla](https://youtu.be/YVAwHJnen7k)

# Foram feitos os exercícios no LeetCode

## [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)

Neste método, os intervalos são organizados em ordem crescente com base em seus tempos de término (a[1]). Em seguida, percorremos os intervalos a partir do segundo intervalo, verificando se há alguma sobreposição com o intervalo anterior. Se houver sobreposição, aumentamos o contador count. Caso contrário, atualizamos o tempo de término end para o tempo de término do intervalo atual. Após a conclusão do loop, o valor de count representa o número mínimo de intervalos a serem excluídos para evitar sobreposições. Essa abordagem faz uso do algoritmo de Agendamento de Intervalos para selecionar o conjunto máximo de intervalos sem sobreposição.

![Non-overlapping Intervals](/images/435.jpeg)

## [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/)

Esta solução utiliza o algoritmo "Agendamento para Minimizar Atrasos" com o objetivo de maximizar o número de cursos concluídos dentro dos prazos estabelecidos. O algoritmo percorre a lista de cursos, avaliando a possibilidade de concluir cada curso no prazo máximo determinado. Se não for viável, o algoritmo realiza uma substituição, trocando um curso com um prazo máximo maior pelo curso atual, desde que isso resulte em um atraso total menor.

![Course Schedule III](/images/630.jpeg)

## [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/description/)

Existem n voos rotulados de 1 a n.

Você recebe uma série de reservas de voos, onde bookings[i] = [firsti, lasti, Seati] representa uma reserva para voos firsti até lasti (inclusive) com assentos assentos reservados para cada voo no intervalo.

Retorna uma resposta de matriz de comprimento n, onde resposta[i] é o número total de assentos reservados para o voo i.

![Corporate Flight Bookings](/images/1109.jpg)

## [535. Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)

TinyURL é um serviço de encurtamento de URL onde você insere um URL como https://leetcode.com/problems/design-tinyurl e retorna um URL curto como http://tinyurl.com/4e9iAk. Projete uma classe para codificar um URL e decodificar um URL minúsculo.

Não há restrição sobre como seu algoritmo de codificação/decodificação deve funcionar. Você só precisa garantir que um URL possa ser codificado em um URL minúsculo e que o URL minúsculo possa ser decodificado no URL original.

Implemente a classe Solution:

Solution() Inicializa o objeto do sistema.
String encode (String longUrl) Retorna um pequeno URL para o longUrl fornecido.
String decode(String shortUrl) Retorna o URL longo original para o shortUrl fornecido. É garantido que o shortUrl fornecido foi codificado pelo mesmo objeto.

![Encode and Decode TinyURL](/images/535.jpg)

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
