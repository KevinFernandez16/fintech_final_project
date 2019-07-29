def options(room_type, furniture, color):
    for item in room_type and furniture:
        if room_type == "dining room" and furniture == "couch":
            return "ERROR! These don't mix!!"
print(options)
        