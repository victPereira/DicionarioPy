# Dicionario Vorium

Esse programa é um dicionário que busca a definição de uma palavra a partir de uma API e exibe os significados e exemplos em frames dentro de uma janela

##Tecnologias utilizadas

Python 3.8.5
Tkinter 8.6
Pillow 8.1.0
Requests 2.25.1
JSON 2.0.9
TkScrolledFrame 1.1.0

## O programa utiliza as seguintes bibliotecas:

-tkinter e ttk: para construir a interface gráfica.

-PIL: para abrir e manipular imagens.

-tkscrolledframe: para criar uma área rolável dentro da janela.

-requests e json: para fazer a requisição HTTP e tratar a resposta JSON


##Interface Gráfica

A interface gráfica é construída usando a biblioteca tkinter. A janela principal tem o tamanho de 350x415 pixels e não pode ser redimensionada. Ela é composta por três frames:

-O frame superior contém o logo e o nome do dicionário.

-O frame do meio contém um campo de entrada para a palavra a ser pesquisada.

-O frame inferior contém a lista de significados retornados pela API.
