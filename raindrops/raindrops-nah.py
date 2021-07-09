def convert(number):
    results = ""

    if number % 3 == 0:
        results += "Pling"
    if number % 5 == 0:
        return "Plang"
    if number % 7 == 0:
        return "Plong"
    if number % 3 == 0 & number % 5 == 0 & number % 7 != 0:
        return "PlingPlang"
    if number % 3 == 0 & number % 7 == 0 & number % 5 != 0:
        return "PlingPlong"
    if number % 5 == 0 & number % 7 == 0 & number % 3 != 0:
        return "PlangPlong"
    if number % 3 == 0 & number % 5 == 0 & number % 7 == 0:
        return "PlingPlangPlong"
    else:
        return str(number)
