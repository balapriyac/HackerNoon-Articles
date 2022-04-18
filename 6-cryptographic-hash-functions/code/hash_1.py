import hashlib
 
message = "I'm coding"
 
hash_obj = hashlib.sha256(message.encode())
 
hash_val = hash_obj.hexdigest()
 
print(hash_val)

# output: 860f5cae6febaa6b9064a16d78553819de43cb1e4c5a87ab267bb1c35fb41a04

print(len(hash_val)) 

# output: 64
# correct! 64 hexadecimal digits; total length = 64 * 4 = 256 bits