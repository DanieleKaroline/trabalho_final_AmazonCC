import time
#ATRIBUIÇÃO DAS CLASSES
#DEFINIÇÃO DA CLASSE PRODUTO COM CARACTERÍSTICAS DO PRODUTO
class Produto:
    item = None
    nome = None
    valor = None


#DEFINIÇÃO DE CLASSE USUARIO COM ATRIBUTOS PESSOAIS E DE CONTA
class Usuario:
    carrinho = None 
    nome = ''
    cpf = ''
    email = ''
    senha = ''
    saldo = 1000


    #Adicionar os produtos no carrinho
    def adicionar_produto(self, produto):
        self.carrinho.append(produto)
        print('\nO produto', produto.nome,'foi adicionado ao carrinho.')
    
    
    #Atribuir o valor total do carrinho
    def valor_total_carrinho(self):
        valor_total_carrinho = 0
        for produto in self.carrinho:
            valor_total_carrinho += produto.valor
        return valor_total_carrinho


    #Mostra o carrinho do usuario com valor de compra e os produtos adcionados
    def mostrar_carrinho(self):
        print('\n*----------*----------*----------*----------*----------*\n')
        print(f'\n               Este é o carrinho de {self.nome} \n')
        for produto in self.carrinho:
            print(produto.nome, produto.valor)

        print(f'\nValor total do carrinho: R$ {self.valor_total_carrinho()}')
        print(f'Saldo disponível: R${self.saldo - self.valor_total_carrinho()}')
        print('\n*----------*----------*----------*----------*----------*\n')
    

    #Verificar se o usuário possui limite para realizar a compra 
    def tem_limite_para_comprar(self, valor_produto):
        if valor_produto + self.valor_total_carrinho() <= self.saldo:
            return True
        return False


    #Realiza o pagamento do usuário, podendo renovar seu saldo para R$1000
    def pagar(self):
        if self.carrinho != []:
            print(f'Você deseja realizar o pagamento e finalizar o pedido {self.nome}?')
            opcao = input('Digite "sim" para finalizar e encaminhar o seu pedido ou outra tecla para continuar comprando e ser encaminhado para o menu: ')
            
            if opcao == 'sim': 
                self.saldo = self.saldo - self.valor_total_carrinho()
                self.carrinho = [] #zerar o carrinho
                print(F'O Saldo de {self.nome} é: R$ {self.saldo}\nPagamento realizado com sucesso! A comunidade da AmazonCC agradece por efetivar o seu pedido.') 
                self.saldo = 1000
                print(f'Saldo de {self.nome} renovado! Agora o limite é de: R${self.saldo}.')
        
        elif self.carrinho == []:
            print("Não há compras em sua conta. Por favor, realize um pedido antes de efetuar o pagamento!")


#DEFINIÇÃO DE CLASSE LOJA COM ELEMENTOS GERAIS DE PRODUTOS E USUÁRIOS PARA MAZENAMENTO
class Loja:
    produtos = [] 
    usuarios = []
    

    #Cadastro do usuário
    def cadastro(self):
        usuario = Usuario()  
        usuario.carrinho = [] #Para que os usuários não compartilhem da mesma lista 
        while True: #inicia verificação dos dados
            usuario.nome = input('Digite seu nome: ')  
            while not usuario.nome.replace(' ','').isalpha():
                usuario.nome = input('Digite um nome válido: ')

            while usuario.cpf == '':
                usuario.cpf = input('Digite seu CPF: ')
                if not usuario.cpf.isdigit() or not len(usuario.cpf) == 11 or usuario.cpf[::-1] == usuario.cpf::
                    print('CPF inválido.')
                    usuario.cpf = '' #Para que continue dentro da condição e pergunte o cpf novamente

                if usuario.cpf in [u.cpf for u in self.usuarios]:
                    print('Este CPF já está cadastrado!')
                    usuario.cpf = ''   
                 
            usuario.email = input('Digite seu e-mail: ')
            while usuario.email == '' or '@' not in usuario.email: 
                usuario.email = input('Digite um e-mail válido: ')

            usuario.senha = input('Digite uma senha com 6 digitos: ')
            while usuario.senha == '' or len(usuario.senha) !=6: 
                usuario.senha = input('Digite uma senha válida: ')
            print(f'Usuário cadastrado com sucesso! Seja bem vindo(a) {usuario.nome}!')
            break

        self.usuarios.append(usuario) #adicionado dentro da lista da classe
  

    #Verififcar os dados de determinado cliente informado pelo usuário  
    def consulta_cliente(self): 
        while True:
            cpf = input('Insira o seu CPF: ')
            for usuario in self.usuarios:
                if usuario.cpf == cpf:
                    print(f'Usuario encontrado! \nNome: {usuario.nome} \nEmail: {usuario.email} \nSaldo: R${usuario.saldo - usuario.valor_total_carrinho()}')
                    return usuario
            print('CPF inválido! Tente consultar o cliente novamente.')


    #Para pegar cada cliente individualmente 
    def get_cliente(self):
        while True:
            cpf = input('Insira o seu CPF: ')
            senha = input('Insira sua senha: ')

            for usuario in self.usuarios:
               if usuario.cpf == cpf and usuario.senha==senha:
                   return usuario
            print('Usuário não encontrado.\nCPF ou senha incorreta, tente novamente.')
            

# PRODUTOS
    #Para adicionar os produtos 
    def adicionar_produto(self, item_produto, nome_produto, valor_produto): #self se refere a própria classe,e nesse caso recebe a atribuição de produto
        produto = Produto() #produto é o argumento que está sendo passado
        produto.nome = nome_produto
        produto.valor = valor_produto
        produto.item = item_produto
        self.produtos.append(produto) #utilizar o self pra se referir aos próprios métodos da função


    #Adição de produtos na loja
    def popular_produtos(self): #entende que é um método da classe
        self.adicionar_produto(1,'Mentirosos -> E.LOCKHART', 24.90)
        self.adicionar_produto(2,'O lado feio do amor -> COLLEN HOOVER', 39.90)
        self.adicionar_produto(3,'Os sete maridos de Evelyn Hugo -> TAYLOR JENKINS REID', 24.80)
        self.adicionar_produto(4,'Vermelho branco e sangue azul -> CASEY MCQUISTION', 23.90)
        self.adicionar_produto(5,'As mil partes do meu coração -> COLLEN HOOVER', 30)
        self.adicionar_produto(6,'Kit Livros - Coleção Corte de Espinhos e Rosas - 5 Volumes -> SARAH J. MASS', 225)
        self.adicionar_produto(7,'Coleção Harry Potter - 7 Volumes -> J.K ROWLING', 250)
        self.adicionar_produto(8,'Por lugares incríveis -> JENNIFER NIVEN:', 25)
        self.adicionar_produto(9,'É assim que acaba -> COLLEN HOOVER:', 30)
        self.adicionar_produto(10,'O poder da ação -> PAULO VIEIRA:', 30)
        self.adicionar_produto(11,'Kit A Rainha Vermelha - Coleção 5 livros -> VICTORIA AVEYARD: R$', 220)
        self.adicionar_produto(12,'O homem de giz -> C.J. TUDOR: R$', 34)
        self.adicionar_produto(13,'A revolução dos bichos -> GEORGE ORWELL', 15)
        self.adicionar_produto(14,'O que o sol faz com as flores -> RUPI KAUR', 25)
        self.adicionar_produto(15,"Teto para dois -> BETH O'LEARY", 37)
        self.adicionar_produto(16,'Todas as suas (Im)perfeições -> COLLEN HOOVER', 30)
        self.adicionar_produto(17,'Jogo de espelhos -> CARA DELEVINGNE E ROWAN COLEMAN', 25)
        self.adicionar_produto(18,'Kit A Seleção - 6 Livros -> KIERA CASS', 225)
        self.adicionar_produto(19,'As vantagens de ser invisível -> STEPHEN CHBOSKY', 25)
        self.adicionar_produto(20,'Kit Como eu era antes de você - 3 LIVROS -> JOJO MOYES', 85)


    #Para listar os produtos disponíveis para compra 
    def listar_produtos(self):
        for p in self.produtos: 
            print(f'{p.item} -- {p.nome} -- R${p.valor}')

# COMPRAS
    #Verifica os dados do usuario para poder disponibilizar a opção de compra
    #Após, o usuário pode adicionar produtos ao seu carrinho de compras
    def comprar(self, usuario=None): 
        if not usuario: #Na opção 04 não sabemos qual é o usuário, por isso o usuário  vem como None
            usuario = self.get_cliente() #Buscar o cliente
            print(f'\n----- Usuario encontrado! Comprando com {usuario.nome} -----\n')
            
        self.listar_produtos()
        item = int(input('\nDigite o código do produto que você deseja comprar: '))

        for produto in self.produtos: 
            if produto.item == item: #Verifica se o produto é listado
                if usuario.tem_limite_para_comprar(produto.valor): #Verifica se o usuário possui limite de compra
                    usuario.adicionar_produto(produto)
                else: 
                     #Se não, ele será informado
                    print('Usuario sem limite. Favor, pague sua fatura!')

        usuario.mostrar_carrinho()
        opcao = input('\nDigite 1 para continuar comprando ou outra tecla para sair: ')
        if opcao == '1':
            self.comprar(usuario) #o usuário deseja comprar e sabemos qual é o usuário


    #Mostar o carrinho a partir do cliente encontrado
    def mostrar_carrinho_de_usuario(self):
        usuario = self.get_cliente()
        usuario.mostrar_carrinho()


    #Pagar o carrinho de determinado usuário
    def pagar_carrinho_de_usuario(self):
        usuario = self.get_cliente()
        usuario.pagar()


loja = Loja() 
loja.popular_produtos()
opcao = None
print('\n*----------*----------*----------*----------*----------*\n')
print('Olá, seja bem-vindx a AmazonCC!\nPara acessar o menu basta digitar o código da operação e\naproveitar as novidades em livros que temos na loja.\nNão perca tempo e garanta já o seu!')


#MENU DAS OPÇÕES DE PRODUTOS DISPONÍVEIS
while (opcao !='07'):
    time.sleep(3)
    print('\n*----------*----------*----------*----------*----------*\n')
    opcao = input('-> 01: Cadastro \n-> 02: Consultar Cliente \n-> 03: Listar Produtos \n-> 04: Comprar \n-> 05: Carrinho de Compras \n-> 06: Pagar Contas \n-> 07: Sair\nOpção: ') 
    print('\n*----------*----------*----------*----------*----------*\n')

    if opcao == '01': 
        print('Opção selecionada: Cadastro')
        loja.cadastro()
    
    elif opcao == '02':
        print('Opção selecionada: Consultar cliente')
        loja.consulta_cliente()
    
    elif opcao == '03':
        print('Opção selecionada: Listar produtos')
        print(loja.listar_produtos())

    elif opcao == '04': #O usuário deseja comprar mas não sabemos com qual usuario
        print('Opção selecionada: Comprar')
        loja.comprar() 

    elif opcao == "05": 
        print('Opção selecionada: Carrinho de compras')
        loja.mostrar_carrinho_de_usuario()

    elif opcao == '06':
        print('Opção selecionada: Pagar contas')
        loja.pagar_carrinho_de_usuario()

    elif opcao == '07': 
        print('Opção selecionada: Sair')
    
    elif opcao != '01' or '02' or '03' or '04' or '05' or '06' or '07': 
        print("Opção inválida! Tente novamente.")
