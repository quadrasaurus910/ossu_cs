'''
    Provided implementation. Do not modify any of the functions below
    You should acquaint yourself with how to initialize and access data from
    Node objects but you do not need to fully understand how this class works internally
'''

class Node:
    def __init__(self, value, left_child=None, right_child=None):
        '''
        Constructs an instance of Node
        Inputs:
            value: An object, the value held by this node
            left_child: A Node object if this node has a left child, None otherwise
            right_child: A Node object if this node has a right child, None otherwise
        '''
        if isinstance(left_child, Node):
            self.left = left_child
        elif left_child == None:
            self.left = None
        else:
            raise TypeError("Left child not an instance of Node")

        if isinstance(right_child, Node):
            self.right = right_child
        elif right_child == None:
            self.right = None
        else:
            raise TypeError("Right child not an instance of Node")

        self.value = value

    def get_left_child(self):
        '''
        Returns this node's left child if present. None otherwise
        '''
        return self.left

    def get_right_child(self):
        '''
        Returns this node's right child if present. None otherwise
        '''
        return self.right

    def get_value(self):
        '''
        Returns the object held by this node
        '''
        return self.value

    def __eq__(self, tree):
        '''
        Overloads the == operator
        Example usage: Node(6, Node(1)) == Node(6, Node(1)) evaluates to True
        Output:
            True or False if the tree is equal or not
        '''
        if not isinstance(tree, Node):
            return False
        return (self.value == tree.value and
                self.left == tree.left and
                self.right == tree.right)

    def __str__(self):
        '''
        Output:
            A well formated string representing the tree (assumes a node can have at most one parent)
        '''
        def set_tier_map(tree,current_tier,tier_map):
            if current_tier not in tier_map:
                tier_map[current_tier] = [tree]
            else:
                tier_map[current_tier].append(tree)
            if tree.get_left_child() is not None:
                set_tier_map(tree.get_left_child(),current_tier+1,tier_map)
            if tree.get_right_child() is not None:
                set_tier_map(tree.get_right_child(),current_tier+1,tier_map)
        tiers = {}
        set_tier_map(self,0,tiers)
        nextTier = [True]
        for key in sorted(tiers,reverse=False):
            current_tier = nextTier[:]
            nextTier = [' ' for i in range(2**(key+1))]
            for tree in tiers[key]:
                i = current_tier.index(True)
                current_tier[i] = str(tree.get_value())
                if tree.get_left_child():
                    nextTier[2*i] = True
                if tree.get_right_child():
                    nextTier[2*i+1] = True 
            tiers[key] = current_tier
        max_tier = max(tiers)
        lowest_tier = []
        for i,val in enumerate(tiers[max_tier]):
            lowest_tier.append(val)
            if i < len(tiers[max_tier])-1:
                lowest_tier.append(' ')
        all_tier_strs = [lowest_tier]
        skip,hop = 1,4
        for key in sorted(tiers,reverse=True):
            if key != max_tier:
                new_tier = [' ' for i in lowest_tier]
                arrow_tier = new_tier[:]
                tier_index,new_tier_index = 0,skip
                offset = hop//4
                if key != max_tier-1:
                    offset //= 2
                while new_tier_index < len(new_tier):
                    new_tier[new_tier_index] = tiers[key][tier_index]
                    if tiers[key+1][2*tier_index] != ' ':
                        arrow_tier[new_tier_index-offset] = '/'
                    if tiers[key+1][2*tier_index+1] != ' ':
                        arrow_tier[new_tier_index+offset] = '\\'
                    tier_index += 1
                    new_tier_index += hop
                skip = hop - 1
                hop = 2*hop
                all_tier_strs.append(arrow_tier)
                all_tier_strs.append(new_tier)

        out = []
        for t in all_tier_strs:
            out.append(' '.join(t))
        return '\n\n'.join(out[::-1])


# Problem Set 4A
# Name:
# Collaborators:

# from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
maxHeap = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))
# print(maxHeap)

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if type(tree) == Node:
            # print(tree.get_value())
            maxDepth = 0
            if tree.get_left_child() == None and tree.get_right_child() == None:
                return 0
            else:
                lDepth = 0
                rDepth = 0
                if tree.get_left_child() != None:
                    lDepth = find_tree_height(tree.get_left_child())
                if tree.get_right_child() != None:
                    rDepth = find_tree_height(tree.get_right_child())                
                # print(f'left depth: {lDepth}, right depth: {rDepth}')
            return max(lDepth, rDepth) + 1

def is_heap0(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    print(tree.get_value())
    if find_tree_height(tree) == 0:
        return tree.get_value()
    elif find_tree_height(tree) == 1:
        lValue = 0
        rValue = 0
        if tree.get_left_child() != None:
            lValue = is_heap(tree.get_left_child(), compare_func)
        if tree.get_right_child() != None:
            rValue = is_heap(tree.get_right_child(), compare_func)
        print(compare_func(max(lValue, rValue), tree.get_value()))
        return compare_func(max(lValue, rValue), tree.get_value())
    else:
        lValue = 0
        rValue = 0
        if tree.get_left_child() != None:
            lValue = is_heap(tree.get_left_child(), compare_func)
        if tree.get_right_child() != None:
            rValue = is_heap(tree.get_right_child(), compare_func)
        return  compare_func(max(lValue, rValue), tree.get_value())
      
def is_heap(tree, compare_func):
    # print(tree.get_value())
    print(f'tree height {find_tree_height(tree)}, value {tree.get_value()}')
    if find_tree_height(tree) == 0:
        return True #tree.get_value()
    elif find_tree_height(tree) == 1:
        lValue = 0
        rValue = 0
        if tree.get_left_child() != None:
            lValue = tree.get_left_child().get_value()
        if tree.get_right_child() != None:
            rValue = tree.get_right_child().get_value()
        print(f"height 1: value {tree.get_value()}, lvalue: {lValue}, rValue: {rValue}, max: {max(lValue, rValue)}")
        if lValue == False or rValue == False:
            return False
        if lValue == True and rValue == True:
            return True
        return  compare_func(max(lValue, rValue), tree.get_value())
    elif find_tree_height(tree) > 1:
        lValue = 0
        rValue = 0
        if tree.get_left_child() != None:
            lValue = is_heap(tree.get_left_child(), compare_func)
        if tree.get_right_child() != None:
            rValue = is_heap(tree.get_right_child(), compare_func)
        print(f"height {find_tree_height(tree)}: value {tree.get_value()}, lvalue: {lValue}, rValue: {rValue}, max: {max(lValue, rValue)}")
        # print(f'max: {max(lValue, rValue)}')
        if lValue == False or rValue == False:
            return False
        if lValue == True and rValue == True:
            return True
        return  compare_func(max(lValue, rValue), tree.get_value())


def is_heap3(tree, compare_func):
    if find_tree_height(tree) == 0:
        return tree.get_value()
    else:
        ...


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    # print(find_tree_height(tree1))
    # is_heap(tree2, (lambda x,y: x < y))
    print(is_heap(tree3, (lambda x,y: x > y)))
    pass



