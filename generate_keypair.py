import sys
from time import time
from prime_number_generation import generate_large_prime

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    Return x, y, d where ax + by = d = gcd(a, b)
    Assuming a > b
    """
    if b == 0:
        return 1, 0, a

    x1, y1, d = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return x, y, d


def generate_key_pairs(n_bits) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Randomly creates a p and q (two large n-bit primes)
    Computes N = p*q
    Computes e and d such that e*d = 1 mod (p-1)(q-1)
    Return N, e, and d
    """
    p = generate_large_prime(n_bits)
    q = generate_large_prime(n_bits)
    
    while p == q:
        q = generate_large_prime(n_bits)
    
    N = p * q
    phi_N = (p - 1) * (q - 1)

    e = None
    for candidate_e in primes:
        _, _, gcd_result = extended_euclid(phi_N, candidate_e)
        if gcd_result == 1: 
            e = candidate_e
            break
    
    if e is None:
        raise Exception("Could not find suitable e")
    
    x, y, _ = extended_euclid(phi_N, e)
    d = y % phi_N 
    if d < 0:
        d += phi_N
    
    return N, e, d


def main(n_bits: int, filename_stem: str):
    start = time()
    N, e, d = generate_key_pairs(n_bits)
    print(f'{time() - start} seconds elapsed')

    public_file = filename_stem + '.public.txt'
    with open(public_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(e)
        ])
    print(public_file, 'written')

    private_file = filename_stem + '.private.txt'
    with open(private_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(d)
        ])
    print(private_file, 'written')


if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
