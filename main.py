# importing the function "calculate" from the module 'mean_var_std'
from mean_var_std import calculate

# list of numbers to analyze
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# calling the function and storing the results in the variable 'result'
result = calculate(numbers)

# printing the results
print("Calculation results:\n")
for key, value in result.items():
    print(f"{key} → {value}")