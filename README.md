# PythonUnionFind
UnionFind DataStructure with path compression and union by rank for near-linear union and find operations

## Installation
-Fastest would be to copy-paste the contents of UnionFind.py into your code

-Or you could download UnionFind.py and throw it in your project directory. Use "from DisjointSet import *" to use it in your code

-You could clone https://github.com/asawitt/PythonUnionFind/ , move UnionFind.py to your project directory, then use the above import statement if you really want to. Don't. 

## Usage
### Create a new DisjointSet
sets = UnionFind()
### MakeSet
-Makes a new set with value x, if x is not currently in the data-structure
sets.make_set(x)

### Finds root of x if it exists, else None
sets.find(x)
### Union(x,y)
-combines set that contains x with the set that contains y
-if x or y is not in the datastructure, does nothing

sets.union(x,y)



## License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

