import time
import os
from pathlib import Path
from encrypt_decrypt_files import main as encrypt_decrypt_main

def time_encrypt_decrypt(key_bits):
    os.system(f"python3 generate_keypair.py {key_bits} test_key_{key_bits}")
    
    public_key = Path(f"test_key_{key_bits}.public.txt")
    private_key = Path(f"test_key_{key_bits}.private.txt")
    
    input_file = Path("1Nephi.txt")
    encrypted_file = Path(f"encrypted_{key_bits}.bin")
    decrypted_file = Path(f"decrypted_{key_bits}.txt")
    
    start = time.time()
    encrypt_decrypt_main(public_key, input_file, encrypted_file)
    encrypt_time = (time.time() - start) * 1000

    start = time.time()
    encrypt_decrypt_main(private_key, encrypted_file, decrypted_file)
    decrypt_time = (time.time() - start) * 1000

    public_key.unlink()
    private_key.unlink()
    encrypted_file.unlink()
    decrypted_file.unlink()
    
    return encrypt_time, decrypt_time

key_sizes = [64, 128, 256, 512, 1024, 2048]
encrypt_times = []
decrypt_times = []

for bits in key_sizes:
    enc_time, dec_time = time_encrypt_decrypt(bits)
    encrypt_times.append(enc_time)
    decrypt_times.append(dec_time)
    print(f"{bits} bits - Encrypt: {enc_time:.2f}ms, Decrypt: {dec_time:.2f}ms")

print("\nEncryption results:")
for bits, time_ms in zip(key_sizes, encrypt_times):
    print(f"{bits}: {time_ms:.2f}")
    
print("\nDecryption results:")  
for bits, time_ms in zip(key_sizes, decrypt_times):
    print(f"{bits}: {time_ms:.2f}")