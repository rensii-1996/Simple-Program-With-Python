def fibonacci(n):
    sequence = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2, n):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:")
print(", ".join(map(str, fib_sequence)))
