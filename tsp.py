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

def dfs(S, city_now, dp, n, dist):
  if dp[S][city_now] != -1: #訪問済み
    return dp[S][city_now]
  if S == (1 << n) - 1 and city_now == 0: #全ての点を訪れた
    return 0
  res = 10 ** 10  #大きい数
  for city_next in range(n):
    if (S >> city_next & 1) == 0: #city_nextは未訪問
      res = min(res, dfs(S | 1 << city_next, city_next, dp, n, dist) + dist[city_now][city_next])
  dp[S][city_now] = res
  return dp[S][city_now]

def solve(cities):
  dist = all_distance(cities)
  n = len(cities)
  dp = [[-1] * n for _ in range(1 << n)]
  min_dist = dfs(0, 0, dp, n, dist)
  print(min_dist)
  return
  
def main():
  cities = readInputFile("input_2.csv")
  solve(cities)

if __name__ == '__main__':
  main()


