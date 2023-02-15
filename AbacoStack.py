# MARVIN UWALAKA 
import time   # Import time and random modules
import random

class Card:
    def __init__(self,no_colours,depth): 
        '''Takes in number of colours and depth and initiallizes card class'''
        self.__beads = []
        self.no_colours = no_colours 
        self.depth = depth 
        
    def fillbeads(self):
        '''fillbeads fills self.__beads with required colours and number of colours'''
        alpa_counter = 0
        for i in range(self.no_colours):
            for i in range(self.depth):
                self.__beads.append(chr(65 + alpa_counter))
            alpa_counter += 1
            
    def reset(self):
        '''reset shuffles the order of the items in self.__beads and creates a new card configuration'''
        random.shuffle(self.__beads)
       
    def show(self):
        '''displays configured card'''
        self.bead_Matrix = [self.__beads[i:i+self.depth] for i in range(0,len(self.__beads),self.depth)]
        for i in range(len(self.bead_Matrix)):
            print('| ', end = '')
            for x in self.bead_Matrix:
                print(x[i], end =' ')
            print('|')
       
    def stack(self,number):
        '''takes in number and returns the stack of that number index'''
        '''input: number of type int '''
        '''output: self.__beads[left:right] of type list'''
        assert type(number) == int, 'enter an integer'
        assert 0 <= number <= self.no_colours, 'stack does not exist'
       
        left = ((number+1)*self.depth)- self.depth 
        right = ((number+1)*self.depth)
        return self.__beads[left:right]
   
    def __str__(self):
        '''str returns a str illustration of the configured card'''
        '''returns str_ of type str'''
        str_ = ''
        counter1 = 0 
        counter2 = self.depth        
        for b in range(self.depth):
            temp = '|'
            temp += ''.join(self.__beads[counter1:counter2]) +'|'
            str_ += temp
            counter1 += self.depth
            counter2 += self.depth            
        return str_
    
    def replace(self,filename,n):
        '''Reads line n in a file and makes it self.__beads'''
        '''input: filename type(str)
                  n of type int'''
                  
        assert type(n) == int, 'enter an integer'
        assert n > 0, 'index our of range'
        file = open(filename, "r")
        config = file.readlines()
        config = config[n].strip('\n')
        char = ''
        length = 0
        for i in config:
            length +=  1 
            if i not in char:
                char+= i
        self.__beads = list(config)
        self.no_colours = len(char)
        self.depth = length//self.no_colours
            
class Bstack:
    '''Bounded stack implementated using position 0 as the end and is full method to check is the bounded satck is full'''
    
    def __init__(self,capacity):
        self.capacity = capacity 
        self.items = []
    
    def push(self, item):
        if self.isFull():
            raise Exception('Bstack is Full')
        self.items.insert(0,item)
    
    def pop(self):       
        if self.isEmpty():
            raise Exception('Bstack is empty')
        else:
            return self.items.pop(0)  
    
    def peek(self):      
        if self.isEmpty():
            raise Exception('Bstack is empty')
        else:
            return self.items[0] 
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        return ' '.join(self.items)
    def clear(self):
        self.items.clear()
           
    def isFull(self):
        return self.size() == self.capacity 
        
class AbacoStack:
    def __init__(self,no_stacks,stack_depth):
        '''initialize Abzo stack class'''
        '''inputs: no_stacks(int)
                   stack_depth(int)'''
        self.no_stacks = no_stacks
        self.stack_depth = stack_depth
        self.moves = 0 
        self.top_list = ['.'] * (self.no_stacks + 2) 
        self.stacks= ['place_holder'] * no_stacks
         
         
        # make stacks 
        for i in range(self.no_stacks):
            self.stacks[i] = Bstack(self.stack_depth)
            for j in range(self.stack_depth):
                self.stacks[i].push(chr(65 + i))
                
    def moveBead(self,move):
        '''moves the colours in a stack based on the value of move'''
        '''move(str)'''
        # chack if the stack object being moved exists
        try :
            if int(move[:1]) not in range(self.no_stacks+2) and int(move[1:]) not in 'ulrd':  
                raise AssertionError('Error: invalid move')
        except ValueError:
                raise AssertionError('Error: invalid move')
       
        # chacks if length of move is more than 2 
        if len(move) > 2:
            raise AssertionError('Error: invalid move')
        
        # checks if the item being moved up or down is in the position 0 or the last position 
        if move[:1] == '0' or move[:1] == str(self.no_stacks+1):
            if move[1:] in 'ud':
                raise AssertionError('Error: invalid move')
            
        if move[1:] =='u':
            z = self.top_list[int(move[:1])]
            # checks if is a colour above the stack that up is called on 
            if self.top_list[int(move[:1])] != '.':
                c = self.top_list[int(move[:1])]
                raise AssertionError('Error: invalid move')
            counter = 1
            b = ' '
            while self.stacks[int(move[:1])-1].isEmpty() or self.stacks[int(move[:1])-1].peek() == '.':
                b = self.stacks[int(move[:1])-1].pop()
                counter +=1 
            self.top_list[int(move[:1])] = self.stacks[int(move[:1])-1].pop()
            
            for i in range(counter):
                self.stacks[int(move[:1])-1].push('.')
            self.moves += 1
          
        elif move[1:] == 'd':
            # checks if the stack that down is called on is full
            list_empty = False 
            if self.stacks[int(move[:1])-1].peek() != '.':
                raise AssertionError('Error: invalid move')
            counter = -1 
            b = ''
            while not self.stacks[int(move[:1])-1].isEmpty() and self.stacks[int(move[:1])-1].peek() == '.' and not list_empty :
                
                # if the loop is empty and an item is poped from it catch the exception and break the loop
                try:
                    b = self.stacks[int(move[:1])-1].pop()
                except:   
                    list_empty= True 
                    counter -=1 
                counter += 1
                
            self.stacks[int(move[:1])-1].push(self.top_list[int(move[:1])])
            self.top_list[int(move[:1])] = b 
            for i in range(counter):
                self.stacks[int(move[:1])-1].push(b)
            self.moves += 1
                
        elif move[1:] in 'rl':
            if move[1:] == 'l':
                moveIndex = -1 
            else:
                moveIndex = 1
            # check if the top list index being moved into is occupied 
            if move[:1] == str(self.no_stacks+1) and  move[1:] == 'r':
                raise AssertionError('Error: invalid move')                 
            if move[:1] == '0' and move[1:] == 'l':
                raise AssertionError('Error: invalid move')
            if self.top_list[int(move[:1]) + moveIndex] != '.':
                raise AssertionError('Error: invalid move')            
                     
            # switch the variables 
            temp =  self.top_list[int(move[:1]) + moveIndex]
            self.top_list[int(move[:1]) + moveIndex] = self.top_list[int(move[:1])]
            self.top_list[int(move[:1])] = temp 
            self.moves += 1
        
        
    def reset(self):
        '''resets the Abacostack game by making moves 0 and making new stacks'''
        self.set_moves(0)
        self.top_list = ['.'] * (self.no_stacks + 2) 
        for i in range(self.no_stacks):
            self.stacks[i] = Bstack(self.stack_depth)
            for j in range(self.stack_depth):
                self.stacks[i].push(chr(65 + i))        
        
    def set_moves(self,x):
        self.moves = x
    
    def show(self,card=None):
        '''takes in an optional card arguement of type Card and displays the Abocotack and acrd if the card is given but only the abaco stack if it isn't'''
        
        # make list of Abacostacks 
        Abaco_stacks = []
    
        positions = [str(i)for i in range(self.no_stacks + 2)]
        print(' '+ ' '.join(positions))
        print("{:<16}".format(' '+' '.join(self.top_list)),end = '' )
        if card != None:
            print('card')
        else:
            print()
            
        # fill abacostacks and card stacks 
        for stack in self.stacks:
            Abaco_stacks.append(stack.items)
    
        # transpose those stacks 
        tranposed_Ab_stacks = transpose(Abaco_stacks) 
    
        # check if card is given and prinst corresponding output 
    
        if card == None:
        
            for row in tranposed_Ab_stacks:
                print (' | '+' '.join(row), end = ' |\n')
            print("{:<25}".format(' +'+'-'*(2*self.no_stacks + 1)+'+'))
        else: 
            # make list of card stacks 
            card_stacks  = [] 
            for i in range(card.no_colours):
                card_stacks.append(card.stack(i))  
            transposed_card_stacks = transpose(card_stacks)
            i = 0
            for row in tranposed_Ab_stacks:
                print ("{:<15}".format(' | '+' '.join(row)+ ' |')  +  '|'+' '.join(transposed_card_stacks[i]) + '|', end = ' \n')
                i += 1
            print("{:<25}".format(' +'+'-'*(2*self.no_stacks + 1)+'+') +  str(self.moves)+ ' moves' )
            
    def isSolved(self,card):
        # takes in card of type Card and returns solved of type bool 
        solved = True 
        for i in range(self.no_stacks):
            b = card.stack(i) 
            c = self.stacks[i].items
            if  card.stack(i) != self.stacks[i].items:
                solved = False 
        return solved        
        
                    
def transpose(matrix): 
    '''takes in a matrix of type list and return a transposed version that matrix'''
    Tmatrix  = []
    for col_index in range(0,len(matrix[0])):
        new_row = []
        for row_index in range(0,len(matrix)):
            number= matrix[row_index][col_index]
            new_row.append(number) 
        Tmatrix.append(new_row)
    return Tmatrix        


def main():
    stack = AbacoStack(3,3)
    card = Card(3,3)
    card.fillbeads()
    card.reset()
    card.fillbeads()
    stack.reset()
    stack.show(card)
    print("possible moves:1u,1d,1u ,2d ,3u ,3d,0r,1r,2r ,3r,4l")
    while not stack.isSolved(card):
        move = input('move: ' )
        stack.moveBead(move)
        stack.show(card)
        print("possible moves:1u,1d,1u ,2d ,3u ,3d,0r,1r,2r ,3r,4l")
    print('you win')
  
         
if __name__ == '__main__':
    main()
    

#1u means stack 1 upward move
#1d means stack 1 downward move
#2u means stack 2 upward move
#2d means stack 2 downward move
#3u means stack 3 upward move
#3d means stack 3 downward move
#0r means position 0 right move
#1r and 1l mean position 1 right move and left move respectively
#2r and 2l mean position 2 right move and left move respectively
#3r and 3l mean position 3 right move and left move respectively
#4l means position 4 left move