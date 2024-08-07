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
	

##########################################      
######## 2. LOGIC GATE class ##################### 
############################################### 


class NAND_gate:
	@staticmethod  
	#for static methods, you can call the method using the class itself. There is no need to instantiate an object first to apply the method.
	def compute(bit1, bit2):
		if (type(bit1), type(bit2)) != (Bit, Bit):
			raise ValueError(" You have not supplied a bit object")
		if bit1.state + bit2.state == 2:
			return Bit(0) # return off
		else:
			return Bit(1)

## NAND gates are the fundamental gates from which other gates are made!

class NOT_gate:
	@staticmethod
	def compute(bit):
		output_bit = NAND_gate.compute(bit, bit)
		return output_bit
	
class AND_gate:
	@staticmethod
	def compute(bit1, bit2):
		output_bit = NOT_gate.compute(NAND_gate.compute(bit1, bit2))
		return output_bit


##########################################      
######## 3. Memory class ##################### 
########################################### 

class MemoryBlock:
	#made up of 4 NAND gates
	def __init__(self, s):
		self.switch = Bit(s)
		self.output = Bit(0) #a general initalisatoin
	
	def __repr__(self):
		return f'This memory block is set at {self.set.get()} and holds memory of {self.output.get()}'
	
	def change_switch(self):
		self.switch = Bit(1 - self.switch.state)

	def compute(self, i):
		if self.switch.state == 1:
			self.output = i
		else:
			pass

	def retrieve_memory(self):
		return self.output.state
	

##########################################      
####### 4. Byte class ##################### 
########################################### 

class Byte:
    ##initialisation of 8 memory blocks
    def __init__(self, s_bit = Bit(1)):
        self.memory_blocks = [MemoryBlock(s_bit.get()) for _ in range(8)] #by default the switch is on

    def change_switch(self):
        [memory_block.change_switch() for memory_block in self.memory_blocks]

    def compute(self, input_8bit):
        if len(input_8bit) != 8:
            raise ValueError('You have not given a valid 8 bit string')
        [memory_block.compute(Bit(int(bit))) for memory_block, bit in zip(self.memory_blocks, input_8bit)]

    def retrieve_memory(self):
        output_string = ''
        for memory_block in self.memory_blocks:
            output_string += str(memory_block.retrieve_memory())
        return output_string
    
    def retrieve_switch(self):
        return self.memory_blocks[0].switch.get()
    
    def __repr__(self):
        return f'This memory block is set at {self.retrieve_switch()} and holds memory of {self.retrieve_memory()}'
	


##########################################      
####### 5.  Enabler and Register class ##################### 
###########################################

class Enabler:

	def __init__(self, e = Bit(1)):
		self.e_bit = e
		self.output = Byte()
	def change_switch(self):
		self.e_bit.flip()
	
	def compute(self, input_bit_string):
		if self.e_bit.state == 1:
			B = Byte()
			B.compute(input_bit_string)
			self.output = B
	def retrieve_switch(self):
		return self.e_bit.get()
	def retrieve_memory(self):
		return self.output.retrieve_memory()
	def __repr__(self) -> str:
		return f'This Enabler is set at {self.e_bit.state} and outputs {self.output.retrieve_memory()}'
	
class Register:

	#Stores the input bits into a byte and if needed outputs it.
	def __init__(self, e, s):
		self.byte = Byte(s) #initialises an empty byte
		self.enab = Enabler(e) #enabler object tied to the byte object

	def change_e_switch(self):
		self.enab.change_switch()
	def change_s_switch(self):
		self.byte.change_switch()

	def compute(self, input_bit_string):
		self.enab = Enabler()
		self.byte.compute(input_bit_string)
		if self.byte.retrieve_switch() == 1:
			self.enab.compute(input_bit_string)
			return self.enab.retrieve_memory()
	def __repr__(self):
		return (f'This Register has s_switch {self.byte.retrieve_switch()} and e_switch {self.enab.retrieve_switch()}\n' 
		  		f'It holds a memory of {self.byte.retrieve_memory()} and output of {self.enab.retrieve_memory()}')
	

##########################################      
####### 5.  Enabler and Register class ##################### 
###########################################




