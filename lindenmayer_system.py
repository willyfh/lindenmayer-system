"""
__author__  = Willy Fitra Hendria
"""

def generate_lindenmayer_system(axiom, rules, max_steps):
	current_seq =  axiom
	print("step= 0 ,\t",current_seq)
	for i in range(max_steps):
		next_seq = ""
		for c in current_seq:
			if c in rules:
				next_seq += rules[c]
			else:
				next_seq += c
		current_seq = next_seq
		print("step=",i+1,",\t",current_seq)
	


print("---------------------")
print("Lindenmayer System #1 (Fibonacci)")
print("---------------------")	

axiom = "C"
rules = {"C":"A", "A":"CA"}
max_steps = 5

generate_lindenmayer_system(axiom, rules, max_steps)

print("---------------------")
print("Lindenmayer System #2")
print("---------------------")	

axiom = "R"
rules = {"R":"RS", "S":"ST", "T":"TR"}
max_steps = 5

generate_lindenmayer_system(axiom, rules, max_steps)

print("---------------------")
print("Sample with Constants")
print("---------------------")	

axiom = "B"
rules = {"B":"F[-B]+B", "F":"FF"}
max_steps = 3

generate_lindenmayer_system(axiom, rules, max_steps)