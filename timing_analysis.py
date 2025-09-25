import time
import matplotlib.pyplot as plt
from prime_number_generation import generate_large_prime
from generate_keypair import generate_key_pairs
from encrypt_decrypt_files import main as encrypt_decrypt_main
from pathlib import Path

def time_function(func, *args, iterations=3):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(*args)
        end = time.time()
        times.append((end - start) * 1000)
    return sum(times) / len(times)

def test_baseline():
    bit_sizes = [64, 128, 256, 512, 1024, 2048]
    times = []
    
    for bits in bit_sizes:
        avg_time = time_function(generate_large_prime, bits, iterations=3)
        times.append(avg_time)
        print(f"Prime generation {bits} bits: {avg_time:.2f} ms")
    
    return bit_sizes, times

def test_core():
    bit_sizes = [64, 128, 256, 512, 1024, 2048]
    times = []
    
    for bits in bit_sizes:
        avg_time = time_function(generate_key_pairs, bits, iterations=3)
        times.append(avg_time)
        print(f"Key pair generation {bits} bits: {avg_time:.2f} ms")
    
    return bit_sizes, times

if __name__ == "__main__":
    print("Testing baseline...")
    baseline_bits, baseline_times = test_baseline()
    
    print("\nTesting core...")
    core_bits, core_times = test_core()
    
    print(f"\nBaseline results:")
    for bits, time_ms in zip(baseline_bits, baseline_times):
        print(f"{bits}: {time_ms:.2f}")
        
    print(f"\nCore results:")
    for bits, time_ms in zip(core_bits, core_times):
        print(f"{bits}: {time_ms:.2f}")