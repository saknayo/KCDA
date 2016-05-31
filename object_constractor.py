# object constractor

# fundmental object
class Equipment:
	def __init__(self,id):
		self.id=id
class EquipmentDecorator:
	def __init__(self,equipment):
		''' add the environment parameter '''
class Fleet:
	def __init__(self,id):
		self.id=id
	def base_para_set(self):
		self.id
		self.stype=1
		self.sortno=1

		self.maxHP=10
		self.karyoku=10
		self.soukou=10
		self.raisou=0
		self.kaihi=10
		self.taiku=99
		self.maxeq=[1,1,1,1]
		self.taisen=0
		self.soku=10 # 10:高速 5:低速
		self.saikuteki=9
		self.leng=3 # 3:长 2:中 1:短
		self.luck=10

		self.maxfuel=10
		self.maxbull=10
		self.slotnum=3
		
	def level_up(self):
		''' base para update '''
	def kaisou(self):
		''' base para update '''
		
		
		
		
		

class FleetDecorator:
	def __init__(self,fleet):
		''' add the environment parameter '''
		self.nowhp=10

class log:
	''' data node '''
# event
class Kogeki:
	def __init__(self):
		pass
	# characters --> base class
	self.attack=fleet1
	self.defense=fleet2

	# event type --> method class
	self.type="" # ci normal ...
	self.times=2

	# result --> influence on base object
	self.affected_property_a=[self.a.maxHP]
	self.a_value=9
	self.affected_property_d=[self.d.nowhp]
	self.d_value=9

class Battle:
	pass