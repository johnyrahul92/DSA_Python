from bs import bs

cards =[1,4,4,4,8,2,9]
cards.sort(reverse=True)
print(cards)
query = 4

def get_card_position(cards, query):
    position=0
    while position<len(cards):
        if cards[position] == query:
            return position
        position +=1

    return -1    


def locate_cards(cards,query):
    def condition(mid):

        if cards[mid] == query:
            if mid-1 >= 0 and cards[mid-1]== query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return bs(0,len(cards)-1,condition)







print(get_card_position(cards,query))
print(locate_cards(cards,query))


   
    