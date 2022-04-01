# Trovare l'elemento con più ricorrenze
test = [1, 2, 3, 4, 2, 2, 3, 1, 1, 1, 4]
print(max(set(test), key=test.count))
