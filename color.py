def myFun(elev):
    if elev > 1000 and elev <= 2000:
        return "blue"
    elif elev > 2000 and elev <= 3000:
        return "green"
    elif elev > 3000:
        return "red"
    else:
        return "black"