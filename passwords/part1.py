import hashlib, time

t1 = time.time()
words = [line.strip().lower() for line in open('words.txt')]
users = [line for line in open('passwords1.txt')]
t2 = time.time()
hashes = {}
for word in words:
    h = hashlib.sha256(word.encode('utf-8')).hexdigest()
    hashes[h] = word
t3 = time.time()


cracked = []

for line in users:
    h = line[line.find(':') + 1: line.find('::')]
    name = line[:line.find(':')]
    if h in hashes:
        cracked.append((name, hashes[h]))
t4 = time.time()

with open("part1Passwords.txt", 'w') as f:
    for line in cracked:
        f.write(line[0] + ':' + line[1] + '\n')
t5 = time.time()

print(f"Loading files: {(t2 - t1) * 1000} ms")
print(f"Precomputing hashes: {(t3 - t2) * 1000} ms")
print(f"Comparing hashes to users: {(t4 - t3) * 1000} ms")
print(f"Writing results: {(t5 - t4) * 1000} ms")
