
class NotVisited (Exception) : pass

class NoVotes (Exception) : pass

#Ireland:Dublin:The Spire, TUS Athlone, Cliffs of Moher:4244:899:True:True:1:22:0
#France:Paris:The Eiffel Tower, The Louvre:528:255435:False:True:0:0:0
#Lithuania:Vilnus:The Military, Mylkolos, Veonirana, Palanga Beach:3362:344:True:False:1:6:900
#Россия:Москва:Санкт-Петербург, Девятая часовня, Федор Сам:996854:4346676:False:False:0:0:0
#Uzbekistan:Tashkent:Samarkand, Bukhara, Khiva, Fergana Valley:0:0:True:False:567:54654:0

class Country:

    def __init__(self, name, capital, POI, encourage, discourage, visited, transportable, timesVisited, totalDays, calcCost):
        self.__name = name
        self.__capital = capital
        self.__POI = POI
        self.__transportable = transportable
        self.__visited = visited
        self.__encourage = int(encourage)
        self.__discourage = int(discourage)
        self.__timesVisited = timesVisited
        self.__totalDays = totalDays
        self.__calcCost = calcCost
        self.__cost = 150

    def getCalcCost(self):
        return self.__calcCost

    def getPOI(self):
        return self.__POI

    def getName(self):
        return self.__name

    def getCapital(self):
        return self.__capital

    def getDiscourage(self):
        return str(self.__discourage)

    def getTotalDays(self):
        return self.__totalDays

    def getEncourage(self):
        return str(self.__encourage)

    def getTransportable(self):
        return self.__transportable

    def getTimesVisited(self):
        return self.__timesVisited

    def getVisited(self):
        return self.__visited

    def getRating(self):
        votes = (self.__encourage + self.__discourage)
        if votes == 0:
            raise NoVotes
        else:
            return int(100 * (self.__encourage / votes))

    def calcCost(self,visited):
        if not visited:
            raise NotVisited
        self.__calcCost = self.__totalDays * self.__cost

    def addTimesVisited(self, visited):
        if not visited:
            raise NotVisited
        else:
            self.__timesVisited += 1

    def addDaySpent(self, visited):
        if not visited:
            raise NotVisited
        else:
            self.__totalDays += 1

    def resetRatings(self):
        self.__discourage = 0
        self.__encourage = 0

    def markEncourage(self, num):
        self.__encourage += num

    def markDiscourage(self,num):
        self.__discourage += num

    def setName(self, name):
        self.__name = name

    def setCapital(self, cap):
        self.__capital = cap

    def setPOI(self, POI):
        self.__POI = POI