class Internal_Node:
    def __init__(self, character, left, right):
        self.character = character
        self.left = left
        self.right = right
        
class Leaf_Node:
    def __init__(self, language):
        self.language = language
        
def find_language(node, letters, answer):
    if isinstance(node, Leaf_Node):
        answer.add(node.language)
        return

    if node.character in letters:
        find_language(nodes[node.left], letters, answer)
    else:
        # When the character of the current node is not presents in the sentence, we need to check both branches.
        find_language(nodes[node.left], letters, answer)
        find_language(nodes[node.right], letters, answer)

n, p = map(int, input().split())

nodes = {}

for i in range (n):
    details = input().split()
    
    if details[0] == "I":
        nodes[details[1]] = Internal_Node(details[2], details[3], details[4])
    else:
        nodes[details[1]] = Leaf_Node(details[2])

node_ids = list(nodes.keys())

for node in nodes.values():
    if isinstance(node, Internal_Node):
        if node.left in node_ids:
            node_ids.remove(node.left)
        if node.right in node_ids:
            node_ids.remove(node.right)

root = nodes[node_ids[0]]

for i in range(p):
    characters = set(input())
    
    if " " in characters:
        characters.remove(" ")
        
    answer = set()
    
    find_language(root, characters, answer)
    
    answer = sorted(list(answer))
    print(*answer)
