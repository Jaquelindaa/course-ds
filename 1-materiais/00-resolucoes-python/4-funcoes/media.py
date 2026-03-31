def media(n1, n2, n3, T):
    if T == "A":
        media = (n1 + n2 + n3) / 3
    elif T == "P":
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    else:
        media = 0
    
    return media

media = media(7, 8, 9, "A")
print(f"Média: {media:.2f}")