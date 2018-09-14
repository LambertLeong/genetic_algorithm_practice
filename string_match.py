import random
import string
import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from string import ascii_lowercase
from string import ascii_uppercase

class Agent:
	
	def __init__(self,length):
		
		self.string = ''.join(random.choice(string.letters) for _ in xrange(length))
		self.fitness = -1

	def __str__(self):
		return 'String: '+str(self.string)+' Fitness: '+str(self.fitness) 

def brute_force():
	
	search_str = ''
	
	for c in in_str:
		letter = ''
		for d in ascii_lowercase:
			if c == d:
				search_str += d
				break
		for D in ascii_uppercase:
			if c == D:
				search_str += D
				break
	if search_str == in_str:
		print 'FOUND'
		print 'search_str is ',search_str,' in_str is ',in_str
		sys.exit(0)
	else:
		print 'search_str is ',search_str,' in_str is ',in_str
		print 'ERROR NOT FOUND'
		sys.exit(1)


def ga():

	agents = init_agents(population, in_str_len)
	
	for generation in xrange(generations):
		
		print 'Generation '+str(generation)
		
		agents = fitness(agents)
		agents = selection(agents)
		agents = crossover(agents)
		agents = mutation(agents)

		if any(agent.fitness >= 100 for agent in agents):
		
			print 'Threshold met!'
			exit(0)

def init_agents(population, length):

	return[Agent(length) for _ in xrange(population)]

def fitness(agents):
	
	for agent in agents:
	
		total = len(in_str)*2
		score = 0
		for i, letter in enumerate(agent.string):
				if in_str[i] == letter:
					score += 1
		compare_str = in_str
		for a_char in agent.string:
			for i, in_char in enumerate(compare_str):
				if a_char == in_char:
					score += 1
					compare_str = compare_str[:i]+compare_str[i+1:]
					break
		agent.fitness = int((float(score)/float(total))*100)				

	return agents

def selection(agents):

	agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
#	print '\n'.join(map(str,agents))
	agents = agents[:int(0.2*len(agents))]

	return agents

def crossover(agents):
#	print 'RAND AGENT IS '+str(random.choice(agents))	
	offspring = []
	
	for _ in xrange((population - len(agents))/2):
		parent1 = random.choice(agents)
		parent2 = random.choice(agents)
		child1 = Agent(in_str_len)
		child2 = Agent(in_str_len)
		split = random.randint(0, in_str_len)
		child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
		child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

		offspring.append(child1)
		offspring.append(child2)

	agents.extend(offspring)

	return agents

def mutation(agents):
	
	for agent in agents:
		
		for idx, param in enumerate(agent.string):

			if random.uniform(0.0, 1.0) <= 0.1:
			
				agent.string = agent.string[0:idx] + random.choice(string.letters) + agent.string[idx+1:in_str_len]

	return agents

def parse_arguments():

	parser = argparse.ArgumentParser(epilog="""""",formatter_class=RawTextHelpFormatter)

	parser.add_argument('-in', '-i', action='store', type=str,
				    dest='in_str', metavar='<input string>',
				    required=True, help='String that the genetic algorithm will try to match')
	parser.add_argument('--search', '-a', action='store',
                            dest='algorithm', metavar='<search algorithm>',
                            required=True, help='enter "genetic" or "g" to use a genetic algorithm or "brute" or "b" to brute force string matching')
	return parser.parse_args()

in_str = None
in_str_len = None
population = 20
generations = 10000

if __name__== '__main__':

	argv = parse_arguments()
	if not argv.in_str.isalpha():
		print 'Error!\nonly apha letter charachters allowed\nExititng'
		sys.exit(1)

	in_str = argv.in_str
	in_str_len = len(in_str)
	if argv.algorithm == 'genetic' or argv.algorithm == 'g':
		ga()
	elif argv.algorithm == 'brute' or argv.algorithm == 'b':
		brute_force()
		#print 'to be implemented'
		#sys.exit(1)
	else:
		sys.exit(1)
