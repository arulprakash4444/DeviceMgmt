from prettytable import PrettyTable


def TheArray2PT(Array):
    pt = PrettyTable()
    pt.field_names = Array[0]
    for i in range(1, len(Array)):
        pt.add_row(Array[i])

    print(pt)


# if __name__ == "__main__":
#     TheArray2PT(TheArray)