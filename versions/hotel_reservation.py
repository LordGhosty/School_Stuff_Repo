reservations = {}
def view_reservations():
    if not reservations:
        print(' Δεν υπάρχουν κρατήσεις.')
    for room, guest in reservations.items(): 
        print(f' Δωμάτιο {room}: {guest}')

view_reservations()