import matplotlib.pyplot as plt
import numpy as np

baseline_n = [64, 128, 256, 512, 1024, 2048]
baseline_times = [0.49, 1.87, 12.36, 150.88, 1563.95, 14457.44]

core_n = [64, 128, 256, 512, 1024, 2048]
core_times = [0.59, 3.62, 32.39, 289.13, 3311.74, 38856.16]

def calculate_constant(n_values, times):
    constants = [t / (n**4) for n, t in zip(n_values, times)]
    return sum(constants[-3:]) / 3

baseline_k = calculate_constant(baseline_n, baseline_times)
core_k = calculate_constant(core_n, core_times)

print(f"Baseline constant: {baseline_k:.2e}")
print(f"Core constant: {core_k:.2e}")

def create_plot(n_values, times, k, title, filename):
    plt.figure(figsize=(10, 6))
    
    plt.plot(n_values, times, 'bo-', label='Empirical Data', linewidth=2)
    
    theoretical = [k * (n**4) for n in n_values]
    plt.plot(n_values, theoretical, 'r--', label='Theoretical O(n^4)', linewidth=2)
    
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (ms)')
    plt.title(title)
    plt.legend()
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

create_plot(baseline_n, baseline_times, baseline_k, 
           'Prime Number Generation Performance', 'baseline_plot.png')

create_plot(core_n, core_times, core_k,
           'Key Pair Generation Performance', 'core_plot.png')