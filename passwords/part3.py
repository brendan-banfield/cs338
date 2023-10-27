import hashlib, time

t1 = time.time()
words = [line.strip().lower() for line in open('words.txt')]
users = [line for line in open('passwords3.txt')]
t2 = time.time()


cracked = []

for line in users:
    i = line.find('$') + 3
    salt = line[i:i+8]
    h = line[i+9:line.find('::')]
    name = line[:i-4]
    for word in words:
        salted = hashlib.sha256((salt + word).encode('utf-8')).hexdigest()
        if salted == h:
            #print(name, word)
            cracked.append((name, word))
    
t3 = time.time()

with open('part3Passwords.txt', 'w') as f:
    for password in cracked:
        f.write(f"{password[0]}:{password[1]}\n")
t4 = time.time()

print(f"Loading files: {(t2 - t1) * 1000} ms")
print(f"Brute forcing passwords: {t3 - t2} seconds")
print(f"Average time per user: {(t3-t2) / len(users) * 1000} ms")
print(f"Writing output: {(t4-t3) * 1000} ms")
print(cracked)

