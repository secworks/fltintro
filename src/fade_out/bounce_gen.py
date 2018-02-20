import math
num_elements = 256
max_val = 0x110
fraction = (math.pi / 2) / num_elements

for i in range(num_elements):
    indata = i * fraction
    sinval = math.sin(indata)
    posval = int(max_val * sinval)
#    print(indata, posval, int(posval / 255), (posval % 255))
    print("$%x $%02x" % (int(posval / 255), (posval % 255)))
print("")
