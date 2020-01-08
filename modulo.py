import hashlib


class test:
	def testing():
		home = input('PassWord: ')
		generating = hashlib.md5(str.encode(home))
		return print(generating.hexdigest())


show = test.testing()

