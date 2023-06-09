from abc import ABCMeta, abstractmethod

class IPrototype(metaclass= ABCMeta):

	@abstractmethod
	def clone():
		pass
