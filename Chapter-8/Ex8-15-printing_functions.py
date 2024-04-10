# Printing
#printing_models.py:
# remove Ex8-15- from Ex8-15-printing_functions.py then run it
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)