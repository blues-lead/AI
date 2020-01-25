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
import time
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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    import collections
    visited = set()
    state = problem.getStartState()
    waiting_list = util.Stack() # LIFO-stack
    #parents = collections.defaultdict(collections.UserDict)
    parents = {}
    sequence = []
    for action in problem.getSuccessors(state): # in order to push full-state values, not just (x,x)
        waiting_list.push(action)

    while not waiting_list.isEmpty():
        state = waiting_list.pop()
        visited.add(state[0]) # node is visited and not intended anymore to be visited
        for substate in problem.getSuccessors(state[0]): # take a look to successors of current node
            if substate[0] not in visited: # if not in visited
                parents[substate[0]]={'parent':state, 'cost':substate[2]} # generate new node
                waiting_list.push(substate) # push to stack
                if problem.isGoalState(substate[0]): 
                    target_state = substate
    
    start = problem.getStartState()
    print("Start state is:", start)
    while target_state[0] in parents.keys():
        temp=parents[target_state[0]]['parent']
        sequence.append(target_state[1])
        target_state = temp
    sequence.append(target_state[1])
    return sequence[::-1]
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    import collections
    waiting_list = util.Queue()
    visited = set()
    parents = {} #collections.defaultdict(collections.UserDict)
    sequence = []
    start_state = problem.getStartState()
    for action in problem.getSuccessors(start_state):
        waiting_list.push(action)
    while not waiting_list.isEmpty():
        node = waiting_list.pop()
        visited.add(node[0])
        for action in problem.getSuccessors(node[0]):
            if action[0] not in visited:
                parents[action[0]] = {'parent':node, 'cost':action[2]}
                waiting_list.push(action)
                if problem.isGoalState(action[0]):
                    target_state = action
                    

    start = problem.getStartState()
    print("Start state is:", start)
    print("Target state", target_state)
    while target_state[0] in parents.keys():
        temp=parents[target_state[0]]['parent']
        sequence.append(target_state[1])
        target_state = temp
    sequence.append(target_state[1])
    return sequence[::-1]


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from game import Directions
    from game import Actions
    visited = set()
    pStack = util.PriorityQueue()
    parents = {}
    st_state = problem.getStartState()
    visited.add(st_state)
    if problem.isGoalState(st_state):
        return
    for state in problem.getSuccessors(st_state):
        pStack.push(state,state[2])
    while not pStack.isEmpty():
        q_state = pStack.pop()
        visited.add(q_state[0])
        if problem.isGoalState(q_state[0]):
            target_state = q_state
            #print("Goal State Found!!", target_state)
            break
        for child in problem.getSuccessors(q_state[0]):
            if not child[0] in visited:
                pStack.push(child, child[2])
                parents[child[0]] = q_state
        
    sequence = []
    #test_seq = []
    while target_state[0] in parents.keys():
        #print(target_state)
        sequence.append(target_state[1])
        #test_seq.append(target_state[0]) # debug purposes
        target_state = parents[target_state[0]]
    #print(test_seq)
    #print("VecTODIR",Actions.vectorToDirection(test_seq[0]))
    sequence.append(target_state[1])
    #return sequence[::-1]
       


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    #print("Enterd heuristic definition")
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from game import Actions
    from game import Directions
    waiting_list = util.PriorityQueue()
    cost_so_far = {}
    start_state = problem.getStartState()
    cost_so_far[start_state] = 0
    waiting_list.push(start_state,0)
    parents = {}
    while not waiting_list.isEmpty():
        q_state = waiting_list.pop()
        if problem.isGoalState(q_state):
            target_state = q_state
            break
        for child in problem.getSuccessors(q_state):
            n_cost = cost_so_far[q_state] + child[2]
            if child[0] not in cost_so_far or n_cost < cost_so_far[q_state]:
                cost_so_far[child[0]] = n_cost
                prior = n_cost + heuristic(child[0], problem)
                waiting_list.push(child[0], prior)
                parents[child[0]] = q_state

    sequence = []
    prev_state = target_state
    while target_state in parents.keys():
        target_state = parents[target_state]
        direction = Actions.vectorToDirection([prev_state[0] - target_state[0], prev_state[1] - target_state[1]])
        prev_state = target_state
        sequence.append(direction)
        
    #print(sequence)
    return sequence[::-1]





# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
