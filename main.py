#Napraviti database management system u pythonu za univerzitet politehnickog fakulteta u zenici.
#Sistem treba moci unijeti studenta sa brojem indexa, imenom, prezimenom, godinom studija
#ucitati iz fajla i upisati u fajl

class Student():
    def __init__(self, br_indexa, ime, prezime, godina_studija):
        self.br_indexa = br_indexa
        self.ime = ime
        self.prezime = prezime
        self.godina_studija = godina_studija



def save_data(student_list):
    save_file = open("studenti.txt","a")
    for i in range(0,len(student_list)):
        save_file.write(student_list[i].br_indexa)
        save_file.write("\n")
        save_file.write(student_list[i].ime)
        save_file.write("\n")
        save_file.write(student_list[i].prezime)
        save_file.write("\n")
        save_file.write(student_list[i].godina_studija)
        save_file.write("\n#\n")
    save_file.close()


def Unesi_Studenta():
    student = Student(input("Unesite broj indexa: "), input("Unesite vase ime: "), input("Unesite prezime: "), input("Unesite godinu studija: "))
    student_list.append(student)
    print(f"Dodan student: {student.ime}")
def Izbaci_Studenta(student_list):
    pretraga=input("Unesite index studenta kojeg zelite izbaciti: ")
    for i in range(0,len(student_list)):
        if student_list[i].br_indexa == pretraga:
            student_list.remove(student_list[i])
            print(f"Izbacen student sa indeksom {pretraga}")

def Ispisi_Listu(student_list):
    for i in range(0,len(student_list)):
        print(f"Broj indexa studenta:{student_list[i].br_indexa}")
        print(f"Ime studenta:{student_list[i].ime}")
        print(f"Prezime studenta:{student_list[i].prezime}")
        print(f"Godina studija studenta:{student_list[i].godina_studija}")


def Ispisi_Jednog_Studenta(student_list,br_indexa):
    for i in range(0,len(student_list)):
        if student_list[i].br_indexa == br_indexa:
            print(f"Broj indexa studenta:{student_list[i].br_indexa}")
            print(f"Ime studenta:{student_list[i].ime}")
            print(f"Prezime studenta:{student_list[i].prezime}")
            print(f"Godina studija studenta:{student_list[i].godina_studija}")


student_list = []
izbor:int = 0
while izbor != 5:
    print(
        "1. Unesi novog studenta\n2.Izbaci studenta\n3.Ispisi sve studente\n4.Ispisi jednog studenta\n5.Ugasi program")
    izbor = int(input("Izaberite opciju:"))
    match izbor:
        case 1:
            Unesi_Studenta()
        case 2:
            Izbaci_Studenta(student_list)
        case 3:
            Ispisi_Listu(student_list)
        case 4:
            Ispisi_Jednog_Studenta(student_list, input("Unesite broj indexa: "))
save_data(student_list)



