library(GA)

# Define budget and budget categories
budget <- 1200
budget_categories <- c("Housing", "Food & Drinks", "Life & Entertainment", "Education", "Vehicle","Shopping")

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
mutation_rate <- 0.5
generations <- 100
elite <- 5

# Run GA optimization
result <- ga(type = "real", fitness = fitness, lower = c(200,200,10,0,150,0), upper = c(300,300,150,150,250,100), 
             popSize = population_size, pcrossover = 0.7, pmutation = mutation_rate, 
             maxiter = generations, elitism = elite, keepBest=TRUE)

# Print result
cat("Best chromosome:", result@solution, "\n")
cat("Fitness:", result@fitnessValue, "\n")
summary(result)
plot(result)
