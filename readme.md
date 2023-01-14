# Automated Farming Route Tractor - Bat Mobile

Team Members :
1. Tan Yong Le s2164472
2. Boon Yin Yin s2149527
3. Darkhan Baibulat s2172558
4. Xue Bai s2116024
5. Liow Gian Hao s2178227

Our project is to assemble an autonomous driving car that is able to help with pesticide control in a
farm. The car will be able to traverse from the location of one crop to another in the shortest distance
possible. The algorithm that we are using to find the shortest distance is a path finding algorithm
called Floyd–Warshall.
Below shows an example of the farm and its distance matrix:

![Farm_example](https://github.com/tyl1999tyl/BatMobile/blob/main/images/example_farm.png)

- The numbers in dark purple and circled are the nodes (a.k.a location of the crops). They are the
location that the robot car needs to reach.
- The numbers in red are the distances.
- The black lines are the path.
A demo of the algorithm in working is in floyd_warshall_demo.py. The distance matrix is inserted
and when the algorithm is run, we can get the shortest path that the robot needs to go through to get
from node A to node B. Example output:

```

The shortest path from 1 -> 2 is [1, 2] 
The shortest path from 1 -> 3 is [1, 2, 3]
The shortest path from 1 -> 4 is [1, 2, 3, 4]
The shortest path from 1 -> 5 is [1, 2, 3, 4, 5]
The shortest path from 1 -> 6 is [1, 2, 3, 4, 6]
The shortest path from 1 -> 7 is [1, 2, 9, 8, 7]
The shortest path from 1 -> 8 is [1, 2, 9, 8]
The shortest path from 1 -> 9 is [1, 2, 9]
The shortest path from 1 -> 10 is [1, 2, 9, 10]

```


