import random
# this is a built in module in python which will allow us to use a built in function to generate random numbers

class Die:


    def __init__(self):
        self._value = None 
        # we could have set value = None as a default agrument but we don't want to give user the permision to send any agrument 
        # here we opt to make this attribute non public

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    

class Player:
    def __init__(self, die , is_computer= False):
        self._die = die
        self._is_computer = is_computer
        self.counter = 5
        # initially we will set the counter value to 10 for both the players
        # here all attributes of this class are non public because we don't want them to be accessed from outside the class

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
# her we have ,mad eonly the getters of thes attributes , no setters so far
# now we define the increment counter and decrement counter methods

    def increment_counter(self):
        self.counter += 1
        return self.counter
    
    def decrement_counter(self):
        self.counter -= 1
        return self.counter
    
# here we are using the method of Die class in the Player class
# this is a composition relationship
    def roll_die(self):
        return self.die.roll()
    #using the return keyword is very important here , even though the actual method in the die class is returning a value , we need to return that value from this method as well


# now we will define a DiceGame class to implement the actual logic of the game
class DiceGame:


    def __init__(self, player , computer):
        self._player = player
        self._computer = computer
        # here we opted to make these attributes non public , however we will not define any getters or seters for thiese attributes
        # we will define a method to play the game

    def play_round(self):
        print("\n---- New Round ----")
        input(" 🎲 Press Any key to roll the Dice 🎲")
        # now this input statement will stop te program and ait till the user gives any input
        player_value = self._player.roll_die() 
        # now this is the value passed by the human player roll_die function
        computer_value = self._computer.roll_die()
        # now this is the value passed by the computer player roll_die function
        # Showing the values
        print(f"Your Die : {player_value}")
        print(f"Computer's Die : {computer_value}")
# now we will compare the values and decide the winner
# here we call the conclude results method passing it the values of both player and computer die
        self.conclude_results(player_value , computer_value)
# printing counter of each player by calling the show_counter method
        self.show_counter()
    

    def conclude_results(self, player_value , computer_value):
        if player_value > computer_value:
            print("You won this round 🎉")
            self.update_counter(winner= self._player , loser = self._computer)
# here we are specifying the update counter method to update the counter of the winner and loser
        elif player_value < computer_value:
            print("Computer won this round , Try again! 🙃")
            self.update_counter(winner= self._computer , loser = self._player)
        else:
            print("This round is a draw 😀")

    
    def show_counter(self):
        print(f"\n Your Counter : {self._player.counter}")
        print(f"Computer's Counter : {self._computer.counter}")


    def update_counter(self, winner , loser):
        winner.increment_counter()
        loser.decrement_counter()
        return winner.counter , loser.counter
    
    def game_over(self):
        print("\n =====================================")
        print("     🎲   Game Over!   🎲     ") 
        print("=====================================")

        if self._player.counter == 0:
            print("You Lost the Game , Better Luck Next Time! 😢")
        elif self._computer.counter == 0:
            print("Congratulations! You Won the Game 🎉")

        print("=====================================")

    def play(self):
        print("=====================================")
        print("      Welcome to the Dice Game  🎲   ")
        print("=====================================")
        print("Rules of the Game :")
        print("The game is simple , you will roll a dice and so will the computer , the one with the higher number wins the round")
        print("You have 5 points , if you win a round , you will get a point , if you lose a round , you will lose a point , if the round is a draw , no points will be added or deducted")
        # since we don't know the number of rounds there will be in the game , so we will use an infinite loop in this case 
        # we will use a while true loop , which runs untill it finds a break statement
        while True:
            self.play_round()
            if self._player.counter == 0 or self._computer.counter == 0:
                self.game_over()
                break

        

# creating instances
# first of all we will create Dice instances
player_die = Die()
computer_die = Die()
# now we will create Player instances
human_player = Player(player_die)
computer_player = Player(computer_die , is_computer=True)
# now we will create DiceGame instance
game = DiceGame(human_player , computer_player)
# now we will start the game
game.play()