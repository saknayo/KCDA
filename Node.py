# Node.py
import time	

class Node:
	def __init__(self):
		self.nid=Node._nidG()

	def _nidG():
		return repr(time.time())

class Object(Node):
	def isObject(node):
		try :
			return node._objtect()
		except AttributeError:
			return False

	def __init__(self):
		super(Object,self).__init__()
		self.description='node based object'

	def _object(self):
		return self.description

class Action(Node):
	def isAction(node):
		try :
			return node._action()
		except AttributeError:
			return False

	def __init__(self):
		super(Action,self).__init__()
		self.description='node based action'

	def _action(self):
		return self.description

if __name__ == '__main__' :
	tnode=Node()
	tobj=Object()
	tact=Action()