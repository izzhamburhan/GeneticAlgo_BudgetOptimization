import random
import matplotlib.pyplot as plt

#########################
##### Fitness Func  #####
#########################

# Fitness function - calculates the fitness of a given chromosome
def fitness(chromosome, budget):
    total_cost = sum(chromosome.values())
    return (budget - total_cost) / budget

#########################
#### Selection Func  ####
#########################

# Selection function - selects two chromosomes from the population based on their fitness
def selection(population, budget):
    fitness_values = [fitness(chromosome, budget) for chromosome in population] 
    sum_fitness = sum(fitness_values)
    selection_probabilities = [fitness_value/sum_fitness for fitness_value in fitness_values]
    index1 = random.choices(range(len(population)), weights=selection_probabilities)[0]
    index2 = random.choices(range(len(population)), weights=selection_probabilities)[0]
    return population[index1], population[index2]

#########################
#### Crossover Func  ####
#########################

# Crossover function - performs a single-point crossover on two chromosomes
def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(0, len(chromosome1)-1) # can choose between 0-5(untuk point yang mana nak crossover)
    new_chromosome1 = { key: (chromosome1[key] if index <= crossover_point else chromosome2[key]) for index, key in enumerate(chromosome1)} # tukar value dict pada point dengan parent2
    new_chromosome2 = { key: (chromosome2[key] if index <= crossover_point else chromosome1[key]) for index, key in enumerate(chromosome2)} # tukar value dict pada point dengan parent1
    return new_chromosome1, new_chromosome2

#########################
#### Mutation Func   ####
#########################

# Mutation function - mutates a single gene in the chromosome
def mutation(chromosome, mutation_rate):
    for key in chromosome:
        if random.random() < mutation_rate:
            chromosome[key] += random.randint(-10, 10)
    return chromosome


#########################
###### Main Func  #######
#########################

# Main function - runs the genetic algorithm
def genetic_algorithm(budget, population_size, generations, mutation_rate):
    # Generate initial population
    population = [{ 'Shopping': random.randint(0, 150), 'Food & Drink': random.randint(250, 300), 'Life & Entertainment': random.randint(100, 200), 'Vehicle': random.randint(200, 400), 'Housing': random.randint(200, 350), 'Education':random.randint(0,150)} for i in range(population_size)]
    best_chromosome = None
    for i in range(generations):
        # Select two parents from the population
        parent1, parent2 = selection(population, budget)
        # Create two children from the parents
        child1, child2 = crossover(parent1, parent2)
        # Mutate the children
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)
        # Add the children to the population
        population.extend([child1, child2])
        # Keep only the best chromosomes in the population
        population = sorted(population, key=lambda x: fitness(x, budget), reverse=True)[:population_size]
        # Update the best chromosome if necessary
        if best_chromosome is None or fitness(best_chromosome, budget) < fitness(population[0], budget):
            best_chromosome = population[0]
        # Print the best chromosome and its fitness
        print(f"Generation {i}: Best chromosome = {best_chromosome}, Fitness = {fitness(best_chromosome, budget)}")
    return best_chromosome


#########################
###### Main Func  #######
#########################


# Initialization
budget = 1500
population_size = 100
generations = 100
mutation_rate = 0.1
best_chromosome = genetic_algorithm(budget, population_size, generations, mutation_rate)
print(f"Best chromosome: {best_chromosome}, Fitness: {fitness(best_chromosome, budget)}")



population = [{ 'Shopping': random.randint(0, 150), 'Food & Drink': random.randint(250, 300), 'Life & Entertainment': random.randint(100, 200), 'Vehicle': random.randint(200, 400), 'Housing': random.randint(200, 350), 'Education':random.randint(0,150)} for i in range(population_size)]
fitness_values = [fitness(chromosome, budget) for chromosome in population] # fitness value in here

generations = list(range(0, 100))
# fitness_scores = [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Replace with actual fitness scores

plt.plot(generations, fitness_values)
plt.xlabel("Generation")
plt.ylabel("Fitness Score")
plt.title("Fitness Score vs Generation")
plt.savefig("images/generation_fitnessvalue.jpg",dpi=120) 
# plt.show()
plt.close()


with open("metrics.txt", 'w') as outfile:
        outfile.write(f"Best chromosome: {best_chromosome}, Fitness: {fitness(best_chromosome, budget)}")
        
