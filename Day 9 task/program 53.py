class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count +=1
player1=Player("Alice","Beginner")
player2=Player("Bob","Intermediate")
print("Total Players:",Player.player_count)        
