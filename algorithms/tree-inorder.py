from typing import Optional, List
from structures import TreeNode


def TraverseInorder(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []

    current = root
    visited = set()
    parents = []
    while True:
        print(
            f'current={current.val} len(parents)={len(parents)} res={result}')

        # have unvisited left - go left and save parent beforehand
        if current.left and not current.left in visited:
            parents.append(current)
            current = current.left
            continue

        # no unvisited left? save yourself if haven't already
        if not current in visited:
            result.append(current.val)
            visited.add(current)

        # no unvisited left? try right and save parent beforehand
        if current.right and not current.right in visited:
            parents.append(current)
            current = current.right
            continue

        # neither left or right left? go back to parent
        if parents:
            current = parents[-1]
            parents.pop()
            continue

        # no parent to back to - we are done
        break

    return result
