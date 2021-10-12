#%% Importing useful stuff

from selenium import webdriver
from bs4 import BeautifulSoup
from ABPruning import Node
import shogi_engine
import pickle

#%% Setting up selenium

driver = webdriver.Firefox()
url = 'https://www.crazy-sensei.com/book/shogi'

#%% Creating the tree

Node_list = []

def scraping(move = '', prevMoves = [], startingPlayer = True, depth = 0):
    
    #Setting up useful variable
    move_list = []
    appendix = '/' + ','.join(prevMoves) + ',' + move
    #Gathering data from the corresponding web page
    if move != '':
        appendix = '/' + ','.join(prevMoves) + ',' + move
        if prevMoves == []:
                appendix = '/' + move
        driver.get(url + appendix)
    else: 
        driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    
    negamax = soup.findAll('p')[1].text[9:] #seems complicated but just formating
    
    if depth < 6:#float(negamax) > -0.04 and startingPlayer) or not startingPlayer):
    
        for a in soup.findAll('th'):
            move_list.append(a.text)
        move_list = move_list[3:]
        
        
        #Building node
        branch = Node(shogi_engine.Game_state())
        branch.sons = move_list
        branch.value = negamax
        branch.prior = move
        branch.depth = depth
        #i'll add branch.parent eventually
        
        Node_list.append(branch)
        
        for i in move_list:
            if move != '':
                scraping(i,prevMoves + [move],not startingPlayer,depth + 1)
            else:
                scraping(i,prevMoves,not startingPlayer, depth + 1)
            
scraping()

#%% ALL OF THIS WAS ALREADY DONE, IT IS A LONG PROCESS SO IT IS USELESS TO DO IT AGAIN
#If you want to see the result, just execute this part

Node_list = pickle.load(open('Node_list.dat','rb'))

