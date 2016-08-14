import hashlib

m = hashlib.md5()
m.update('poultry outwits ants')
print(m.hexdigest())
if m.hexdigest() == "8b35bbd7ff2f5dd7c94fffbb1a3512bc":
    print("yay")