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

def update_reservation(room_number, new_name):
    if room_number not in reservations:
        raise KeyError(' Το δωμάτιο δεν έχει κράτηση!')
    reservations[room_number] = new_name
    print(f' Το δωμάτιο {room_number} ανατέθηκε στον {new_name}')

def delete_reservation(room_number):
    if room_number not in reservations:
        raise KeyError(' Δεν υπάρχει κράτηση για αυτό το δωμάτιο!')
    del reservations[room_number]
    print(f' Η κράτηση για το δωμάτιο {room_number} διαγράφηκε.')

try:
    book_room('Γιάννης', 101)
    book_room('Μαρία', 102)
    update_reservation(101, 'Νίκος')
    delete_reservation(102)
    
    print("\n-o-o-o-o-o-o~ Τελική Λίστα Κρατήσεων ~o-o-o-o-o-o")
    view_reservations()


except (ValueError, KeyError) as e: 
    print(f'Σφάλμα Συστήματος: {e}')