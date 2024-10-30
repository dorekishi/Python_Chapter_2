from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)    # [:] allows the designs to stay intact with their original list
show_completed_models(completed_models)                 # Can be a hassle for time and memory with larger lists

#print_models(unprinted_designs, completed_models)   # Without it, they will be removed
#show_completed_models(completed_models)