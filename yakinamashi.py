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

def loop_distance(dist, visitation_order):
  n = len(dist)
  res = 0
  for i in range(1, n):
    res += dist[visitation_order[i-1]][visitation_order[i]]
  res += dist[visitation_order[n-1]][visitation_order[0]]
  return res

def exchange_two_node(visitation_order, exchange_number, dist):
  n = len(visitation_order)
  front, back = visitation_order[exchange_number], visitation_order[(exchange_number + 1) % n]
  front_front, back_back = visitation_order[(n + exchange_number - 1) % n], visitation_order[(exchange_number + 2) % n]
  dist_front = dist[front_front][front]
  dist_back = dist[back][back_back]
  dist_front_new = dist[front_front][back]
  dist_back_new = dist[front][back_back]
  if dist_front + dist_back > dist_front_new + dist_back_new :
    visitation_order[exchange_number] = back
    visitation_order[(exchange_number + 1) % n] = front
  return visitation_order

def solve(cities):
  n = len(cities)
  dist = all_distance(cities)
  visitation_order = list(range(n))
  random.shuffle(visitation_order)
  # print(visitation_order)
  for i in range(10000):
    for j in range(n):
      exchange_two_node(visitation_order, j, dist)
  res = loop_distance(dist, visitation_order)
  return(res)

  
def main():
  cities = readInputFile("input_3.csv")
  print(solve(cities))

if __name__ == '__main__':
  main()


