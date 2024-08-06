## Creating a bit object ###

"""
A bit object has two main features;
-> it can be in one of two state: either up(o) represented by 1 or down(off) by 0.
-> we can flip the bits, that is there is an operation tied to a bit such that its state can be flipped when acted on by it.

I am not sure canonically, but I am representing 0 as off and 1 as on here!
"""
##########################################      
####### 1. Bit class ##################### 
############### ####### ####### ####### ####### 

class Bit:
	"""Generates a bit object
	"""
	def __init__(self, ini_state = 0):
		if ini_state not in (0,1):
			raise ValueError("You have not given a proper bit state")
		else:
			self.state = ini_state
	def __repr__(self):
		return f'This bit is {self.state}.'
	
	def flip(self): ##same as the not gate
		current_state = self.state
		###
		self.state = 1 - current_state
	
	def get(self):
		return self.state
	
def duplicate_bit(bit):
	bit_state = bit.state
	output_bit = Bit(bit_state)
	return output_bit

class NAND_gate:
	@staticmethod  #for static methods, you can call the method using the class itself. There is no need to instantiate an object first to apply the method.
	def compute(bit1, bit2):
		if bit1.state + bit2.state == 2:
			return Bit(0) # return off
		else:
			return Bit(1)

## you can built all kind of gates using the NAND gate

class NOT_gate:
	@staticmethod
	def compute(bit):
		bit1 = Bit(bit.state)
		bit2 = Bit(bit.state)
		output_bit = NAND_gate.compute(bit1, bit2)
		return output_bit
	
class AND_gate:
	@staticmethod
	def compute(bit1, bit2):
		bit3 = NAND_gate.compute(bit1, bit2)
		output_bit = NOT_gate.compute(bit3)
		return output_bit
	
class MemoryBlock:
	#made up of 4 NAND gates
	def __init__(self, s):
		self.set = Bit(s)
		self.output = Bit(0) #a general initalisatoin
	
	def __repr__(self):
		return f'This memory block is set at {self.set.state} and holds memory of {self.output.state}'
	def change_set(self):
		self.set = Bit(1 - self.set.state)

	def compute(self, i):
		if self.set.state == 0:
			pass
		else:
			self.output = i
	def retrieve_memory(self):
		return self.output

