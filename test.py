




    

import sys
import math

class node(object):
  def __init__(self,input, heuristic, city,g = 0,f = 0,d =0,parent = None):
    self.city = city
    self.g = g
    self.f = f
    self.d = d
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

# def catculateCost(g =0, h = 0):
#   pass


# def getNeighbours(graph, city):
#   pass

# def reconstructPath(camefrom, current):
#   totalPath = []
#   while current in camefrom.keys():
#     current = camefrom[current]
#     totalPath.append(current)
#   return totalPath  

# def distBetween(current, neighbor):
#   return 0

# def heuristicCostEstimate(heuristicData, city):
#   return heuristicData[city]

# def cityWithLowestFvalue(openedSet):
#   lowCostNeighbour = ""
#   cost = 0
#   for city in openedSet:
#     cost =  12
#   return lowCostNeighbour

def performSearch(model, start, goal):
#   closedSet = openedSet = set()
#   openedSet.add(start)

#   cameFrom = {}

#   g_score = {}
#   f_score = {}

#   f_score[start] = heuristicCostEstimate(model.heuristicData, start)

#   while openedSet is not None:
#     current = cityWithLowestFvalue(openedSet)
#     if current == goal:
#       return reconstructPath(cameFrom, current)
#     openedSet.remove(current)
#     closedSet.add(current)

#     for neighbor in getNeighbours(model.inputData, current):
#       if neighbor in closedSet:
#         continue

#       tentativeGScore = g_score[current] + distBetween(current, neighbor)    

#       if neighbor not in openedSet:
#         openedSet.add(neighbor)
#       elif tentativeGScore >= g_score[neighbor]:
#         continue

#       cameFrom[neighbor] = current
#       g_score[neighbor] = tentativeGScore
#       f_score[neighbor] = g_score[neighbor] + heuristicCostEstimate(neighbor, goal)

  print(model)

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name and the other arguments.
  fName = sys.argv[1]
  origin_city = sys.argv[2].lower()
  destination_city = sys.argv[3].lower()
  hName = sys.argv[4]

  model = FindRoute( fName, origin_city, destination_city, hName )
  performSearch(model,origin_city, destination_city)
  # print("Origin City")
  # for tup in model.inputData:
  #   print('From %s \n'%(tup))
  #   for des in model.inputData[tup]:
  #     print("%s is at %d kilometre"%(des[0], des[1]))
  # print("\n\n")

  # print("The heuristic destance to kassel from different cities")
  # for city in model.heuristicData:
  #   print("%s at %d"%(city, model.heuristicData[city]))
  print("hello")

if __name__ == '__main__' :
  _main()