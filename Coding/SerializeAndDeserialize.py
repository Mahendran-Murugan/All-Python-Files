from pickle import load, dump


a = {1: 2, 2: 3, 3: 4}

# Serialization is done using dump()
with open('pickle.bin', 'wb') as f:
    dump(a, f)
    f.close()

# Deserialization is done using load()
with open('pickle.bin', 'rb') as f:
    res = load(f)
    f.close()

print(res)