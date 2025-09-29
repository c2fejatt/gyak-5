#HIÁNYZIK INNEN HALÓ
a = float(input("Kérem az 'a' oldalát a háromszögnek! "))
b = float(input("Kérem az 'b' oldalát a háromszögnek! "))
c = float(input("Kérem az 'c' oldalát a háromszögnek! "))

if a + b > c or a + c > b or c + b > a:
    print("Ez érvényes háromszög!")
else:
    print("Ez nem érvényes háromszög!")


print("\nMost pedig ki fogjuk szmámolni a téglalap kerületét meg területét")
egyikOldal = float(input("A téglalap egyik oldala: "))
masikOldal = float(input("A téglalap másik oldala: ")) 

print(f"Téglalap területe: {egyikOldal * masikOldal}")
print(f"Téglalap kerülete: {2 * (egyikOldal + masikOldal)}") #ez gatya, hazudsz te tamusom