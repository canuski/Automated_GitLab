from rich import print
from rich.tree import Tree


def build_tree(dir):
    # maak een boom met de directory
    tree = Tree(
        f"[yellow]{dir['name']}[/yellow]")

    # gfa over over de kinderen van de directory
    for child in dir["children"]:
        # maak onderliggende boom voor elk kind en voeg het toe aan de boom
        subtree = build_tree(child)
        tree.add(subtree)

    return tree


folder_hierarchy = {
    "name": "level 1 directory",
    "level": 1,
    "children": [
            {
                "name": "level 2 directory A",
                "level": 2,
                "children": [
                    {
                        "name": "level 3 directory A1",
                        "level": 3,
                        "children": []
                    },
                    {
                        "name": "level 3 directory A2",
                        "level": 3,
                        "children": []
                    }
                ]
            },
        {
                "name": "level 2 directory B",
                "level": 2,
                "children": [
                    {
                        "name": "level 3 directory B1",
                        "level": 3,
                        "children": []
                    }
                ]
                },
        {
                "name": "level 2 directory C",
                "level": 2,
                "children": [
                    {
                        "name": "level 3 directory C1",
                        "level": 3,
                        "children": []
                    },
                    {
                        "name": "level 3 directory C2",
                        "level": 3,
                        "children": [
                            {
                                "name": "level 4 directory C3",
                                "level": 4,
                                "children": []
                            }
                        ]
                    }
                ]
            }
    ]
}

tree = build_tree(folder_hierarchy)
print(tree)
