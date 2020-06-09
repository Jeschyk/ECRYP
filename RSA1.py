from math import sqrt; from itertools import count, islice

import random

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))    # checking if the given number from the keyboard is a prime number (both p and q have to be)

while True:
    p=int(input('Enter prime p: '))
    if isPrime(p) == True:
        print("p=" + str(p) + " is a prime number\n") 
        break
    else: print("p=" + str(p) + " is NOT a prime number\n")        # inserting number p, till the value will be a prime number


while True:
    q=int(input('Enter prime q: '))
    if isPrime(q) == True:
        print("q=" + str(q) + " is a prime number\n") 
        break
    else: print("q=" + str(q) + " is NOT a prime number\n")        # inserting number q, till the value will be a prime number

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a                                                     # calculating greatest common divisor for given two values

def modinv(a, m):
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x                                             # modular inverse of a under modulo m, in other case it is 1 
    return 1

def coprime(a):
    while True:
        x = random.randrange(2, a)
        if gcd(a, x) == 1:
                return x                                        # selecting a random number between 2 and phi(n), which is a coprime to phi(n) this number will be the e

def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')          # dividing the message into small blocks for encryption using modular inverse 
    else: return c

def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')          # dividing encrypted message into small blocks for decryption using modular inverse
    else: return m

def encrypt_string(s):
    return ''.join(str(chr(encrypt_block(ord(x)))) for x in s)                                  #firstly messege m is returned as integer into encrypt_block by ord(), then after encryption 
                                                                                                #is returned as string by chr() and printed as joined string with "" as separator

def decrypt_string(s):
    return ''.join(str(chr(decrypt_block(ord(x)))) for x in s)                                  #the very same thing with decryption 


if __name__== "__main__":

    print("Chosen primes from the keyboard for encryption:\np=" + str(p) + ", q=" + str(q) + "\n")

    n=p*q

    print("n = p * q = " + str(n) + "\n")

    phi=(p-1)*(q-1)

    print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")

    e=(coprime(phi))

    print("random number e is " + str(e) + "\n")

    d=modinv(e,phi)

    print("\nThe public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")

    print("The private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")

    s = input("Enter a message (string) to encrypt: ")

    print("\nPlain message: " + str(s) + "\n")

    E = encrypt_string(s)

    print("Encrypted message: " + str(E) + "\n")

    D = decrypt_string(E)

    print("Decrypted message: " + str(D) + "\n")