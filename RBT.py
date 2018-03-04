class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'

class Solution:
    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            if x.key != 0:
                print ('key:', x.key, 'parent:', x.parent.key, 'color:', x.color)
            self.InorderTreeWalk(x.right)

    def LeftRotate(self, T, x):
        '''左旋将左图转为右图
            |       O          |     |            O         |
            |    X             |     |         U            |
            | a     U          | --> |      X    c          |
            |     b   c        |     |    a   b             |

        #a， c 都可以不用动 ，先将b和X构造关系，主要要相互赋值（x的right为b，b的parent为x）。
        '''
        y = x.right                 #可以理解为：依次构造X和b、U和O、U和X的关系
        x.right = y.left
        if y.left != T.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right          #和左旋操作相反。
        if y.right != T.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def RBInsert(self, T, z):
        # init z
        z.left = T.nil
        z.right = T.nil
        z.parent = T.nil

        y = T.nil
        x = T.root
        while x != T.nil:           #在while循环中，可以看作是按z的key值先找到树T的底部节点并存为y。
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y                #以下步骤就是按z的key值与y做相互链接，并将z上色。
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = 'red'
        self.RBInsertFixup(T,z)      #调用Fixup将z进行操作放至合理位置。

    def RBInsertFixup(self, T, z):
        while z.parent.color == 'red':           #当z的父节点为红色时
            if z.parent == z.parent.parent.left:    #如果z的父节点在左边
                y = z.parent.parent.right               #先将z的叔节点存储
                if y.color == 'red':                    #如果z的叔节点为红色
                    z.parent.color = 'black'                #将z的父节点改为黑色
                    y.color = 'black'                       #将z的叔节点改为黑色
                    z.parent.parent.color = 'red'           #将z的祖父节点改为红色
                    z = z.parent.parent                     #将z的祖父节点赋值给z
                else:                                   #如果z的叔节点为黑色
                    if z == z.parent.right:                 #如果z节点在右边
                        z = z.parent                            #将z的父节点赋值给z
                        self.LeftRotate(T, z)                   #对z节点进行左旋操作
                    z.parent.color = 'black'                #将z的父节点改为黑色
                    z.parent.parent.color = 'red'           #将z的祖父机诶但改为红色
                    self.RightRotate(T,z.parent.parent)     #对z节点进行右旋操作
            else:                                   #如果z的父节点在右边，操作相反。
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.LeftRotate(T, z.parent.parent)
        T.root.color = 'black'

    def RBTransplant(self, T, u, v):
        if u.parent == T.nil:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBDelete(self, T, z):
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.RBTransplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.RBTransplant(T, z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(T, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(T, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.RBDeleteFixup(T, x)

    def RBDeleteFixup(self, T, x):
        while x != T.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.LeftRotate(T, x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.RightRotate(T, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.LeftRotate(T, x.parent)
                    x = T.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.RightRotate(T, x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.LeftRotate(T, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.RightRotate(T, x.parent)
                    x = T.root
        x.color = 'black'

    def TreeMinimum(self, x):
        while x.left != T.nil:
            x = x.left
        return x

nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
s = Solution()
for node in nodes:
    s.RBInsert(T,RBTreeNode(node))

s.InorderTreeWalk(T.root)

s.RBDelete(T,T.root)
print ('after delete')
s.InorderTreeWalk(T.root)