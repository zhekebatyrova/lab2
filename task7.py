def election(x, y, z):
    true_counter = 0
    false_counter = 0

    if x == 0:
        false_counter += 1
    elif x == 1:
        true_counter += 1

    if y == 0:
        false_counter += 1
    elif y == 1:
        true_counter += 1

    if z == 0:
        false_counter += 1
    elif z == 1:
        true_counter += 1

    if true_counter > false_counter:
        return 1
    else:
        return 0
