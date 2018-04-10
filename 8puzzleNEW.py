#https://stackoverflow.com/questions/11969361/sorting-a-list-containing-objects-of-a-class-in-python
#https://stackoverflow.com/questions/23026324/how-to-make-a-list-from-a-raw-input-in-python

#lists of problems
veryeasy = [1,2,3,4,5,6,7,0,8]
easy = [1,2,0,4,5,3,7,8,6]
doable = [0,1,2,4,5,3,7,8,6]
ohboy = [8,7,1,6,0,2,5,4,3]
ex = [1,2,3,4,8,0,7,6,5]

thelist = [1,2,3,4,0,8,7,6,0]
goal = [1,2,3,4,5,6,7,8,0]

#test case function, not used 
def treverse(node):
    printlist = []
    while node.getParent() != 0:
        printlist.append(node)
        node = node.getParent()
    printlist.append(node)

    return printlist   

#Function that expands the node, pretty much the logic of the program
def Expand(node, parent):
    q = []
    n = node.getList()
    if n.index(0) > 2: #means that it either on row 2,3 so move up
        temp = list(n)
        a,b = temp.index(0), temp.index(0) - 3
        temp[a] , temp[b] = temp[b], temp[a]
        d = Node(temp, parent)
        d.setG(node.getG())
        q.append(d)
    if n.index(0) < 6: #means it's either on row 1,2 so move down
        temp = list(n)
        a,b = temp.index(0), temp.index(0) + 3
        temp[a] , temp[b] = temp[b], temp[a]
        c = Node(temp, parent)
        c.setG(parent.getG())
        q.append(c)
    
    if n.index(0) % 3 != 0: #move left
        temp = list(n)
      
        a,b = temp.index(0), temp.index(0) - 1
        temp[a] , temp[b] = temp[b], temp[a]
        e = Node(temp, parent)
        e.setG(parent.getG())
        q.append(e)
    

    if (n.index(0) != 2) and (n.index(0) != 5) and (n.index(0) != 8): #move right
        temp = list(n)
     
        a,b = temp.index(0), temp.index(0) + 1
        temp[a] , temp[b] = temp[b], temp[a]
     
        f = Node(temp, parent)
        f.setG(parent.getG())
        q.append(f)
    return q

def display(thelist):
    string = ''
    for i in range(len(thelist)):
        if i == 2 or i == 5:
            string = string + str(thelist[i]) + '\n---------\n'
        else:
            if i == 8:
                string = string + str(thelist[i]) + '\n'
            else:
                string = string + str(thelist[i]) + ' | '
        
    print string 


class Node: #Node class, building blocks for this program
    
    def __init__(self,thelist, parent): #Initilize constructors
        self.thelist = thelist
        self.parent = parent
        self.g = 0        
    
    def Assign_Parent(self, ParentNode):  #Assignes Parent to node
        self.parent = ParentNode
        
    def getParent(self): #Get parent
        return self.parent
    
    def displayList(self): #displays the list in grid form
        display(self.thelist)
    
    def getList(self):   #returns the list (game)
        return self.thelist
    
    def getMisplacedWeight(self):
        count = 0
        for i in range(len(self.thelist)):
            if self.thelist[i] != goal[i]:
                count = count + 1
        return count
    
    def setG(self, parent):
        self.g = parent + 1


    def getG(self):
        return self.g

    def Distancefn(self):
        return self.g + self.getDistanceWeight() 

    def Misplacefn(self):
        return self.g + self.getMisplacedWeight() 

    def getDistanceWeight(self):
        count = 0
        val_levely = 0
        goal_levely = 0
        val_levelx = 0
        goal_levelx = 0
        for i in range(1,len(self.thelist)):
            if self.thelist.index(i) != i - 1:
                if self.thelist.index(i) < 3:
                    val_levely = 1
                elif self.thelist.index(i) < 6:
                    val_levely = 2
                elif self.thelist.index(i) >= 6:
                    val_levely = 3
                        
                if i - 1 < 3:
                    goal_levely = 1
                elif i - 1 < 6:
                    goal_levely = 2
                elif i - 1 >= 6:
                    goal_levely = 3
                
                if self.thelist.index(i) % 3 == 0:
                    val_levelx = 1
                elif self.thelist.index(i) == 1 or self.thelist.index(i) == 4 or self.thelist.index(i) == 7:
                    val_levelx = 2
                elif self.thelist.index(i) == 2 or self.thelist.index(i) == 5 or self.thelist.index(i) == 8:
                    val_levelx = 3
                        
                if (i - 1) % 3 == 0:
                    goal_levelx = 1
                elif i - 1 == 1 or i - 1 == 4 or i - 1 == 7:
                    goal_levelx = 2
                elif i - 1 == 2 or i - 1 == 5 or i - 1 == 8:
                    goal_levelx = 3
                
                
                if val_levely > goal_levely:
                    count = count + (val_levely - goal_levely)
                    if val_levelx > goal_levelx:
                        count = count + (val_levelx - goal_levelx)
                    elif val_levelx < goal_levelx:
                        count = count + (goal_levelx - val_levelx)
                elif val_levely < goal_levely:
                    count = count + (goal_levely - val_levely)
                    if val_levelx > goal_levelx:
                        count = count + (val_levelx - goal_levelx)
                    elif val_levelx < goal_levelx:
                        count = count + (goal_levelx - val_levelx)
                else:
                    if val_levelx > goal_levelx:
                        count = count + (val_levelx - goal_levelx)
                    elif val_levelx < goal_levelx:
                        count = count + (goal_levelx - val_levelx)
        return count        
            
todo = []    
print "Welcome to Dillon Sio 8-puzzle solver"

user = int(raw_input("Type '1' to use a default puzzle, or '2' to enter your own puzzle "))

if user == 1:
    todo = ohboy
elif user == 2:
    print ("Enter your puzzle, use a zero to represent the blank")
    string_input = raw_input("Enter the first row, use space or tabs between numbers ")
    input_list1 = string_input.split() #splits the input string on spaces
    # process string elements in the list and make them integers
    input_list1 = [int(a) for a in input_list1] 

    string_input = raw_input("Enter the second row, use space or tabs between numbers ")
    input_list2 = string_input.split() #splits the input string on spaces
    # process string elements in the list and make them integers
    input_list2 = [int(a) for a in input_list2] 

    string_input = raw_input("Enter the third row, use space or tabs between numbers ")
    input_list3 = string_input.split() #splits the input string on spaces
    # process string elements in the list and make them integers
    input_list3 = [int(a) for a in input_list3] 

    todo = input_list1 + input_list2 + input_list3


alg = int(raw_input("Enter your choice of algorithm\n 1. Uniformed search cost\n 2. A* with the Misplaced Tile heuristic\n 3. A* with the Manhatten distance heuristic\n"))

n = Node(todo, 0)
queue = []
GoalList = []
queue.append(n)
total_node = 0
max_node = 0
total_expand = 0
depth = 1
start = True
function = 0;
NewExpand = []
while True:
    if len(queue) == 0:
        print 'No Solution found'
        break
    if len(queue) > max_node:
        max_node = len(queue)
    check = queue[0]
    if alg == 1:
        function = 0
    elif alg == 2:
        function = check.getMisplacedWeight()
    elif alg == 3:
        function = check.getDistanceWeight()
    queue.pop(0)
    if check.getList() == goal:
        print 'Goal!\n'
        GoalList = treverse(check)
        break
    else:
        if start == True:
            print 'Expanding State '
            check.displayList()
            start = False
        else: 
            print 'The best state to expand with a g(n) = ' + str(check.getG()) + ' and h(n) = ' + str(function) + ' is...'
            check.displayList()
            print 'Expanding this node...\n'
            depth = depth + 1
        queue = queue + Expand(check,check)
        #add a sorting algorth
        if alg == 2:
            queue.sort(key=lambda x: x.Misplacefn()) #Misplaced sort
            print str(queue[0].Misplacefn())
        elif alg == 3:
            queue.sort(key=lambda x: x.Distancefn())
            print str(queue[0].Distancefn()) 
        elif alg == 1:
            queue.sort(key=lambda x: (x.getG()))
        #total_expand = total_expand + len(queue)
#print 'To solve this problem the search algorithm expanded a total of ' + str(total_expand) + ' nodes.'
print 'The maximum number of nodes in the queue at any one time was ' + str(max_node) + '.'
print 'The depth of the goal node was ' + str(check.getG()) + '.'

