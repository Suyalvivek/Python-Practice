class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent = None
    def get_level(self):
        level=0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                #RECURSIVE METHOD
                child.print_tree()

    def add_children(self,child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_children(TreeNode("Macbook"))
    laptop.add_children(TreeNode("Windows"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_children(TreeNode("Iphone"))
    cellphone.add_children(TreeNode("Android"))

    tv = TreeNode("TV")
    tv.add_children(TreeNode("Samsung"))
    tv.add_children(TreeNode("Sony"))
    root.add_children(laptop)
    root.add_children(cellphone)
    root.add_children(tv)
    root.print_tree()

if __name__ == "__main__":
    build_product_tree()