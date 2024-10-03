favorite_languages = {          #people who have already taken poll with their favorite language
    'jen':      'python',
    'sarah':    'c',
    'edward':   'rust',
    'phil':     'python'
}

friends = [         #people who should take the poll
    'phil',
    'sarah',
    'jaden',
    'avery',
    'armando',
    'mir',
    'nick',
    'john',
    'von'
]

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"\nHi {friend.title()}, thanks for taking the poll!")

for friend in friends:
    if friend not in favorite_languages.keys():
        print(f"\nHi {friend.title()}, can you please take the poll :)" )