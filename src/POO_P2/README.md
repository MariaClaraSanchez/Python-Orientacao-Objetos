# Anotações sobre o curso

Usando o '__' o atributo fica privado.
Se usar apenas o _ o atributo fica protegido, mas quando usado sinaliza que deve ser 
tratado como um atributo "privado", fazendo com que acessá-lo diretamente possa ser perigoso.

Código "pythônico": é um código mais bem feito, com design melhor, mais bem estruturado e expressivo.

Para chamar todos os métodoss e atributos da class mãe é só utilizar : super()

Métodos de classe:declarados com @classmethod. 

Quando criamos um método de classe, temos acesso aos atributos da classe.
Em vez de usar o self usamos o cls para o método, 
pois nesse caso sempre recebemos uma instância da classe como primeiro argumento. 

Métodos estáticos
Podemos criar também métodos ligados a classe usando o @staticmethod.
Com o @staticmethod não é possível acessar as informações da classe.
Apenas o método e acessível a partir da classe e também da instância.

O hasattr() é um método retorna true se um objeto tiver o atributo nomeado 
fornecido e false se não tiver.

Assim como o __str__, existe outro método especial chamado __repr__, 
que é usado para mostrar uma representação que ajude no debug ou log de um código.

__getitem__() é um método que define algo como iterável.

Interface vs Reuso:

Interface, quando queremos resolver questões relativas a polimorfismo;
Reuso do código, ou remoção de duplicações.


Para ter as vantagens de iterável de um list, sem precisar fazer herança no python utilizados O
__getitem__() que é um modo Duck typing

A caracteristica Duck typing do python é um estilo de codificação 
de linguagens dinamicamente tipadas onde o tipo de uma variável não importa, 
contanto que seu comportamento seja o desejado.


No Python Data Model, todo objeto em Python pode se comportar de forma a ser 
compatível e mais próximo à linguagem, e de toda a ideia idiomática dela. 

| Para que?            | Método                                       |
|----------------------|----------------------------------------------|
| Inicialização        | __init__                                     |
| Representação        | __str__                                      |
| Container, sequência | __contains__, __iter__, __len__, __getitem__ |
| Numéricos            | __add__, __sub__, __mul__, __mod__           |

O __repr__(), utilizado para demonstrar como o objeto foi criado
O __contains__(), que também fará o in funcionar
O __iter__(), define protocolos de iteração
O __len__(), retorna o tamanho da lista
O __getitem__(), ajuda a percorrermos a lista e pegarmos um item específico dela.

|       Para quê?      |                     Como?                     |
|:--------------------:|:---------------------------------------------:|
| Inicialização        | obj = Novo()                                  |
| Representação        | print(obj), str(obj), repr(obj)               |
| Container, sequência | len(obj), item in obj, for i in obj, obj[2:3] |
| Numéricos            | obj + outro_obj, obj * obj                    |


Sobre herença múltipla:

1) Os mixins são classes herdadas que não precisam ser instanciadas e contém preocupações comuns a diversas classes.

3) Podemos usar composição para substituir herança como boa prática de orientação a objetos.

