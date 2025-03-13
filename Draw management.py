from draw_management import DrawManagement

# Create a list of participants
participants = ["Team A", "Team B", "Team C", "Team D", "Team E"]

# Initialize the DrawManagement class with a sport and participants
draw_manager = DrawManagement("tennis", participants)

# Generate the draw
draw = draw_manager.generate_draw()

# Print the results
print("Tennis Draw:")
for match in draw:
    print(match)


