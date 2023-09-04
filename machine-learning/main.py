from dataclasses import dataclass
from typing import *
from abc import *
import numpy as np

class Perceptron(metaclass=ABCMeta):
	w: np.ndarray
	b: np.ndarray
	
	def __call__(self, x: np.ndarray) -> np.ndarray:
		return self.forward(x)
	
	@abstractmethod
	def forward(self, x: np.ndarray) -> np.ndarray:
		raise NotImplementedError

class F(Perceptron):
	w = np.array([1, 1])
	b = np.array([7])
	
	def forward(self, x: np.ndarray) -> np.ndarray:
		return self.w * x + self.b

f = F()
print(f(np.array([3, 3])))
