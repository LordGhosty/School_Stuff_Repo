r_inf = ("Ρομποτική", "κ. Παπαδόπουλος", "Δευτέρα")
t_inf = ("Θέατρο", "κ. Ιωάννου", "Τρίτη")
m_inf = ("Μουσική", "κ. Δημητρίου", "Τετάρτη")
s_inf = ("Αθλητισμός", "κ. Κωνσταντίνου", "Πέμπτη")

r_set = {"Άννα", "Γιάννης", "Μαρία"}
t_set = {"Μαρία", "Νίκος", "Ελένη"}
m_set = {"Πέτρος", "Άννα", "Σοφία"}
s_set = {"Γιάννης", "Κώστας", "Ελένη"}

info_lst = [r_inf, t_inf, m_inf, s_inf]
stu_lst = [r_set, t_set, m_set, s_set]

while True:
    print("\n--- ΜΕΝΟΥ ---")
    print("1. Εμφάνιση λεσχών")
    print("2. Στοιχεία λέσχης")
    print("3. Μαθητές λέσχης")
    print("4. Αναζήτηση μαθητή")
    print("5. Προσθήκη μαθητή")
    print("6. Διαγραφή μαθητή")
    print("7. Μοναδικοί μαθητές")
    print("8. Κοινοί μαθητές 2 λεσχών")
    print("9. Μαθητές μόνο 1 λέσχης")
    print("10. Έξοδος")

    choice = input("Επιλογή: ").strip()

    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            print("Τέλος.")
            break
        case _:
            print("Λάθος επιλογή.")