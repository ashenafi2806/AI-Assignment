# Differential Evolution Optimization
## Project Overview
This project implements the **Differential Evolution (DE)** algorithm, a stochastic population-based optimization method used to find the **minimum of an objective function**.  

We demonstrate DE by minimizing the **Sphere function**, a common benchmark in optimization problems.


## Algorithm Details
**Differential Evolution** works by:
1. **Initializing a population** of candidate solutions randomly within given bounds.  
2. Iteratively generating **mutant vectors** by combining randomly selected individuals.  
3. Performing **crossover** between the mutant and current individuals.  
4. **Selecting** the best solutions based on fitness (objective function value).  
5. Repeating this process for a fixed number of generations.

**Key Parameters:**
- `population_size`: Number of candidate solutions in the population (default: 30)  
- `F`: Differential weight controlling the mutation (default: 0.8)  
- `CR`: Crossover probability (default: 0.9)  
- `generations`: Number of iterations to perform (default: 500)  

## Objective Function
The **Sphere function** is defined as:
$$f(\mathbf{x})=\sum _{i=1}^{n}x_{i}^{2}$$

- It is a simple convex function with a **global minimum at x = 0**.  
- The DE algorithm searches for the input vector `x` that minimizes this function.  
 
 ## Usage

1. Clone the repository:  
```bash
git clone https://github.com/ashenafi2806/AI-Assisgnment.git
cd AI-Assignment

2. run the Python script 
python differential_evolution.py

3.Output example:
Best Solution: [ 2.26998171e-49 -5.63870316e-49]
Best Fitness: 3.6947790325234505e-97

Dependencies

Python 3.14.0

NumPy

Install dependencies with:

pip install numpy

Results

The algorithm successfully finds a solution close to the global minimum of the Sphere function. Results may vary slightly due to the stochastic nature of Differential Evolution.

