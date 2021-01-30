
## Objetivo
Utilizar as estruturas de dados conhecidas(fila e lista encadeada) em um sistema que fosse utilizavel, nesse caso, um jogo.  

## :rocket: Ferramentas utilizadas
- allegro_monolith-5.2.dll
- Linguagem C
- DevC++

## :warning: OBS
O seu codigo so pode funcionar se tiver o arquivo **allegro_monolith-5.2.dll** (essa foi a versao utilizada por mim), caso nao possua o arquivo
ele gera erro.    

Instale a biblioteca do Allegro, a versao utilizada foi 5.2.2  
link-> [allegro](https://github.com/liballeg/allegro5/releases)

## Instalação

---

### Configurando Allegro no Windows:
1- Extraia o arquivo baixado da sua versao do allegro  

2- Copie o arquivo extraido para o Disco local `\C:`  

### Configurando Allegro no DevC++  

1- Crie um novo codigo Fonte

2- Ferramentas -> Opcoes do Compilador

3- Compilador -> Adicione a Linha de comando do Linker o seguinte: `C:\allegro\lib\liballegro_monolith.dll.a`

4- Diretorios -> Bibliotecas -> Adicione o seguinte caminho: `C:\allegro\lib`

5- Diretorios -> C Includes -> Adicione o seguinte caminho: `C:\allegro\include`
