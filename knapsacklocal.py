from __future__ import print_function

import time
import random
from simpleai.search.viewers import BaseViewer

from simpleai.search.models import SearchProblem

from simpleai.search.local import hill_climbing,hill_climbing_random_restarts,genetic


class KnapsackProblem(SearchProblem):
    def __init__(self,weightOfEach:list,valueOfEach:list,numberOfItems=5,capacity=50):
            # user: number of items, knapsack capacity, weights of each item, and values of each item.
            self.numOfItems = numberOfItems
            self.capacity = capacity
            self.space_comlexity = 0
            super(KnapsackProblem, self).__init__( initial_state = list((0 for _ in range(self.numOfItems))))
            self.weightOfEach = dict()
            self.valueOfEach = dict()
            for i in range(self.numOfItems):
                self.weightOfEach[i] = weightOfEach[i]
                self.valueOfEach[i] = valueOfEach[i]
                
            print(self.weightOfEach,"weightofeach")
            print(self.valueOfEach,"valueofeach")
            
       
    def actions(self, s):
        self._actions = list()
        for i in self.weightOfEach.keys():
            self._actions.append(f'change item {i}')
        b = self.weightOfEach.keys()
        return [(a) for a in self._actions if self._is_valid(self.result(s, a))]

    def result(self, state, action):
        next_state = list(state)
        next_state[int(action[-1])] = 1 if next_state[int(action[-1])] == 0 else 0

        return list(next_state)

    def _is_valid(self, state):

        weight = 0

        for i in range(len(state)):
            if state[i] == 1:
                weight += self.weightOfEach[i]
        
        
        return weight <= self.capacity

    def value(self, state):
        value = 0
        for i in range(len(state)):
            if state[i] == 1:
                value += self.valueOfEach[i]
            
            
        return value


    
    def generate_random_state(self):
        randomState  = [random.randint(0, 1) for _ in range(self.numOfItems)]
        return randomState if self._is_valid(randomState) else self.generate_random_state()
    
    def crossover(self, state1, state2):
        cut_point = random.randint(0, len(state1))
        child = state1[:cut_point] + state2[cut_point:]
        return child  if self._is_valid(child) else self.crossover(state1, state2)
        
    def mutate(self, state):
        state[random.randint(0, len(state) - 1)] = 1 if state[random.randint(0, len(state) - 1)] == 0 else 0
        return state if self._is_valid(state) else self.mutate(state)

def test_class(algorithm,problem,viewer,restart_limit=1000):
    print("-----------------------------------------------------------------------------------------")

    print("Testing",algorithm.__name__," algorithm")
    start_time = time.time()
    print(algorithm.__name__,"testt")
    algname= str(algorithm.__name__)
    if algname == "hill_climbing_random_restarts":
        result = algorithm(problem,viewer=viewer,restarts_limit=restart_limit)
    else :
        result = algorithm(problem,viewer=viewer)

    end_time = time.time()

    weight=0
    val = 0 
    count=0

    for i in result.state:
        count+=1
        if i==1:
            weight += myp.weightOfEach[count-1]


    count=0
    for i in result.state:
        count+=1
        if i==1:
            val += myp.valueOfEach[count-1]

    print("Time: ",end_time-start_time)
    
    print("Result: ",result.state)
    print("Weight: ",weight)
    print("Value: ",val)

    print("-----------------------------------------------------------------------------------------")

if __name__ == "__main__":
    
    # ! Uncomment the following lines to get input from user
    
    # numOfItems = int(input("Enter number of items: "))
    # capacity = int(input("Enter knapsack capacity: "))
    # weightOfEach = list()
    # valueOfEach = list()
    # for i in range(numOfItems):
    #     weightOfEach.append(int(input("Enter weight of item "+str(i+1)+": ")))
    # for i in range(numOfItems):
    #     valueOfEach.append(int(input("Enter value of item "+str(i+1)+": ")))

    # ******* I ASSIGNED THESE VALUES FOR TESTING *******
    numOfItems = 15
    capacity = 50
    weightOfEach = [24,10,10,7,2,8,6,5,9,12,20,18,13,5,4]
    valueOfEach = [50,10,25,30,20,25,40,15,12,22,35,45,55,100,60]
    myp = KnapsackProblem(weightOfEach,valueOfEach,numOfItems,capacity)
    myviewer = BaseViewer()
    test_class(hill_climbing,myp,myviewer)
    test_class(hill_climbing_random_restarts,myp,myviewer)
    test_class(genetic,myp,myviewer)
    
    

