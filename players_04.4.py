players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are first three players in our team")
for player in players[:3]:
    print(player.title())

#列表复制
other_players=players[:]
print(other_players)
#如果直接赋值则是两个相同的列表