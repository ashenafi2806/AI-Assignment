#Group members: 
#Abdi Ahmed UGR/6905/14
#Ashenafi Bizuwork UGR/2063/15
#Feven Alemayehu UGR/0918/13
#Fewzan Abdulkerim UGR/7225/15

import numpy as np


def differential_evolution(
    objective_function,
    bounds,
    population_size=30,
    F=0.8,
    CR=0.9,
    generations=500
):
    dim = len(bounds)

    population = np.random.rand(population_size, dim)
    for i in range(dim):
        min_b, max_b = bounds[i]
        population[:, i] = min_b + population[:, i] * (max_b - min_b)

    fitness = np.array([objective_function(ind) for ind in population])

    for gen in range(generations):
        for i in range(population_size):
            indices = [idx for idx in range(population_size) if idx != i]
            a, b, c = population[np.random.choice(indices, 3, replace=False)]
            mutant = a + F * (b - c)

            mutant = np.clip(
                mutant,
                [b[0] for b in bounds],
                [b[1] for b in bounds]
            )

            crossover = np.random.rand(dim) < CR
            if not np.any(crossover):
                crossover[np.random.randint(0, dim)] = True

            trial = np.where(crossover, mutant, population[i])

            trial_fitness = objective_function(trial)
            if trial_fitness < fitness[i]:
                population[i] = trial
                fitness[i] = trial_fitness

    best_index = np.argmin(fitness)
    return population[best_index], fitness[best_index]

#sphere function that will be minimizeed
def sphere_function(x):
    return sum(xi**2 for xi in x)

#setting the bounds for the input variables
bounds = [(-5, 5), (-5, 5)] 

#running differential evol.
best_solution, best_fitness = differential_evolution(
    objective_function=sphere_function,
    bounds=bounds,
    population_size=30,
    F=0.8,
    CR=0.9,
    generations=500
)

#displaying results 
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)

