import random
import string
import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from string import ascii_lowercase
from string import ascii_uppercase

class Individual:
	
	def __init__(self,length):
		
		self.string = ''.join(random.choice(string.letters) for _ in xrange(length))
		self.fitness = -1

def brute_force():
	
	search_str = ''
	
	for c in in_str:
		letter = ''
		stop = False
		while stop is False:
			letter = random.choice(string.letters)
			if letter == c:
				search_str += letter
				stop = True
		"""
		for d in ascii_lowercase:
			if c == d:
				search_str += d
				break
		for D in ascii_uppercase:
			if c == D:
				search_str += D
				break
		"""
	if search_str == in_str:
		print 'FOUND'
		print 'search_str is ',search_str,' in_str is ',in_str
		sys.exit(0)
	else:
		print 'search_str is ',search_str,' in_str is ',in_str
		print 'ERROR NOT FOUND'
		sys.exit(1)


def ga():

	individuals = init_individuals(population, in_str_len)
	found = False	
	for generation in xrange(generations):
		
		generation_list.append(generation)
		individuals = fitness(individuals)
		individuals = selection(individuals)
		individuals = crossover(individuals)
		individuals = mutation(individuals)

		if any(individual.fitness >= 100 for individual in individuals):
			found = True	
			break
	return found

def init_individuals(population, length):

	return[Individual(length) for _ in xrange(population)]

def fitness(individuals):
	
	for individual in individuals:
	
		total = len(in_str)*2
		score = 0
		for i, letter in enumerate(individual.string):
				if in_str[i] == letter:
					score += 1
		compare_str = in_str
		for a_char in individual.string:
			for i, in_char in enumerate(compare_str):
				if a_char == in_char:
					score += 1
					compare_str = compare_str[:i]+compare_str[i+1:]
					break
		individual.fitness = int((float(score)/float(total))*100)				
	return individuals

def selection(individuals):

	individuals = sorted(individuals, key=lambda individual: individual.fitness, reverse=True)
	
	max_fit.append(max(individuals, key=lambda individual: individual.fitness).fitness)
	min_fit.append(min(individuals, key=lambda individual: individual.fitness).fitness)
	avg_fit.append(float(sum(i.fitness for i in individuals)//len(individuals)))

	individuals = individuals[:int(0.2*len(individuals))]

	return individuals

def crossover(individuals):
	offspring = []
	
	for _ in xrange((population - len(individuals))/2):
		parent1 = random.choice(individuals)
		parent2 = random.choice(individuals)
		child1 = Individual(in_str_len)
		child2 = Individual(in_str_len)
		split = random.randint(0, in_str_len)
		child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
		child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

		offspring.append(child1)
		offspring.append(child2)

	individuals.extend(offspring)

	return individuals

def mutation(individuals):
	
	for individual in individuals:
		
		for i, param in enumerate(individual.string):

			if random.uniform(0.0, 1.0) <= 0.05:
			
				individual.string = individual.string[0:i] + random.choice(string.letters) + individual.string[i+1:in_str_len]

	return individuals

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
generations = 5000
max_fit = [0]
avg_fit = [0]
min_fit = [0]
generation_list = [0]


if __name__== '__main__':

	argv = parse_arguments()
	if not argv.in_str.isalpha():
		print 'Error!\nonly apha letter charachters allowed\nExititng'
		sys.exit(1)

	in_str = argv.in_str
	in_str_len = len(in_str)
	if argv.algorithm == 'genetic' or argv.algorithm == 'g':
		if ga() is True:

			#sys.exit(0)
			import matplotlib.pyplot as plt
			import pylab
			plt.plot(generation_list, max_fit, label = 'Max Fitness')
			plt.plot(generation_list, avg_fit, label = 'Average Fitness')
			plt.plot(generation_list, min_fit, label = 'Min Fitness')
			pylab.legend(loc='lower right')
			#pylab.ylim(-1.5, 2.0)
			plt.xlabel('Generation')
			plt.ylabel('Fitness Score out of 100')
			plt.title('Genetic Algorithms Performance for Matching String = '+in_str)
			plt.show()
			sys.exit(0)

	elif argv.algorithm == 'brute' or argv.algorithm == 'b':
		brute_force()
		#print 'to be implemented'
		#sys.exit(1)
	else:
		sys.exit(1)
