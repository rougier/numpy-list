# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    import numpy as np
    from array_list import ArrayList

    L = ArrayList(np.arange(10), itemsize=1)
    for item in L: print(item)
    print(L.data)
    print()
    

    L = ArrayList([[0], [1,2], [3,4,5], [6,7,8,9]])
    for item in L:print(item)
    print(L.data)
