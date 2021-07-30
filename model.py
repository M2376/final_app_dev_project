def outcome(Markers, Scissors, Pillows, Wood):
    score = 0
    if Markers == "Plain o'l Markers":
        score += 4
    elif Markers == "Crayola Markers":
        score += 24
    elif Markers == "Bic Markers":
        score += 2
    elif Markers == "Sharpie Markers":
        score += 3
    else:
        score += 0
    
    if Scissors == "Fiskars Scissors":
        score += 13
    elif Scissors == "Ali-Express Scissors":
        score += 200
    else:
        score += 0

    if Pillows == "Teacup Pillows":
        score += 2
    elif Pillows == "Embriodery Pillows":
        score += 3
    elif Pillows == "Elephant Pillows":
        score += 2
    else:
        score += 0

    if Wood == "Paper":
        score += 1
    elif Wood == "Table":
        score += 2
    elif Wood == "Stool":
        score += 3
    else:
        score += 0
    print(Markers,Scissors, Pillows, Wood)
    return score
    