wybor = input('wybierz \nW - wiertnictwo, \nS - plik excell z POM_STUD, '
              '\nR - plik excell z każdym punktem "dniówkowy",'
              '\nQ - anuluj: ').lower()


if wybor == 'w':
    import raport_wiertnictwo
elif wybor == 's':
    import studnie_pom
elif wybor == 'r':
    import raport_daily
elif wybor == 'q':
    quit()