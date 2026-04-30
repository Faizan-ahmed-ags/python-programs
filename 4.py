n_terms = 5
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(n1, end=" ")
    nth = n1 + n2
    # Update values
    n1 = n2
    n2 = nth
    count += 1