def readInputFile(filename):
  x, y = [], []
  with open(filename) as f:
    next(f)
    for data in f.read().splitlines():
      coordinate = data.split('\t')
      x.append(data[0])
      y.append(data[1])
  return x, y

def WriteOutputFile(filename, visitation):
  with open(filename, 'w') as f:
    f.write("index\n")
    for v in visitation:
      f.write(v + "\n")

def main():
  x, y = readInputFile("input_0.csv")
  

if __name__ == '__main__':
  main()


