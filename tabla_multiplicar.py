
def multiTable(multiplicando):
    i=1
    tabla=""

    while i < 11:
        if i == 10:
            tabla += f"{i} * {multiplicando} = {i * multiplicando}"
        else:
            tabla += f"{i} * {multiplicando} = {i * multiplicando}\n"
        i += 1
    return tabla
