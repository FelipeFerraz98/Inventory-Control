class Produto:
    def __init__(self, nome, preco, descricao, quantidade):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome: {self.nome}, Preço: {self.preco}, Descrição: {self.descricao}, Quantidade: {self.quantidade}"

    def to_dict(self):
        return {
            'nome': self.nome,
            'preco': self.preco,
            'descricao': self.descricao,
            'quantidade': self.quantidade
        }

    @staticmethod
    def from_dict(d):
        return Produto(d['nome'], d['preco'], d['descricao'], d['quantidade'])
