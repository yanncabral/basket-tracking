# Projeto de Visão Computacional (INF1031 - 2022.1)

Este projeto visa desenvolver um sistema de visão computacional para reconhecer e rastrear jogadores e a bola em uma quadra de basquete. O sistema será capaz de identificar os jogadores e a bola e rastreá-los em tempo real, permitindo que os espectadores acompanhem a partida.

## Introdução

Este projeto foi desenvolvido com o objetivo de reconhecer e rastrear jogadores e a bola em uma quadra de basquete. Foram utilizadas diversas técnicas de visão computacional para atingir este objetivo, e apesar de ser um projeto em andamento, os resultados foram bastante satisfatórios.

Os métodos utilizados foram:

- Detecção de bordas
- Detecção de cores
- Rastreamento de objetos

Os algoritmos foram aplicados a diversos quadros de um vídeo de um jogo de basquete, e foram capazes de reconhecer e rastrear com sucesso os jogadores e a bola.

## Métodos

### Detecção de bordas

A detecção de bordas foi feita utilizando o algoritmo Canny. Este algoritmo foi escolhido por ser um dos mais precisos para a detecção de bordas em imagens.

### Detecção de cores

Para a detecção de cores, foi utilizado o algoritmo de segmentação de cores HSV (Hue, Saturation, Value). Essa é uma boa abordagem porque cores parecidas tem um HSV parecido, assim, é possível encontrar ranges de cores mais condizentes com as variações do mundo real.

### Rastreamento de objetos

Para o rastreamento de objetos, foi utilizado o algoritmo de rastreamento de Kalman. Este algoritmo é muito eficiente para o rastreamento de objetos em movimento em imagens.

## Métodos

O reconhecimento e rastreamento de jogadores e bola será realizado utilizando técnicas de visão computacional, aprendizado de máquina e processamento de imagens. As imagens da quadra de basquete serão capturadas por uma câmera e processadas para detectar e rastrear os objetos de interesse. Para isso, serão utilizadas técnicas de detecção de objetos, rastreamento de objetos e aprendizado de máquina.

## Resultados

Espera-se que o sistema desenvolvido seja capaz de reconhecer e rastrear os jogadores e a bola em tempo real, permitindo que os espectadores acompanhem a partida. Além disso, o sistema poderá ser utilizado para analisar o jogo, fornecendo dados estatísticos sobre a performance dos jogadores e a dinâmica da partida.

No entanto, esse é um trabalho ainda em andamento, e nosso estagio atual de desenvolvimento é:

- [x] Detecção da quadra
- [x] Detecção dos jogadores
- [ ] Detecção da bola na maioria dos frames.
- [ ] Subtração de background p/ melhorar reconhecimento dos objetos.
- [ ] Usar as duas versões do video p/ medir também a altura da bola.
    