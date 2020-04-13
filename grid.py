def grid(width, length, corners='+', horizontal_edges='-', vertical_edges='|'):
    print(corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + \
          corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + corners)
    for x in range(length // 2 - 1):
        print(vertical_edges + ' ' + (width - 5) // 4 * '  ' + \
              vertical_edges + ' ' + (width - 5) // 4 * '  ' + vertical_edges)
    print(corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + \
          corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + corners)
    for x in range(length // 2 - 1):
        print(vertical_edges + ' ' + (width - 5) // 4 * '  ' + \
              vertical_edges + ' ' + (width - 5) // 4 * '  ' + vertical_edges)
    print(corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + \
          corners + ' ' + (width - 5) // 4 * (horizontal_edges + ' ') + corners)