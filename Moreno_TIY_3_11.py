#the list
places_to_visit=['italy',
                 'vienna',
                 'australia',
                 'new zealand']

#index error code below
print(f'{places_to_visit[4].title()} is the capitol France.')

#fixed code below
places_to_visit.append('paris')
print(f'{places_to_visit[4].title()} is the capitol France.')