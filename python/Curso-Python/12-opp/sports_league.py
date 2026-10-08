"""

We want to implement a simple system for managing a sports league, where each team has several players with individual performance scores.

Class Player: should include attributes such as
name, position, and performance_score.
Class Team: should include attributes like
team_name and a list of Player objects.
External function best_player(team): this function
must not be part of any class. It should receive a Team object as parameter,
iterate through its list of players, and return the Player with the
highest performance_score.
Check the example code to see how to implement your classes and the external function correctly.


-----------------


Queremos implementar un sistema sencillo para gestionar una liga deportiva, donde cada equipo tenga varios jugadores con puntuaciones de rendimiento individuales.

ClasePlayer : debe incluir atributos como
name, position, y performance_score.
ClaseTeam : debe incluir atributos como
team_namey una lista de Playerobjetos.
Función externabest_player(team) : esta función
no debe formar parte de ninguna clase . Debe recibir un Teamobjeto como parámetro,
iterar a través de su lista de jugadores y devolver el que Playertenga la
puntuación más alta performance_score.
Consulta el código de ejemplo para ver cómo implementar correctamente tus clases y la función externa.


"""




# Your code goes here

#-------------
# Player
#-------------
class Player:

    def __init__(self, name, position, performance_score):
        self.name = name
        self.position = position
        self.performance_score = performance_score

    
    def __repr__(self):
        return f" {self.name} {self.position} {self.performance_score}"





#-------------
# Team
#-------------
class Team:

    def __init__(self, team_name, players = []):
        self.team_name = team_name
        self.players = players


    def __repr__(self):
        return f"{self.team_name} {self.players}"





def best_player(team: Team):
    player = team.players[0]

    for i in range(1, len(team.players)):
        if team.players[i].performance_score > player.performance_score:
            player = team.players[i]

    return player

     ## return max(team.players, key=lambda p: p.performance_score)

    



# Example usage

# Create players and a team
leo = Player("Leo", "Defender", 95)
mike = Player("Mike", "Forward", 80)
teamA = Team("Alpha")
teamA.players.extend([leo, mike])

# Find the best player
star = best_player(teamA)
print(f"The best player in {teamA.team_name} is {star.name}.")
print(f"He/She is a {star.position} and his/her score is {star.performance_score}.")