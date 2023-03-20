# Mechanics 

## Classes

### Mechanics
This class will hold all the basic mechanics that will be required for us to complete the game Settlers. This class will 
be the super class for many of the other classes stored in the mechanics folder. 

#### Functions
* dice_roll: Emulates the dice roll in Catan.
#### Methods

#### Variables

### Player
This class will act as the player in catan game.
#### Constructor
Player: Sets of the players attributes to 0.

#### Functions

* roll: Simulates the dice roll each round. Returns an integer between 2 and 12. Inherits from the dice_roll in the 
Mechanics class.

#### Methods

#### Variables
* victory_Points: How many victory points the player has currently.
* wood: How much of the wood material the player has.
* livestock: how much of the livestock material the player has.
* clay: how much of the clay material the player has.
* stone: how much of the stone material the player has.
* hay: how much of the hay material the player has.
* roads: how many roads the player has.
* settlements: how many settlements the player has.
* cities: how many cities the player has.
* knights: how many knights the player has.
* cards_in_hand: how many cards the player has in there hand.

### Start
This class will be used to for setting up the settlers game, i.e. deciding on what game type the players want to play. 
The player will also be able to decided on how long of a timer they want if they decide on a quick game.
#### Functions
* game_type: Used to decide which game type the player wants to play. Returns True for a full game and False for a quick
game.
#### Methods

#### Variables


