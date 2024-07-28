is_year_leap = int(input("Введите год:"))
if (is_year_leap % 4 == 0):
    print ("год", is_year_leap,":", True)
else:
    print ("год", is_year_leap,":", False)
