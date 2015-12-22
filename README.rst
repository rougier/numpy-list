Typed list based on numpy array
===============================

A Numpy array list is a strongly typed list whose type can be anything that can
be interpreted as a numpy data type.

.. code::

   >>> L = ArrayList( [[0], [1,2], [3,4,5], [6,7,8,9]] )
   >>> print(L)
   [ [0] [1 2] [3 4 5] [6 7 8 9] ]
   >>> print(L.data)
   [0 1 2 3 4 5 6 7 8 9]


You can add several items at once by specifying common or individual size: a
single scalar means all items are the same size while a list of sizes is used
to specify individual item sizes.


.. code::

   >>> L = ArrayList( np.arange(10), [3,3,4])
   >>> print(L)
   [ [0 1 2] [3 4 5] [6 7 8 9] ]
   >>> print(L.data)
   [0 1 2 3 4 5 6 7 8 9]

You can also us typed list for storing strings with different sizes:

.. code::

   >>> L = ArrayList(["Hello", "world", "!"])
   >>> print(L[0])
   'Hello'
   >>> L[1] = "brave new world"
   >>> print(L)
   ['Hello', 'brave new world', '!']
   
