import hashlib


class teste:
	def testando():
		entrada = input('Palavra chave: ')
		gerando = hashlib.md5(str.encode(entrada))
		return print(gerando.hexdigest())


show = teste.testando()

