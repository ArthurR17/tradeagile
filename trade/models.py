from django.db import models

# Classe que representa um Vendedor
class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)  # Identificador único do vendedor
    codivende = models.CharField(max_length=10)  # Código do vendedor
    nomevende = models.CharField(max_length=100)  # Nome do vendedor
    razasocvende = models.CharField(max_length=100)  # Razão social do vendedor
    fonevende = models.CharField(max_length=20)  # Telefone do vendedor
    porcvende = models.FloatField()  # Porcentagem de comissão do vendedor

    class Meta:
        db_table = 'vendedor'  # Nome da tabela no banco de dados


# Classe que representa um Produto
class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)  # Identificador único do produto
    codiprod = models.CharField(max_length=20)  # Código do produto
    descprod = models.CharField(max_length=100)  # Descrição do produto
    valorprod = models.FloatField()  # Valor do produto
    situprod = models.CharField(max_length=1)  # Situação do produto (por exemplo, disponível, fora de estoque)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Relacionamento com o fornecedor
    imagem = models.CharField(max_length=200, blank=True, null=True)  # Novo campo para o caminho da imagem do produto

    class Meta:
        db_table = 'produto'  # Nome da tabela no banco de dados



# Classe que representa um Fornecedor
class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)  # Identificador único do fornecedor
    codiforn = models.CharField(max_length=10)  # Código do fornecedor
    nomeforn = models.CharField(max_length=100)  # Nome do fornecedor
    razasocforn = models.CharField(max_length=100)  # Razão social do fornecedor
    foneforn = models.CharField(max_length=20)  # Telefone do fornecedor

    class Meta:
        db_table = 'fornecedor'  # Nome da tabela no banco de dados


# Classe que representa um Cliente
class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)  # Identificador único do cliente
    codcli = models.CharField(max_length=10, verbose_name="Código")  # Código do cliente
    nomecli = models.CharField(max_length=100, verbose_name="Nome")  # Nome do cliente
    razasoccli = models.CharField(max_length=100, verbose_name="Razão Social")  # Razão social do cliente
    datacli = models.DateField(verbose_name="Data")  # Data de registro do cliente
    cnpjcli = models.CharField(max_length=20, verbose_name="CNPJ")  # CNPJ do cliente
    fonecli = models.CharField(max_length=20, verbose_name="Telefone")  # Telefone do cliente
    cidcli = models.CharField(max_length=50, verbose_name="Cidade")  # Cidade do cliente
    estcli = models.CharField(max_length=100, verbose_name="Estado")  # Estado do cliente

    class Meta:
        db_table = 'cliente'  # Nome da tabela no banco de dados




# Classe que representa os itens de uma venda
class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)  # Identificador único do item da venda
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)  # Relacionamento com a venda
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)  # Relacionamento com o produto
    valoritvend = models.FloatField()  # Valor do item da venda
    qtditvend = models.IntegerField()  # Quantidade do item na venda
    descitvend = models.FloatField()  # Desconto aplicado ao item da venda

    class Meta:
        db_table = 'itensvenda'  # Nome da tabela no banco de dados


# Classe que representa uma Venda
class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)  # Identificador único da venda
    codivend = models.CharField(max_length=10)  # Código da venda
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Relacionamento com o cliente
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Relacionamento com o fornecedor
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)  # Relacionamento com o vendedor
    valorvend = models.FloatField()  # Valor total da venda
    descvend = models.FloatField()  # Desconto aplicado à venda
    totalvend = models.FloatField()  # Valor total após descontos
    datavend = models.DateField()  # Data da venda
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão do vendedor

    class Meta:
        db_table = 'venda'  # Nome da tabela no banco de dados


class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True)
    codcli = models.CharField(max_length=10)
    nomecli = models.CharField(max_length=100)
    razasoccli = models.CharField(max_length=100)
    datacli = models.DateField()
    cnpjcli = models.CharField(max_length=20)
    fonecli = models.CharField(max_length=20)
    cidcli = models.CharField(max_length=50)
    estcli = models.CharField(max_length=100)

    class Meta:
        db_table = 'clientesbkp'
