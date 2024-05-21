attendees = int(input("Enter number of attendees: "))  # Convert input to integer
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
