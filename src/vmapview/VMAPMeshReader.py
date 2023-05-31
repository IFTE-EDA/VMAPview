import vedo as v
from enum import Enum

class VMAPMeshReader:
    elemTypes = {}
    points = []
    elements = []
    pointIDs = {}
    
    #Shape = Enum('Shape', "SHAPE_INVALID POINT LINE_2 LINE_3 LINE_4 TRIANGLE_3 TRIANGLE_4 TRIANGLE_6 QUAD_4 QUAD_8 QUAD_9 TETRAHEDRON_4 TETRAHEDRON_5 TETRAHEDRON_10 TETRAHEDRON_11 PYRAMID_5 PYRAMID_6 PYRAMID_13 WEDGE_6 WEDGE_15 HEXAHEDRON_8 HEXAHEDRON_9 HEXAHEDRON_20 HEXAHEDRON_21 HEXAHEDRON_27 POLYGON POLYHEDRON USER_DEFINED")
    
    class Shape:
        SHAPE_INVALID = 0
        POINT = 1
        LINE_2 = 2
        LINE_3 = 3
        LINE_4 = 4
        TRIANGLE_3 = 5
        TRIANGLE_4 = 6
        TRIANGLE_6 = 7
        QUAD_4 = 8
        QUAD_8 = 9
        QUAD_9 = 10
        TETRAHEDRON_4 = 11
        TETRAHEDRON_5 = 12
        TETRAHEDRON_10 = 13
        TETRAHEDRON_11 = 14
        PYRAMID_5 = 15
        PYRAMID_6 = 16
        PYRAMID_13 = 17
        WEDGE_6 = 18
        WEDGE_15 = 19
        HEXAHEDRON_8 = 20
        HEXAHEDRON_9 = 21
        HEXAHEDRON_20 = 22
        HEXAHEDRON_21 = 23
        HEXAHEDRON_27 = 24
        POLYGON = 25
        POLYHEDRON = 26
        USER_DEFINED = 27
    
    
    def __init__(self):
        pass
        
    def setPoints(self, points):
        self.points = points
        
    def setIDs(self, ids):
        self.pointIDs = {id: i for i, id in enumerate(ids)}
    
    def setElements(self, elements):
        self.elements = elements
        
    def setElementTypes(self, elemTypes):
        self.elemTypes = {elem[0]: elem[5] for i, elem in enumerate(elemTypes)}
        
    def getPointIndexFromID(self, id):  #TODO: test for easier adressing via i=id-1
        return self.pointIDs[id]
        
    def getPointFromID(self, id):
        return self.points[self.pointIDs[id]]
        
    def getPointsFromElement(self, elem, ids):
        return [self.getPointIndexFromID(elem[5][i]) for i in ids]
    
    def getMesh(self):
        faces = []
        tets = []
        for elem in self.elements:
            elemType = self.elemTypes[elem[1]]
            if elemType in [self.Shape.TRIANGLE_3, self.Shape.TRIANGLE_4, self.Shape.TRIANGLE_6]:
                faces.append(self.getPointsFromElement(elem, [0, 1, 2]))
            elif elemType in [self.Shape.QUAD_4, self.Shape.QUAD_8, self.Shape.QUAD_9]:
                faces.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
            elif elemType in [self.Shape.TETRAHEDRON_4, self.Shape.TETRAHEDRON_5, self.Shape.TETRAHEDRON_10, self.Shape.TETRAHEDRON_11]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
            elif elemType in [self.Shape.PYRAMID_5, self.Shape.PYRAMID_6,self.Shape.PYRAMID_13]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 4]))
                tets.append(self.getPointsFromElement(elem, [0, 2, 3, 4]))
            elif elemType in [self.Shape.HEXAHEDRON_8, self.Shape.HEXAHEDRON_9, self.Shape.HEXAHEDRON_20, self.Shape.HEXAHEDRON_21, self.Shape.HEXAHEDRON_27]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 5]))
                tets.append(self.getPointsFromElement(elem, [0, 2, 3, 7]))
                tets.append(self.getPointsFromElement(elem, [0, 4, 5, 7]))
                tets.append(self.getPointsFromElement(elem, [2, 5, 6, 7]))
                tets.append(self.getPointsFromElement(elem, [1, 3, 4, 6]))
            elif elemType in [self.Shape.WEDGE_6, self.Shape.WEDGE_15]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
                tets.append(self.getPointsFromElement(elem, [2, 3, 4, 5]))
                tets.append(self.getPointsFromElement(elem, [1, 2, 3, 4]))
            else:
                raise NotImplementedError("Element type not imlemented: {} in element #{}".format(elemType, elem[0]))
        mesh = v.Mesh([self.points, faces]).c("red").alpha(1).lw(1) if len(faces) > 0 else v.TetMesh([self.points, tets], mapper='tetra').tomesh(fill=False).c("red").alpha(1)
        pcld = v.Points(self.points, c="blue").ps(3)
        return mesh, pcld#mesh
            
        
        