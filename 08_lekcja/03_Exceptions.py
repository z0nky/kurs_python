

try:
    x = float(input("Podaj liczbę:"))
    result = 4/x
except ValueError as e:
    # handle ValueError exception
    print(e)
except (TypeError, ZeroDivisionError) as e:
    print(e)
except:
   # handle all other exceptions
   print('Nie mam pojęcia jakim jestem błędem!')