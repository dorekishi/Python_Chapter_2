def make_album(artist_name='ken carson', album_title='a great chaos', number_of_songs=None):
    """builds a dictionary that describes a music album"""

    if number_of_songs:
        album = {
            'Album Title': album_title.title(),
            'Number of Songs': number_of_songs,
            'Artist': artist_name.title(),
        }

    else:
        album = {
            'Album Title'   : album_title.title(),
            'Artist'        : artist_name.title(),
        }

    return album

while True:
    print('Hello User.')
    print("(enter 'quit' to quit at any time)\n")
    response_1 = input("Enter Artist's Name:  ")
    if response_1 == 'quit':
        break
    response_2 = input("Enter Artist's Album: ")
    if response_2 == 'quit':
        break
    album_responded = make_album(response_1, response_2)
    print('\n')
    print(album_responded)
    print('\n')