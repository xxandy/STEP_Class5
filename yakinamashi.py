import math
import random

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
      f.write(str(v) + "\n")
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

def loop_distance(dist, visitation_order):
  n = len(dist)
  res = 0
  for i in range(1, n):
    res += dist[visitation_order[i-1]][visitation_order[i]]
  res += dist[visitation_order[n-1]][visitation_order[0]]
  return res

def initialize_visitation_order(cities):
  n = len(cities)
  dist = all_distance(cities)
  city_now = 0
  unvisited_cities = set(range(1, n))
  visitation_order = [0]
  while len(unvisited_cities) > 0:
    min_dist = 10 ** 10
    city_next = 0
    for unvisited_city in unvisited_cities:
      min_dist = min(min_dist, dist[city_now][unvisited_city])
      city_next = unvisited_city
    unvisited_cities.remove(city_next)
    visitation_order.append(city_next)
  return visitation_order

def exchange_two_node(visitation_order, i, j, dist):
  n = len(visitation_order)
  front, back = visitation_order[i], visitation_order[j]
  front_front, front_back = visitation_order[(n + i - 1) % n], visitation_order[(i + 1) % n]
  back_front, back_back = visitation_order[(n + j - 1) % n], visitation_order[(j + 1) % n]
  dist_front1 = dist[front_front][front]
  dist_front2 = dist[front][front_back]
  dist_back1 = dist[back_front][back]
  dist_back2 = dist[back][back_back]
  dist_front1_new = dist[front_front][back]
  dist_front2_new = dist[back][front_back]
  dist_back1_new = dist[back_front][front]
  dist_back2_new = dist[front][back_back]
  
  if dist_front1 + dist_front2 + dist_back1 + dist_back2 > dist_front1_new + dist_front2_new + dist_back1_new + dist_back2_new :
    visitation_order[i] = back
    visitation_order[j] = front
  return visitation_order

def solve(cities):
  n = len(cities)
  dist = all_distance(cities)
  visitation_order = initialize_visitation_order(cities)
  for i in range(10000):
    for j in range(n):
      for k in range(j+1, n):
        exchange_two_node(visitation_order, j, k, dist)
  res = loop_distance(dist, visitation_order)
  return res, visitation_order

  
def main():
  cities = readInputFile("input_3.csv")
  dist, visitation_order = solve(cities)
  print(dist)
  # WriteOutputFile("output_3.csv", visitation_order)

if __name__ == '__main__':
  main()


