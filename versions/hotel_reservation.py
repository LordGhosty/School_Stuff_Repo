reservations = {}

def view_reservations():
    if not reservations:
        print(' Δεν υπάρχουν κρατήσεις.')
    for room, guest in reservations.items(): 
        print(f' Δωμάτιο {room}: {guest}')

def book_room(name, room_number):
    if room_number in reservations:
        raise ValueError(' Το δωμάτιο είναι ήδη κλεισμένο!')
    reservations[room_number] = name
    print(f' Κράτηση επιβεβαιώθηκε για {name} στο δωμάτιο {room_number}')

view_reservations()