# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
import datetime

NO_OF_RECENT_SCORES = 3
ace_high = True

def CheckUpdate():
  complete = False
  while not complete:
    choice = input("Do you want to add your score to the high score table? (y or n): ")
    choice = choice.lower()
    if choice == "no":
      choice = "n"
    elif choice == "yes":
      choice = "y"
    if choice == "n" or choice == "y":
      complete = True
  return choice

def SaveScores(RecentScores):
  fileName = input("Name the file: ")
  fileName = fileName + ".txt"
  with open(fileName, mode ='w',encoding='utf-8') as my_file:
    for count in range(1,4):
      my_file.write(RecentScores[count].Name + "\n")
      my_file.write(str(RecentScores[count].Score) + "\n")
      my_file.write(RecentScores[count].Date + "\n")
        
def LoadScores():
  print("What was the name of your file?")
  count = -1
  RecentScores =[None]
  for Count in range(1, 3):
    RecentScores.append(TRecentScore())
  fileName = input()
  fileName = fileName + ".txt"
  array = []
  try:
    with open(fileName, mode='r',encoding='utf-8') as my_file:
      for line in (my_file):
        temp = line.rstrip("\n")
        array.append(temp)
    countI = 1
    countII = -1 
    while countII != 8:
      countII += 1
      RecentScores[countI].Name = array[countII]
      countII += 1
      RecentScores[countI].Score = array[countII]
      countII += 1
      RecentScores[countI].Date = array[countII]
  except FileNotFoundError:
    print()
    print("Your file was not found!")
    print("Empty recent scores list was created instead")
  return RecentScores
                            
  
def BubbleSortScores(RecentScores):
  complete = False
  while not complete:
    complete = True
    for I in range(1,len(RecentScores)-1):
      if RecentScores[I].Score < RecentScores[I+1].Score:
        try:
          complete = False
          temp = RecentScores[I]
          RecentScores[I] = RecentScores[I+1]
          RecentScores[I+1] = temp
        except:
          pass
  return RecentScores
    
def DisplayOptions():
  print()
  print("OPTION MENU")
  print('1. Set Ace to be HIGH or LOW')

def GetOptionChoice():
  print("Select an option from the menu (or enter q to quit):")
  complete = False
  while not complete:
    OptionChoice = input()
    if OptionChoice == '1':
      complete = True
    else:
      try:
        OptionChoice = OptionChoice.lower()
      except:
        print("Invalid Input!")
      if OptionChoice == 'q':
        complete = True
      else:
        print("Invalid Input!")
  return OptionChoice

def SetOptions(OptionChoice,ace_high):
  if OptionChoice == '1':
    ace_high = SetAceHighOrLow(ace_high)
  return ace_high  

def SetAceHighOrLow(ace_high):
  print("Do you want the ACE to be (h)igh or (l)ow?")
  complete = False
  while not complete:
    ace_high = input()
    ace_high = ace_high.lower()
    if ace_high == 'l':
      ace_high = False
      complete = True
    elif ace_high == 'h':
      ace_high = True
      complete = True
    else:
      print("Invalid Input!")
  print("Assigned!")
  
class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = ''
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''
  
def GetRank(RankNo):
  Rank = ''
  if not ace_high:
    if RankNo == 1:
      Rank = 'Ace'
    elif RankNo == 2:
      Rank = 'Two'
    elif RankNo == 3:
      Rank = 'Three'
    elif RankNo == 4:
      Rank = 'Four'
    elif RankNo == 5:
      Rank = 'Five'
    elif RankNo == 6:
      Rank = 'Six'
    elif RankNo == 7:
      Rank = 'Seven'
    elif RankNo == 8:
      Rank = 'Eight'
    elif RankNo == 9:
      Rank = 'Nine'
    elif RankNo == 10:
      Rank = 'Ten'
    elif RankNo == 11:
      Rank = 'Jack'
    elif RankNo == 12:
      Rank = 'Queen'
    elif RankNo == 13:
      Rank = 'King'
  else:
    if RankNo == 1:
      Rank = 'Two'
    elif RankNo == 2:
      Rank = 'Three'
    elif RankNo == 3:
      Rank = 'Four'
    elif RankNo == 4:
      Rank = 'Five'
    elif RankNo == 5:
      Rank = 'Six'
    elif RankNo == 6:
      Rank = 'Seven'
    elif RankNo == 7:
      Rank = 'Eight'
    elif RankNo == 8:
      Rank = 'Nine'
    elif RankNo == 9:
      Rank = 'Ten'
    elif RankNo == 10:
      Rank = 'Jack'
    elif RankNo == 11:
      Rank = 'Queen'
    elif RankNo == 12:
      Rank = 'King'
    elif RankNo == 13:
      Rank = 'Ace'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save file')
  print('7. Load file')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  Choice = Choice.lower()
  print()
  if Choice == "quit":
    Choice = "q"
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  complete = False
  print("Please enter your name: ")
  while not complete:
    name = input()
    if len(name) != 0:
      complete = True
    else:
      print()
      print("You did not enter anything!")
      print("Try again: ")
  return name
    

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice.lower()
  if Choice == "yes":
    Choice = "y"
  elif Choice == "no":
    Choice = "n"
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = None

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<10}{1:<10}{2:<10}".format("Name","Score","Date"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10}{1:<10}{2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Score,RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  PlayerName = GetPlayerName()
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  CurrentDate = datetime.date.today()
  CurrentDate = CurrentDate.strftime("%d/%m/%Y")
  RecentScores[Count].Date = CurrentDate    

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    choice = CheckUpdate()
    if choice == "y":
      UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    choice = CheckUpdate()
    if choice == "y":
      UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      RecentScores = BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      ace_high = SetOptions(OptionChoice,ace_high)
    elif Choice == '6':
      SaveScores(RecentScores)
    elif Choice == '7':
      RecentScores = LoadScores()
      
  
