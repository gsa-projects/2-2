class IntList(list):
	def append(self, __object: int) -> None:
		if isinstance(__object, int):
			super().append(__object)
		else:
			raise ValueError(f"Only integers and floats are allowed in this list, not {type(__object).__name__}")

class Tensor:
	def __init__(self):
		self.__data = IntList()
	
	def __set__(self, instance, value):
		if isinstance()
	

t = Tensor()
t = (0, ) * 3