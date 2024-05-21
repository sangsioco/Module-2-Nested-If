# code from eventplannerpart2
attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
facilities = []

if attendees > 20:
    facilities.append("audio system")

if 50 < attendees < 100:
    facilities.append("projector")

if attendees > 100:
    facilities.append("projector and audio system")

print("Venue:", venue)
if facilities:
    print("Additional Facilities Recommendation:", ",".join(facilities))
else:
    print("No additional facilities recommended.")

# Task 3 Vegetarian food

vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")

if vegetarian_choice.lower() == "yes":
    print("We recommend Veggie Delight Caterers for vegetarian food.")
else:
    print("We recommend Gourmet Meals Caterers.")
