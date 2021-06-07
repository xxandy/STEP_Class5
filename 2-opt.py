import math

def readInputFile(filename):
  cities = []
  with open(filename) as f:
    next(f)
    for data in f.read().splitlines():
      coordinate = data.split(',')
      # print(coordinate)
      cities.append(list(map(float, coordinate)))
  return cities

def WriteOutputFile(filename, visitation_order):
  with open(filename, 'w') as f:
    f.write("index\n")
    for v in visitation_order:
      f.write(v + "\n")
  return

def distance(city1, city2):
  return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def all_distance(cities):
  n = len(cities)
  dist = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(i, n):
      dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
  return dist

def solve(cities):
  n = len(cities)
  dist = all_distance(cities)
  res = 0
  city_now = 0
  unvisited_cities = set(range(1, n))
  while len(unvisited_cities) > 0:
    min_dist = 10 ** 10
    city_next = 0
    for unvisited_city in unvisited_cities:
      min_dist = min(min_dist, dist[city_now][unvisited_city])
      city_next = unvisited_city
    unvisited_cities.remove(city_next)
    res += min_dist
  res += dist[city_next][0]
  return(res)

  
def main():
  cities = readInputFile("input_6.csv")
  print(solve(cities))

if __name__ == '__main__':
  main()


