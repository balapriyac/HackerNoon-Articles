import hashlib

strings = ["hello","sha256","sensitive info"]

for string in strings:
    hash_obj = hashlib.sha256(string.encode())
    hash_val = hash_obj.hexdigest()
    print(f"Hash #{strings.index(string)+1}: {hash_val}")

# Output
Hash #1: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Hash #2: 5d5b09f6dcb2d53a5fffc60c4ac0d55fabdf556069d6631545f42aa6e3500f2e
Hash #3: 034fcc03d9332ee032b5815ef69b0f21926dd2da73f0fcfd65ff90ded1700892