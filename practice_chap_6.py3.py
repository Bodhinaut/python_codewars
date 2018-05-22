people_I_know = {
        'first_name' : 'amanda',
        'last_name' : 'cornell',
        'age' : '23',
        'city' : 'staunton',
        }

print(people_I_know['first_name'])

fav_num = {
    'first' : 13,
    'second' : 7,
    'third' : 3,
    'fourth' : 23,
    }

print( "Third fav " + str(fav_num['third'] ) + " " + "fourth fav " + str(fav_num['fourth']) + " " + 
      "second fav " + str(fav_num['second'] )  + " " + "first fav " + str(fav_num['first']) )


best_movies = {
    '1' : 'eternal sunshine',
    '2' : 'good will hunting',
    '3' : 'fight club',
    '4' : 'the prestige',
    '5' : 'the imitation game',

    }

print (
    "\n" +
    best_movies['1'].title() + ": is my number one favorite.\n" + 
    best_movies['2'].title() + ": is my second favorite.\n" +
    best_movies['3'].title() + ": I had to think about, it's good though.\n" +
    best_movies['4'].title() + ": most def is a great.\n" +
    best_movies['5'].title() + ": another must watch for sure.\n"
    )
