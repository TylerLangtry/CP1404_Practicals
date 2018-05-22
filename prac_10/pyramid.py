def get_blocks(rows):
    if rows <= 0:
        return 0
    return rows + get_blocks(rows-1)


rows = int(input("rows?:"))
print(get_blocks(rows))
