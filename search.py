# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack

    fringe = Stack()
    direction_to_goal = Stack()
    position_visited = []
    current_position = problem.getStartState()
    final_directions = []
    while problem.isGoalState(current_position) == False:
        if current_position not in position_visited:
            position_visited.append(current_position) 
            for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position): 
                fringe.push(temporary_position)
                direction_to_goal.push(final_directions + [temporary_direction])
        current_position = fringe.pop()
        final_directions = direction_to_goal.pop()
    return final_directions

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    
    fringe = Queue()
    direction_to_goal = Queue()
    position_visited = []
    current_position = problem.getStartState()
    final_directions = []
    while problem.isGoalState(current_position) == False:
        if current_position not in position_visited:
            position_visited.append(current_position) 
            for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position): 
                fringe.push(temporary_position)
                direction_to_goal.push(final_directions + [temporary_direction])
        current_position = fringe.pop()
        final_directions = direction_to_goal.pop()
    return final_directions


def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    
    fringe = PriorityQueue()
    direction_to_goal = PriorityQueue()
    position_visited = []
    current_position = problem.getStartState()
    final_directions = [] 
    while problem.isGoalState(current_position) == False:
        if current_position not in position_visited:
            position_visited.append(current_position) 
            for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position): 
                totalcost = heuristic(temporary_position, problem, "goal")
                fringe.push(temporary_position, totalcost)
                direction_to_goal.push(final_directions + [temporary_direction], totalcost)
        current_position = fringe.pop()
        final_directions = direction_to_goal.pop()
    return final_directions

def biDirectionalSearchMM0(problem):

    from game import Directions
    from util import Queue
    
    fringe_1 = Queue()
    fringe_2 = Queue()
    direction_to_goal_1 = Queue()
    direction_to_goal_2 = Queue()
    position_visited_1 = {}
    positions_1 = []
    position_visited_2 = {}
    positions_2 = []
    current_position_1 = problem.getStartState()
    current_position_2 = problem.goal
    final_directions_1 = []
    final_directions_2 = []
    while True:
#         print(position_visited_1.keys(),len(position_visited_1.keys()))
#         print("-------------------------")
#         print(position_visited_2.keys(),len(position_visited_2.keys()))
#         print("==========================")
        if current_position_1 not in position_visited_2: 
            if current_position_1 not in positions_1:
                positions_1.append(current_position_1)
                for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position_1): 
                    position_visited_1[temporary_position] = final_directions_1 + [temporary_direction]
                    fringe_1.push(temporary_position)
                    direction_to_goal_1.push(final_directions_1 + [temporary_direction])
            current_position_1 = fringe_1.pop()
            final_directions_1 = direction_to_goal_1.pop()
        else:
#             print(position_visited_1[current_position_1] + [Directions.REVERSE[x] for x in position_visited_2[current_position_1]][::-1])
            return position_visited_1[current_position_1] + [Directions.REVERSE[x] for x in position_visited_2[current_position_1]][::-1]
        if current_position_2 not in position_visited_1:
            if current_position_2 not in positions_2:
                positions_2.append(current_position_2)
                for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position_2):
                    position_visited_2[temporary_position] = final_directions_2 + [temporary_direction]
                    fringe_2.push(temporary_position)
                    direction_to_goal_2.push(final_directions_2 + [temporary_direction])
            current_position_2 = fringe_2.pop()
            final_directions_2 = direction_to_goal_2.pop()
        else:
#             print(position_visited_1[current_position_2] + [Directions.REVERSE[x] for x in position_visited_2[current_position_2]][::-1])
            return position_visited_1[current_position_2] + [Directions.REVERSE[x] for x in position_visited_2[current_position_2]][::-1]


def biDirectionalSearchMM(problem, heuristic):

    from game import Directions
    from util import PriorityQueue
    
    fringe_1 = PriorityQueue()
    fringe_2 = PriorityQueue()
    direction_to_goal_1 = PriorityQueue()
    direction_to_goal_2 = PriorityQueue()
    position_visited_1 = {}
    positions_1 = []
    position_visited_2 = {}
    positions_2 = []
    current_position_1 = problem.getStartState()
    current_position_2 = problem.goal
    final_directions_1 = []
    final_directions_2 = []
    

    while True:
        if current_position_1 not in position_visited_2: 
            if current_position_1 not in positions_1:
                positions_1.append(current_position_1)
                for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position_1):
                    totalcost = heuristic(temporary_position, problem, "goal")
                    position_visited_1[temporary_position] = final_directions_1 + [temporary_direction]
                    fringe_1.push(temporary_position, totalcost)
                    direction_to_goal_1.push(final_directions_1 + [temporary_direction], totalcost)
            current_position_1 = fringe_1.pop()
            final_directions_1 = direction_to_goal_1.pop()
        else:
            return position_visited_1[current_position_1] + [Directions.REVERSE[x] for x in position_visited_2[current_position_1]][::-1]
        if current_position_2 not in position_visited_1:
            if current_position_2 not in positions_2:
                positions_2.append(current_position_2)
                for temporary_position, temporary_direction, temporary_cost in problem.getSuccessors(current_position_2):
                    totalcost = heuristic(temporary_position, problem, "start")
                    position_visited_2[temporary_position] = final_directions_2 + [temporary_direction]
                    fringe_2.push(temporary_position, totalcost)
                    direction_to_goal_2.push(final_directions_2 + [temporary_direction], totalcost)
            current_position_2 = fringe_2.pop()
            final_directions_2 = direction_to_goal_2.pop()
        else:
            return position_visited_1[current_position_2] + [Directions.REVERSE[x] for x in position_visited_2[current_position_2]][::-1]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bd0 = biDirectionalSearchMM0
bd = biDirectionalSearchMM
