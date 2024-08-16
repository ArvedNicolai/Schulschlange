# Definition einer Funktion zum Erstellen eines neuen Knotens
def create_node(key):
    return {'left': None, 'right': None, 'value': key}

# Definition einer Funktion zum Einfügen eines neuen Knotens in den Baum
def insert_node(tree, key):
    if tree is None:
        return create_node(key)
    else:
        if key < tree['value']:
            tree['left'] = insert_node(tree['left'], key)
        else:
            tree['right'] = insert_node(tree['right'], key)
    return tree

# Definition einer Funktion für die In-Order-Traversal
def in_order_traversal(tree, result):
    if tree:
        in_order_traversal(tree['left'], result)
        result.append(tree['value'])
        in_order_traversal(tree['right'], result)

def binary_search(tree, key):
    if tree is None:
        return False
    if key == tree['value']:
        return True
    elif key < tree['value']:
        return binary_search(tree['left'], key)
    else:
        return binary_search(tree['right'], key)