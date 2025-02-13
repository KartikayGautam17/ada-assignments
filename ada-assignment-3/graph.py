import matplotlib.pyplot as plt

input_sizes=[10,50,100,500,1000,5000]
binary_best_stepscount=[1,1,1,1,1,1]
binary_avg_stepscount=[2,3,6,7,8,11]
binary_worst_stepscount=[3,5,6,8,9,12]

plt.figure(figsize=(8,5))
plt.plot(input_sizes,binary_best_stepscount,'g-o',label='Binary Best Case')
plt.plot(input_sizes,binary_avg_stepscount,'b-o',label='Binary Avg Case')
plt.plot(input_sizes,binary_worst_stepscount,'r-o',label='Binary Worst Case')
plt.xlabel("Input Size")
plt.ylabel("Number of Steps")
plt.title("Binary Search Analysis")
plt.legend()
plt.grid(True)
plt.show()