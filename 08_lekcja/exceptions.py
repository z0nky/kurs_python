# try:
#   x = 5 / 0
# except ZeroDivisionError as e:
#   print("Pamiętaj kolego nie dziel przez zero! Twój wyjątek to:", e)
#   x = 0 # załóżmy, że potrzebujemy x więc go nadpiszemy

# to obsługa kilku wyjątków na raz:
try:
   my_function()
except ValueError as e:
   # handle ValueError exception
   print(e)

except (TypeError, ZeroDivisionError) as e:
   print(e)

except:
   # handle all other exceptions
   print('Nie mam pojęcia jakim jestem błędem!')