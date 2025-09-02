players = [
    (101, 'jaiswal'),
    (102, 'gill')
]

print(players)

new_player = (103, 'abhishek')
print(new_player)

players.append(new_player)
print(players)

for player_tuple in players:
    if player_tuple[0] == 103:
        print(player_tuple)

players_dict = {player_tuple[0]: player_tuple for player_tuple in players}
print(players_dict[103])