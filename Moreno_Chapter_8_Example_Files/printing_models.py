    # With functions

    # A lot easier to read

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left."""
    """Move each design to completed_models after printing"""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)



def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)    # [:] allows the designs to stay intact with their original list
show_completed_models(completed_models)                 # Can be a hassle for time and memory with larger lists

#print_models(unprinted_designs, completed_models)   # Without it, they will be removed
#show_completed_models(completed_models)