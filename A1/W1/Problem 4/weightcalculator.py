__author__ = 'Danny de Snoo, HR-nr: 1091749'

# pre-define the weight of the widgets and gizmos
def_widget = 75;
def_gizmo = 112;

# Request a input from the user for the amount of widgets and gizmo's they orderd
input_widgets = int(input("Number of widgets: "))
input_gizmos = int(input("Number of gizmos: "))

# Calculate the weights of the ordered Widgets, Gizmos and the total of the order
calc_widgets = input_widgets * def_widget
calc_gizmos = input_gizmos * def_gizmo
calc_total = calc_widgets + calc_gizmos

# Print the results
print("The Total Weight of the Order: " + str(calc_total) + " grams")
