#More list notes 4th November, 2015

import random

#Sequences:
    #strings: sequence of characters(Immutable:(cant be changed)) "Hello",'Hello','''Hello'''.
    #lists: sequence of anything: numbers, strings, other lists, objects, etc. (mutable) [list items]
    #Tupils: same as a list, but it is Immutable. (255,255,255)

#Concepts:
    #For dynamic items in our programs:
        #Lists are the best option (at the moment).
            #we need to add items. (add a new item)
            #we need to remove items. (remove a item)
            #we need to change items. (change a bullet's position)
    #create an empty list:
#bullet_list=[]
    #to add things to a list:
#bullet_list.append([100,100])
    #to remove an item from a list:
#del bullet_list[i] #remove item at position i
# or bullet_list.remove([100,100]) #remove item with value [100,100]
#people=["joe","anne","julius","george"]
#people.append("roger")
#del people[3] #or people.remove("george")
#print(people)

#Example
#list1=[]
#len(list1)
#list1.append("tom")
#list1.append("joe")
#list1.append("anne")
#list1.append("george")
#list1.append("roger")
#list1
#del list1[3]
#list1.append("george")
#list1.remove("george")
#list1
#list1.remove("joe")
#list1
#del list1
#list1=[]
#list1.append([100,100])
#list1
#list1.append([50,95])
#list1[0]
#list1[-1]
#list1.append([90,30])
#list1
#list1.remove([100,100])
#list1
#del list1[1]
#list1

suits = ["H","D","C","S"]
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_deck = []

for suit in suits:
    for rank in ranks:
        card_deck.append(rank+suit)
#print(card_deck)
#print(len(card_deck))
#draw a 5 card hand randomly
#hand1=[]
#hand2=[]
#for i in range(0,4):
#    card = random.choice(card_deck)
#    card_deck.remove(card)
#    hand1.append(card)
#    #hand 2
#    card = random.choice(card_deck)
#    card_deck.remove(card)
#    hand2.append(card)
#print(hand1)
#print(hand2)
#print(len(card_deck))
#return hands to the deck
#for i in range(0,5):
#    card_deck.append(hand1[i])
#    card_deck.append(hand2[i])
#print(len(card_deck))

#shuffle the cards
card_deck_shuffled=[]

while len(card_deck)>0:
    card=random.choice(card_deck)
    card_deck.remove(card)
    card_deck_shuffled.append(card)

hand1=[]
hand2=[]
for i in range(0,5):
    card = card_deck_shuffled[0]
    del card_deck_shuffled[0]
    hand1.append(card)
    card = card_deck_shuffled[0]
    del card_deck_shuffled[0]
    hand2.append(card)
hand1.sort
hand2.sort
print(hand1.sort)
print(hand2.sort)
print(hand2)
