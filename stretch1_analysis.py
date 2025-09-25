import matplotlib.pyplot as plt
import numpy as np

n_values = [64, 128, 256, 512, 1024, 2048]
encrypt_times = [7.61, 6.55, 4.45, 5.39, 13.78, 34.46]
decrypt_times = [242.72, 510.80, 1514.67, 3817.59, 13957.76, 49028.02]

def calc_linear_constant(n_vals, times):
    constants = [t/n for n, t in zip(n_vals, times)]
    return sum(constants[-3:]) / 3

encrypt_k = calc_linear_constant(n_values, encrypt_times)
decrypt_k = calc_linear_constant(n_values, decrypt_times)

print(f"Encryption constant (O(n)): {encrypt_k:.2e}")
print(f"Decryption constant (O(n)): {decrypt_k:.2e}")

plt.figure(figsize=(10, 6))
plt.plot(n_values, encrypt_times, 'bo-', label='Empirical Data', linewidth=2)
theoretical_enc = [encrypt_k * n for n in n_values]
plt.plot(n_values, theoretical_enc, 'r--', label='Theoretical O(n)', linewidth=2)
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (ms)')
plt.title('Encryption Performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('encryption_plot.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(n_values, decrypt_times, 'bo-', label='Empirical Data', linewidth=2)
theoretical_dec = [decrypt_k * n for n in n_values]
plt.plot(n_values, theoretical_dec, 'r--', label='Theoretical O(n)', linewidth=2)
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (ms)')
plt.title('Decryption Performance')
plt.legend()
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('decryption_plot.png')
plt.show()