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

album_default = make_album()
print(album_default)

print('\n')

album_1 = make_album('tyler the creator', 'chromakopia', 14)
print(album_1)

print('\n')

album_2 = make_album('playboi carti', 'i am music')
print(album_2)