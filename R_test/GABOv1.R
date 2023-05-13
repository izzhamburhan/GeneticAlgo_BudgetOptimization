library(GA)

# Define budget and budget categories
budget <- 1200
budget_categories <- c("housing", "food & drinks", "life & entertainment", "education", "vehicle")

# Define fitness function
fitness <- function(x) {
  # Calculate total cost
  total_cost <- sum(x)
  # Calculate fitness as the fraction of budget spent
  fitness_value <- (budget - total_cost) / budget
  return(fitness_value)
}

# Define GA parameters
population_size <- 100
mutation_rate <- 0.1
generations <- 100


# Define bounds for decision variables
lower_bounds <- rep(0, length(budget_categories))
upper_bounds <- rep(budget, length(budget_categories))

# Run GA optimization
result <- ga(type = "real", fitness = fitness, min = lower_bounds, max = upper_bounds, 
             popSize = population_size, pcrossover = 0.3, pmutation = mutation_rate, 
             maxiter = generations,keepBest=TRUE, elitism = 5)

# Print result
cat("Best chromosome:", result@solution, "\n")
cat("Fitness:", result@fitnessValue, "\n")
summary(result)
plot(result)
