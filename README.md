# Weather

Implementação de um *webservice* que consuma o serviço de previsão do tempo do ClimaTempo ([API Advisor](https://advisor.climatempo.com.br/)) com o objetivo de retornar dados climáticos sobre temperatura e precipitações de uma determinada cidade.


## Pré requisitos

Ferramentas necessárias para o funcionamento do *webservice*.

* [Python](https://www.python.org/downloads/release/python-372/) - Linguagem de programação.
* [Flask](http://flask.pocoo.org/docs/1.0/) - *Framework* utilizado na construção do webservice.
* [Pip](https://pip.pypa.io/en/stable/) - Gerenciador de pacotes usado para instalar e gerenciar pacotes de software escritos na linguagem de programação Python
* [MySQL](https://www.mysql.com/downloads/) - Banco de dados relacional.

## Instalação

Para instalar os pacotes, certifique-se de já ter instalado em sua máquina o [pip](https://pip.pypa.io/en/stable/). 

Instale as bibliotecas executando o comando abaixo:

```bash
$ pip install -r requirements.txt
```

Faça a importação do arquivo ***schema.db*** para a criação do banco de dados.

## Como Usar

Uma vez que os pacotes são instalados, inicie o *Flask*:

```bash
$ flask run
```

## Autor

* **José Rodolfo** - [Zé Rodolfo](https://github.com/ZeRodolfo)

## Contribuição
*Pull requests* são bem vindos. Para alterações importantes, por favor, abra um problema primeiro para discutir o que você gostaria de mudar.


## Licença
[GNU](https://www.gnu.org/licenses/licenses.html)