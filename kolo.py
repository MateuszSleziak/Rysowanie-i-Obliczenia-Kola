import math
import turtle

def rys_k(r):
    turtle.bgcolor("grey")
    turtle.circle(r)
    turtle.done()
def promien():
    while True:
        try:
            r = float(input("Podaj promień koła: "))
            if r < 0:
                print("Promień nie może być ujemny. Podaj poprawny promień.")
                continue
            else:
                rys_k(r)
                return r
        except ValueError:
            print("Podaj poprawny promień koła.")

def obwod_kola(r):
    c = 2 * math.pi * r
    return c

def pole_kola(r):
    a = math.pi * (r ** 2)
    return a

if __name__ == "__main__":
    r = promien()
    print(f"Promień koła: {r}")
    c = obwod_kola(r)
    print(f"Obwód koła: {round(c, 3)}")
    a = pole_kola(r)
    print(f"Pole koła: {round(a, 3)}")