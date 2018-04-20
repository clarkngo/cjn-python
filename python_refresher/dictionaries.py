my_set = {1, 3, 5}
my_dict = { 'name': 'Jose', 'age': 90, 'grades':[13, 45, 66, 90]}

another_dict = { 1: 15, 2: 75, 3: 150 }

lottery_players = [
{
	'name': 'Rolf',
	'numbers': (13, 45, 66, 23, 22)
},
{
	'name': 'John',
	'numbers': (14, 56, 80, 23, 22)
}
]

universities = [
	{
		'name': 'Oxford',
		'location': 'UK'
	},
	{
		'name': 'MIT',
		'location': 'US'	
	}

]

sum(lottery_players['numbers'])

# lottery_player['name'] = 'John'
# lottery_player['numbers'][0] = 50

lottery_players[0].total()

lottery_players.total()