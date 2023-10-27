import hashlib
words = [line.strip().lower() for line in open('words.txt')]
passwords2 = [line for line in open('passwords2.txt')]
passwords = {}
for password in passwords2:
    i = password.find(':')
    passwords[password[i+1:password.find('::')]] = password[:i]
cracked = []
i = 0
with open("index.txt", 'r') as f:
    i = int(f.readline())
l = len(words)
try:
    while i < l:
        w1 = words[i]
        for word in words:
            h = hashlib.sha256((w1 + word).encode('utf-8')).hexdigest()
            if h in passwords:
                cracked.append((passwords[h], w1 + word))
                with open("part2Passwords.txt", 'a') as f:
                    f.write(f"{passwords[h]}: {w1 + word}\n")
                with open("index.txt", 'w') as f:
                    f.write(str(i))
                print(passwords[h], w1 + word)
        i += 1
        print(i)


except KeyboardInterrupt:
    with open("index.txt", 'w') as f:
        f.write(str(i))
    print(i)
    print(cracked)

