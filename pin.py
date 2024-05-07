def optimized_bruteforce():
    for pin in range(13, 10000, 13):
        if pin >= 1000:
            return pin

pin = optimized_bruteforce()
print("Optimalizovaná hrubá síla:", pin)

def optimized_divide_and_conquer():
    for a in range(0, 10):
        for b in range(0, 10):
            c = 13 - (a + b) % 13
            if c < 10:
                pin = int(f"{a}{b}{c}{0}")
                if pin >= 1000:
                    return pin

pin = optimized_divide_and_conquer()
print("Optimalizované rozdělení a panování:", pin)

def optimized_heuristic():
    primes = [13, 113, 127, 139, 151, 163, 139, 211, 227, 239, 251, 263, 277, 289]
    for prime in primes:
        if prime < 1000:
            for i in range(1000, 10000, prime):
                if i % 13 == 0:
                    return i

pin = optimized_heuristic()
print("Optimalizovaný heuristický algoritmus:", pin)

