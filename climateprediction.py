kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

w1, w2, w3 = 0.3, 0.2, 0.5
weights = [w1, w2, w3]

def crop_yield(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result

print(crop_yield(kanto, weights))
print(crop_yield(johto, weights))
print(crop_yield(hoenn, weights))
print(crop_yield(sinnoh, weights))
print(crop_yield(unova, weights))