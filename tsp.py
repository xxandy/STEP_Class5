def readInputFile(filename):
  cities = []
  with open(filename) as f:
    next(f)
    for data in f.read().splitlines():
      coordinate = data.split('\t')
      cities.append(data)
  return cities

def WriteOutputFile(filename, visitation_order):
  with open(filename, 'w') as f:
    f.write("index\n")
    for v in visitation_order:
      f.write(v + "\n")
  return



def main():
  cities = readInputFile("input_0.csv")
  

if __name__ == '__main__':
  main()


