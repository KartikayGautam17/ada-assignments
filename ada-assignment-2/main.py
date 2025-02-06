import matplotlib.pyplot as plt


input_sizes = [100, 200, 400, 1600]
linear_best = [1,1,1,1]
linear_avg = [42, 68, 335, 901]
linear_worst = [100, 200, 400, 1600]
binary_best = [1,1,1,1]
binary_avg = [7,5,8,10]
binary_worst = [7,8,9,11]
    
    
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, linear_best, 'g-o', label='Linear Best Case')
plt.plot(input_sizes, binary_best, 'g--s', label='Binary Best Case')
plt.xlabel("Input Size")
plt.ylabel("Number of Steps")
plt.title("Best Case: Linear vs Binary Search")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 5))
plt.plot(input_sizes, linear_avg, 'b-o', label='Linear Avg Case')
plt.plot(input_sizes, binary_avg, 'b--s', label='Binary Avg Case')
plt.xlabel("Input Size")
plt.ylabel("Number of Steps")
plt.title("Average Case: Linear vs Binary Search")
plt.legend()
plt.grid(True)
plt.show()

   
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, linear_worst, 'r-o', label='Linear Worst Case')
plt.plot(input_sizes, binary_worst, 'r--s', label='Binary Worst Case')
plt.xlabel("Input Size")
plt.ylabel("Number of Steps")
plt.title("Worst Case: Linear vs Binary Search")
plt.legend()
plt.grid(True)
plt.show()


   
