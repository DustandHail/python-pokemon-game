import random

class Pokemon:
    def __init__(self, name, max_moves = 4):
        self.name = name
        self.max_moves = max_moves
        self.moves = []

    def teach_move(self, move_name):
        if len(self.moves) < self.max_moves:
            self.moves.append(move_name)
            print(f"{self.name} learned {move_name}!")
        else:
            print(f"{self.name} already knows {self.max_moves} moves and cannot learn {move_name}!")
            self.display_moves()

            
            choice1 = input(f"Replace a move with {move_name}? (y/n): ")
            if choice1 == "yes":
                choice2 = int(input(f"Choose a move to replace 1 - {self.max_moves} to forget:"))
                index_to_replace = choice2 - 1
                old_move = self.moves[index_to_replace]
                self.moves[index_to_replace] = move_name

                print(f"1, 2, and... Poof! {self.name} forgot {old_move} and learned {move_name}!")
            else:
                print(f"{self.name} did not learn {move_name}!")

    def display_moves(self):
         print(f"---{self.name}'s Moveset---")
         for index, move in enumerate(self.moves, start = 1):
             print(f"{index}. {move}")


chimchar = Pokemon("Chimchar")
#piplup = Pokemon("Piplup")
#turtwig = Pokemon("Turtwig")

chimchar.teach_move("Scratch")
chimchar.teach_move("Leer")
chimchar.teach_move("Close Combat")
chimchar.teach_move("Mach Punch")

chimchar.teach_move("Ember")

#piplup.teach_move("Tackle")
#piplup.teach_move("Growl")

#turtwig.teach_move("Tackle")
#turtwig.teach_move("Leer")

print("---VERIFICATION---")
print(f"{chimchar.name}'s move: {chimchar.moves}")
#print(f"{piplup.name}'s move: {piplup.moves}")
#print(f"{turtwig.name}'s move: {turtwig.moves}")

