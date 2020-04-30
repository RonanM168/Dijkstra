class Element:
    """ A key, value and index. """

    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None


class APQ:
    #initialising the array based apq body and a dicitonary used for lookup of each elements index
    def __init__(self):
        self._body = []
        self._dict = {}

    #add a new element with key and item as the elements key and value and bubble the item up the binary heap
    def add(self, key, item):
        new_element = Element(key, item, self.length())
        self._body.append(new_element)
        self.bubble_up(self._body, new_element._index)
        self._dict[item] = new_element._index
        return new_element

    #return the element at the top of the binary heap
    def min(self):
        return self._body[0]._value

    #remove the item at the top of the heap, replace it with the last element in the heap and rebalance
    def remove_min(self):
        if self.length() == 1:
            temp = self._body[0]
            self._body.pop(-1)
            self._dict.pop(temp._value)
        else:
            temp = self._body[0]
            self._body[0] = self._body[-1]
            self._body.pop(-1)
            self._body[0]._index = 0
            self.bubble_down(self._body, 0, self.length())
            self._dict.pop(temp._value)
        return temp._key, temp._value

    #bubble the item up the heap into the correct position
    def bubble_up(self, mylist, myindex):
        # swapping the value at myindex with its parent as long as its parent has a value less than its own
        while (myindex - 1) // 2 >= 0 and mylist[myindex]._key < mylist[(myindex - 1) // 2]._key:
            mylist[myindex]._index, mylist[(myindex - 1) // 2]._index = mylist[(myindex - 1) // 2]._index, mylist[
                myindex]._index
            self._dict[mylist[myindex]._value] = mylist[myindex]._index
            self._dict[mylist[(myindex - 1) // 2]._value] = mylist[(myindex - 1) // 2]._index
            mylist[myindex], mylist[(myindex - 1) // 2] = mylist[(myindex - 1) // 2], mylist[myindex]
            self.bubble_up(mylist, (myindex - 1) // 2)
        # returning the list
        return mylist

    #bubble the item down the heap into the correct position
    def bubble_down(self, mylist, myindex, heap_size):
        # checking the value is not on the lowest level of the heap
        if (2 * myindex) + 1 < heap_size:
            #checking if the value has two children
            if (2 * myindex) + 2 < heap_size:
                #swapping the value with the correct child accordingly
                if mylist[myindex]._key > mylist[(2 * myindex) + 1]._key and mylist[myindex]._key > mylist[
                    (2 * myindex) + 2]._key:
                    if mylist[(2 * myindex) + 1]._key > mylist[(2 * myindex) + 2]._key:
                        mylist[myindex]._index, mylist[(2 * myindex) + 2]._index = mylist[(2 * myindex) + 2]._index, \
                                                                                   mylist[myindex]._index
                        self._dict[mylist[myindex]._value] = mylist[myindex]._index
                        self._dict[mylist[(2 * myindex) + 2]._value] = mylist[(2 * myindex) + 2]._index
                        mylist[myindex], mylist[(2 * myindex) + 2] = mylist[(2 * myindex) + 2], mylist[myindex]
                        self.bubble_down(mylist, (2 * myindex) + 2, heap_size)
                    else:
                        mylist[myindex]._index, mylist[(2 * myindex) + 1]._index = mylist[(2 * myindex) + 1]._index, \
                                                                                   mylist[myindex]._index
                        self._dict[mylist[myindex]._value] = mylist[myindex]._index
                        self._dict[mylist[(2 * myindex) + 1]._value] = mylist[(2 * myindex) + 1]._index
                        mylist[myindex], mylist[(2 * myindex) + 1] = mylist[(2 * myindex) + 1], mylist[myindex]
                        self.bubble_down(mylist, (2 * myindex) + 1, heap_size)
                elif mylist[myindex]._key > mylist[(2 * myindex) + 1]._key and mylist[myindex]._key < mylist[
                    (2 * myindex) + 2]._key:
                    mylist[myindex]._index, mylist[(2 * myindex) + 1]._index = mylist[(2 * myindex) + 1]._index, mylist[
                        myindex]._index
                    self._dict[mylist[myindex]._value] = mylist[myindex]._index
                    self._dict[mylist[(2 * myindex) + 1]._value] = mylist[(2 * myindex) + 1]._index
                    mylist[myindex], mylist[(2 * myindex) + 1] = mylist[(2 * myindex) + 1], mylist[myindex]
                    self.bubble_down(mylist, (2 * myindex) + 1, heap_size)
                elif mylist[myindex]._key < mylist[(2 * myindex) + 1]._key and mylist[myindex]._key > mylist[
                    (2 * myindex) + 2]._key:
                    mylist[myindex]._index, mylist[(2 * myindex) + 2]._index = mylist[(2 * myindex) + 2]._index, mylist[
                        myindex]._index
                    self._dict[mylist[myindex]._value] = mylist[myindex]._index
                    self._dict[mylist[(2 * myindex) + 2]._value] = mylist[(2 * myindex) + 2]._index
                    mylist[myindex], mylist[(2 * myindex) + 2] = mylist[(2 * myindex) + 2], mylist[myindex]
                    self.bubble_down(mylist, (2 * myindex) + 2, heap_size)
            #checking if the value has one child and swapping with it if its key is greater than its own
            elif mylist[myindex]._key > mylist[(2 * myindex) + 1]._key:
                mylist[myindex]._index, mylist[(2 * myindex) + 1]._index = mylist[(2 * myindex) + 1]._index, mylist[
                    myindex]._index
                self._dict[mylist[myindex]._value] = mylist[myindex]._index
                self._dict[mylist[(2 * myindex) + 1]._value] = mylist[(2 * myindex) + 1]._index
                mylist[myindex], mylist[(2 * myindex) + 1] = mylist[(2 * myindex) + 1], mylist[myindex]
                self.bubble_down(mylist, (2 * myindex) + 1, heap_size)

        # returning the list
        return mylist

    #returning the length of the apq body
    def length(self):
        return len(self._body)

    #returning true if the apq is empty
    def is_empty(self):
        return self.length() == 0

    #udating the key of the element in the apq body by using the dicitonary lookup to find the element by its value
    def update_key(self, element, newkey):
        element_index = self._dict[element]
        self._body[element_index]._key = newkey
        if (element_index - 1) // 2 >= 0 and self._body[element_index]._key < self._body[(element_index - 1) // 2]._key:
            self.bubble_up(self._body, element_index)
        else:
            self.bubble_down(self._body, element_index, self.length())

    #returning the key of the element
    def get_key(self, element):
        return self._dict[element]

    #removing the element and rebalancing the heap
    def remove(self, element):
        element_index = self._dict[element]
        if self._body[element_index] == self._body[-1]:
            temp = self._body[-1]
        else:
            temp = self._body[element_index]
            self._body[element_index] = self._body[-1]
            self.bubble_down(self._body, element_index, self.length())
        self._body.pop(-1)
        self._dict.pop(element)
        return temp._key, temp._value


class Vertex:
    """ A Vertex in a graph. """

    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element


class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """

    def __init__(self, v, w, element):
        """ Create an edge between vertice v and w, with label element.

            element can be an arbitrarily complex structure.
        """
        self._vertices = (v, w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element


class Graph1:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edges for the corresponding vertex
    #   Each edge set is also maintained as a dictionary,
    #   with opposite vertex as the key and the edge object as the value

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    # --------------------------------------------------#
    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the

    # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure != None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    # --------------------------------------------------#
    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

            Checks for equality between the elements. If there is special
            meaning to parts of the element (e.g. element is a tuple, with an
            'id' in cell 0), then this method may create multiple vertices with
            the same 'id' if any other parts of element are different.

            To ensure vertices are unique for individual parts of element,
            separate methods need to be written.
        """
        for v in self._structure:
            if v.element() == element:
                # print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

            If either v or w are not vertices in the graph, does not add, and
            returns None.

            If an edge already exists between v and w, this will
            replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements. """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    #implementing dijkstras algorithm to find the shortest path between a vertex and each other vertex
    def dijkstra(self, s):
        #getting the vertex from its label
        s = self.get_vertex_by_label(s)

        #intialising the data structures
        self._open = APQ()
        self._locs = {}
        self._closed = {}
        self._preds = {}

        #setting the predecessor for the input vertex to be None
        self._preds[s] = None

        #adding the vertex to the apq of open vertices
        s = self._open.add(0, s)

        #ading the vertex to locs with its value as its index in the apq
        self._locs[s._value] = s._index

        #while there are open vertices
        while self._open.length() != 0:
            #remove the minimum vertex in the apq
            v = self._open.remove_min()
            #removing this vertx from locs and preds
            self._locs.pop(v[1])
            vpred = self._preds.pop(v[1])
            #adding the vertex into closed with its value as a tuple of its cost and predecessor
            if vpred:
                self._closed[v[1]._element] = (v[0], vpred._element)
            else:
                self._closed[v[1]._element] = (v[0], None)
            #checking all outgoing edges from the current vertex
            for e in self.get_edges(v[1]):
                #checking each edge connected to the current vertex
                w = e.opposite(v[1])
                #checking if these vertices are in closed
                if w._element not in self._closed.keys():
                    #increasing the cost by the weight of the edge
                    newcost = v[0] + e._element
                    #updating the details of this vertex in preds and locs
                    if w not in self._locs.keys():
                        self._preds[w] = v[1]
                        w = self._open.add(newcost, w)
                        self._locs[w._value] = w._index
                    elif newcost < self._open.get_key(w):
                        self._preds[w] = v[1]
                        self._open.update_key(w, newcost)
        #returning the dicitonary
        return self._closed


def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph1()
    file = open(filename, 'r')
    entry = file.readline()  # either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline()  # read the one-way data
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph

class Graph2:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edges for the corresponding vertex
    #   Each edge set is also maintained as a dictionary,
    #   with opposite vertex as the key and the edge object as the value

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()
        #creating a dicoinary which can be used to look up the vertex using its element
        self._vertex_lookup = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    # --------------------------------------------------#
    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the

    # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        vertex = self._vertex_lookup[element]
        if vertex:
            return vertex
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure != None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    # --------------------------------------------------#
    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        self._vertex_lookup[v._element] = v
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

            Checks for equality between the elements. If there is special
            meaning to parts of the element (e.g. element is a tuple, with an
            'id' in cell 0), then this method may create multiple vertices with
            the same 'id' if any other parts of element are different.

            To ensure vertices are unique for individual parts of element,
            separate methods need to be written.
        """
        for v in self._structure:
            if v.element() == element:
                # print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

            If either v or w are not vertices in the graph, does not add, and
            returns None.

            If an edge already exists between v and w, this will
            replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements. """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    #implementing dijkstras algorithm to find the shortest path between a vertex and each other vertex
    def dijkstra(self, s):
        #getting the vertex from its label
        s = self.get_vertex_by_label(s)

        #intialising the data structures
        self._open = APQ()
        self._locs = {}
        self._closed = {}
        self._preds = {}

        #setting the predecessor for the input vertex to be None
        self._preds[s] = None

        #adding the vertex to the apq of open vertices
        s = self._open.add(0, s)

        #ading the vertex to locs with its value as its index in the apq
        self._locs[s._value] = s._index

        #while there are open vertices
        while self._open.length() != 0:
            #remove the minimum vertex in the apq
            v = self._open.remove_min()
            #removing this vertx from locs and preds
            self._locs.pop(v[1])
            vpred = self._preds.pop(v[1])
            #adding the vertex into closed with its value as a tuple of its cost and predecessor
            if vpred:
                self._closed[v[1]._element] = (v[0], vpred._element)
            else:
                self._closed[v[1]._element] = (v[0], None)
            #checking all outgoing edges from the current vertex
            for e in self.get_edges(v[1]):
                #checking each edge connected to the current vertex
                w = e.opposite(v[1])
                #checking if these vertices are in closed
                if w._element not in self._closed.keys():
                    #increasing the cost by the weight of the edge
                    newcost = v[0] + e._element
                    #updating the details of this vertex in preds and locs
                    if w not in self._locs.keys():
                        self._preds[w] = v[1]
                        w = self._open.add(newcost, w)
                        self._locs[w._value] = w._index
                    elif newcost < self._open.get_key(w):
                        self._preds[w] = v[1]
                        self._open.update_key(w, newcost)
        #returning the dicitonary
        return self._closed


class Routemap(object):
    def __init__(self):
        #initialising the graph and the dictionary used to hold the coordinates of each vertex
        self._graph = Graph2()
        self._vertex_coord = {}

    #returning a list which returns the vertices and predeessors for each step along the path between two vertices
    def sp(self, v, w):
        closed = self._graph.dijkstra(v)
        result = []
        while closed[w][1] != v:
            result.append((w, closed[w]))
            w = closed[w][1]
        result.append((w, closed[w]))
        result.reverse()
        return result

    #printing out the formatted shortest path between two vertices
    def printPath(self, path):
        for vertex in path:
            vertex_id = vertex[0]
            coordx = self._vertex_coord[vertex_id][0]
            coordy = self._vertex_coord[vertex_id][1]
            cost = vertex[1][0]

            print("W\t%.6f\t%.6f\t%d\t%.1f" % (coordx, coordy, vertex_id, cost))

    #printing the routemap
    def __str__(self):
        if self._graph.num_edges() < 100 and self._graph.num_vertices() < 100:
            x = str(self._graph)
            return x
        else:
            return ""


def graphreader2(filename):
    """ Read and return the route map in filename. """
    routemap = Routemap()
    file = open(filename, 'r')
    entry = file.readline()  # either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = routemap._graph.add_vertex(nodeid)
        coords = (file.readline().split(': ')[1])
        coordx = float(coords.split()[0])
        coordy = float(coords.split()[1])
        routemap._vertex_coord[nodeid] = (coordx, coordy)
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = routemap._graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = routemap._graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        time = float(file.readline().split()[1])
        edge = routemap._graph.add_edge(sv, tv, time)
        file.readline()  # read the one-way data
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(routemap)
    return routemap


#testing the implementation
routemap = graphreader2('corkCityData.txt')
ids = {}
ids['wgb'] = 1669466540
ids['turnerscross'] = 348809726
ids['neptune'] = 1147697924
ids['cuh'] = 860206013
ids['oldoak'] = 358357
ids['gaol'] = 3777201945
ids['mahonpoint'] = 330068634
sourcestr1 = 'wgb'
deststr1='neptune'
source1 = ids[sourcestr1]
dest1 = ids[deststr1]
tree1 = routemap.sp(source1,dest1)
sourcestr2 = 'oldoak'
deststr2='cuh'
source2 = ids[sourcestr2]
dest2 = ids[deststr2]
tree2 = routemap.sp(source2,dest2)
sourcestr3 = 'gaol'
deststr3='mahonpoint'
source3 = ids[sourcestr3]
dest3 = ids[deststr3]
tree3 = routemap.sp(source3,dest3)
print("\nPath from Western Gateway Building to Neptune")
routemap.printPath(tree1)
print("\nPath from Old Oak to Cork University Hospital")
routemap.printPath(tree2)
print("\nPath from Cork City Gaol to Mahon Point")
routemap.printPath(tree3)
