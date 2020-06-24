# from gpiozero import LED
# from time import sleep 


# red = LED(17)

# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     sleep(1)

def addAndPrint(a, b):
    c = a+b
    print("Das Ergebnis lautet: ", c)
    return c


def aubAndPrint(a, b):
    c = a-b
    print("Das Ergebnis lautet: ", c)
    return c



addAndPrint(10, 5)


