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
            print("\nΛέσχες:")
            for inf in info_lst:
                print("-", inf[0])

        case "2":
            c = input("Επίλεξε λέσχη (1-4): ").strip()
            if c in ["1", "2", "3", "4"]:
                idx = int(c) - 1
                print(f"Λέσχη: {info_lst[idx][0]}, Υπεύθυνος: {info_lst[idx][1]}, Μέρα: {info_lst[idx][2]}")
            else:
                print("Λάθος.")

        case "3":
            c = input("Επίλεξε λέσχη (1-4): ").strip()
            if c in ["1", "2", "3", "4"]:
                idx = int(c) - 1
                print(f"Μαθητές:", stu_lst[idx])
            else:
                print("Λάθος.")

        case "4":
            name = input("Όνομα: ").strip().title()
            fnd = False
            for i in range(4):
                if name in stu_lst[i]:
                    print(f"Βρέθηκε στη λέσχη: {info_lst[i][0]}")
                    fnd = True
            if not fnd:
                print("Δεν βρέθηκε.")

        case "5":
            c = input("Λέσχη για προσθήκη (1-4): ").strip()
            if c in ["1", "2", "3", "4"]:
                name = input("Όνομα: ").strip().title()
                idx = int(c) - 1
                stu_lst[idx].add(name)
                print("ΟΚ.")
            else:
                print("Λάθος.")

        case "6":
            c = input("Λέσχη για διαγραφή (1-4): ").strip()
            if c in ["1", "2", "3", "4"]:
                name = input("Όνομα: ").strip().title()
                idx = int(c) - 1
                if name in stu_lst[idx]:
                    stu_lst[idx].remove(name)
                    print("ΟΚ.")
                else:
                    print("Δεν υπάρχει.")
            else:
                print("Λάθος.")

        case "7":
            all_s = r_set | t_set | m_set | s_set
            print("Όλοι:", all_s)

        case "8":
            c1 = input("Λέσχη 1 (1-4): ").strip()
            c2 = input("Λέσχη 2 (1-4): ").strip()
            if c1 in ["1","2","3","4"] and c2 in ["1","2","3","4"]:
                if c1 == c2:
                    print("Ίδια λέσχη.")
                else:
                    i1, i2 = int(c1)-1, int(c2)-1
                    com = stu_lst[i1] & stu_lst[i2]
                    print("Κοινοί:", com)
            else:
                print("Λάθος.")

        case "9":
            c = input("Λέσχη (1-4): ").strip()
            if c in ["1", "2", "3", "4"]:
                idx = int(c) - 1
                target_s = stu_lst[idx]
                other_s = set()
                for j in range(4):
                    if j != idx:
                        other_s = other_s | stu_lst[j]
                only_here = target_s - other_s
                print("Μόνο εδώ:", only_here)
            else:
                print("Λάθος.")

        case "10":
            print("Πραγματοποιήθηκε έξοδος.")
            break
        case _:
            print("Λάθος επιλογή.")