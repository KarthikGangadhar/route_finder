import sys
import math

class node(object):
  def __init__(self, city,g = 0, tc = 0,f = 0,d =0,parent = None):
    self.city = city
    self.g = g
    self.f = f
    self.d = d
    self.tc = tc
    self.parent = parent

class FindRoute(object) :
  def __init__( self, inputFile = None, originCity = None, destinationCity = None, heuristicFile = None) :
    self.informedSearch = False
    self.inputData = {}
    self.heuristicData = {}
    self.start = originCity 
    self.goal = destinationCity

    if inputFile is not None :
      self.parseInputData( inputFile )
    if heuristicFile is not None :
      self.informedSearch = True
      self.parseHeuristicData( heuristicFile )

  def parseInputData( self, inputFile ) :
    try:
      fp = open(inputFile, 'r')
      lines = fp.read().replace('\r', '' ).split( '\n' )

      for line in lines:
        if line != 'END OF INPUT':
          line_arr = line.strip().split(' ')
          if line_arr[0].lower() in self.inputData:
            self.inputData[line_arr[0].lower()].append((line_arr[1].lower(), int(line_arr[2])))
          else:
            self.inputData[line_arr[0].lower()] = []
            self.inputData[line_arr[0].lower()].append((line_arr[1].lower(), int(line_arr[2])))

          if line_arr[1].lower() in self.inputData:
            self.inputData[line_arr[1].lower()].append((line_arr[0].lower(), int(line_arr[2])))
          else:
            self.inputData[line_arr[1].lower()] = []
            self.inputData[line_arr[1].lower()].append((line_arr[0].lower(), int(line_arr[2])))
    finally:
      fp.close()

  def parseHeuristicData( self, inputFile ) :
    try:
      fp = open(inputFile, 'r')
      lines = fp.read().replace('\r', '' ).split( '\n' )

      for line in lines:
        if line != 'END OF INPUT':
          line_arr = line.strip().split(' ')
          self.heuristicData[line_arr[0].lower()] = int(line_arr[1])
    finally:
      fp.close()

def getTentativeCost(cities, node):
  for city in cities:
    if city[0] == node:
      return city[1]
  return 0

def getCost(model, node, parentCost):
  cost = 0
  if model.start == node:
    return 0
  else:
    return parentCost.g + getTentativeCost(model.inputData[parentCost.city], node)
  return cost

def getFValue(model, node, parentCost = 0):
  heuristic = 0
  if node in model.heuristicData:
    heuristic = model.heuristicData[node]

  if model.start == node and ():
    return (0, heuristic)
  else:
    cost = getCost(model, node, parentCost)
    return  (cost, cost + heuristic)
  
def getNeighbor(model, node):
  return model.inputData[node.city]
  
def generateNodes(model, neighbours, parent):
  Nodes = {}
  for nbour in neighbours:
    cost, fvalue = getFValue(model, nbour[0], parent)
    Nodes[nbour[0]] = node(nbour[0],cost,nbour[1], fvalue,0,parent)  
  return  Nodes

def performSearch(model, start, goal):
  fringe = {}
  openset = set()
  closed = set()
  fvalue = getFValue(model, start)
  expanded = 0
  fringe[start] = node(start,0,0, fvalue[1], 0,parent = None)
  openset.add(fringe[start])
  current = start

  while openset:
    current = min(openset, key=lambda o:o.f)
    # print('Expanding Node %d'%(expanded))
    # print('Generating successors to %s'%(current.city))
    neighbours = getNeighbor(model, current)
    neighboursNodes = generateNodes(model, neighbours, current)

    if current.city == goal:
      path = []
      while current.parent:
        path.append(current)
        current = current.parent
      path.append(current)
      return (path[::-1],expanded)

    openset.remove(current)
    closed.add(current)

    for nodes in neighboursNodes:
      if neighboursNodes[nodes] in closed:
        continue

      if nodes not in [cities.city for cities in closed]:
        if neighboursNodes[nodes] not in openset and nodes != model.start:
          openset.add(neighboursNodes[nodes])
    expanded +=1

  return ([],expanded)  

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name and the other arguments.
  fName = sys.argv[1]
  origin_city = sys.argv[2].lower()
  destination_city = sys.argv[3].lower()
  if len(sys.argv) > 4:
    hName = sys.argv[4]
  else:
    hName = None

  model = FindRoute( fName, origin_city, destination_city, hName )
  path,expanded = performSearch(model,origin_city, destination_city)
  
  paths = [p.city for p in path]
  print(" --> ".join(paths))
  distance = sum(map(lambda x: x.tc, path))
  print("nodes expanded: %d"%(expanded))
  print("")
  if distance:
    print("distance: %d km"%(distance))
    for i in range(len(path) -1):
      print("%s to %s, %d km"%(path[i].city, path[i+1].city, path[i+1].tc))
  else:
    print("distance: infinity")
    print("route: none")


if __name__ == '__main__' :
  _main()
