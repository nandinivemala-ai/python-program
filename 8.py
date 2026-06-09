import secrets

random_number = secrets.randbelow(10) + 1
print(f"Cryptographically secure random number: {random_number}")
