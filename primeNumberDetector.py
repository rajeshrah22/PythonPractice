def is_prime(num):
    prime = True
    for i in range(num-2):
        if num % (i+2) == 0:
            prime = False
    return prime

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
