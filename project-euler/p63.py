import time

start_time = time.time()
a = 300
cubes = {}

while True:
    current_cube = a**3
    sorted_cube = int(''.join(sorted(str(current_cube))[::-1]))
    try:
        cubes[sorted_cube][0] += 1
    except KeyError:
        cubes[sorted_cube] = [1, current_cube]
    if cubes[sorted_cube][0] == 5:
        print("Answer is:", cubes[sorted_cube][1])
        break
    a+=1
    
print("..which took", str(time.time() - start_time ), "seconds to compute")
