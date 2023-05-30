import PyVMAP as VMAP 
import vedo as v

class VMAPMeshReader:
    elemTypes = {}
    points = []
    elements = []
    pointIDs = {}
    
    def __init__(self):
        pass
        
    def setPoints(self, points):
        self.points = points
        
    def setIDs(self, ids):
        #self.ids = ids
        self.pointIDs = {id: i for i, id in enumerate(ids)}
        #print(self.pointIDs)
    
    def setElements(self, elements):
        self.elements = elements
        
    def setElementTypes(self, elemTypes):
        #self.elemTypes = elemTypes
        self.elemTypes = {elem[0]: elem[5] for i, elem in enumerate(elemTypes)}
        #print(self.elemTypes)
        
    def getPointIndexFromID(self, id):
        return self.pointIDs[id]
        #return self.points[id-1]
        
    def getPointFromID(self, id):
        return self.points[self.pointIDs[id]]
        #return self.coordinates[id-1]
        
    def getPointsFromElement(self, elem, ids):
        return [self.getPointIndexFromID(elem[5][i]) for i in ids]
    
    def getMesh(self):
        faces = []
        tets = []
        for elem in self.elements:
            elemType = self.elemTypes[elem[1]]
            print(elemType)
            if elemType in [VMAP.sElementType.TRIANGLE_3, VMAP.sElementType.TRIANGLE_4, VMAP.sElementType.TRIANGLE_6]:
                #faces.append([self.getPointIndexFromID(elem[5][i]) for i in [0, 1, 2]])
                faces.append(self.getPointsFromElement(elem, [0, 1, 2]))
            elif elemType in [VMAP.sElementType.QUAD_4, VMAP.sElementType.QUAD_8, VMAP.sElementType.QUAD_9]:
                #faces.append([self.getPointIndexFromID(elem[5][i]) for i in [0, 1, 2, 3]])
                faces.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
            elif elemType in [VMAP.sElementType.TETRAHEDRON_4, VMAP.sElementType.TETRAHEDRON_5, VMAP.sElementType.TETRAHEDRON_10, VMAP.sElementType.TETRAHEDRON_11]:
                #tets.append([self.getPointIndexFromID(elem[5][i]) for i in [0, 1, 2, 3]])
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
            elif elemType in [VMAP.sElementType.PYRAMID_5, VMAP.sElementType.PYRAMID_6,VMAP.sElementType.PYRAMID_13]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 4]))
                tets.append(self.getPointsFromElement(elem, [0, 2, 3, 4]))
            elif elemType in [VMAP.sElementType.HEXAHEDRON_8, VMAP.sElementType.HEXAHEDRON_9, VMAP.sElementType.HEXAHEDRON_20, VMAP.sElementType.HEXAHEDRON_21, VMAP.sElementType.HEXAHEDRON_27]:
                #faces.append([self.getPointIndexFromID(elem[5][i]) for i in [0, 1, 2, 3]])
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 5]))
                tets.append(self.getPointsFromElement(elem, [0, 2, 3, 7]))
                tets.append(self.getPointsFromElement(elem, [0, 4, 5, 7]))
                tets.append(self.getPointsFromElement(elem, [2, 5, 6, 7]))
                tets.append(self.getPointsFromElement(elem, [1, 3, 4, 6]))
            elif elemType in [VMAP.sElementType.WEDGE_6, VMAP.sElementType.WEDGE_15]:
                tets.append(self.getPointsFromElement(elem, [0, 1, 2, 3]))
                tets.append(self.getPointsFromElement(elem, [2, 3, 4, 5]))
                tets.append(self.getPointsFromElement(elem, [1, 2, 3, 4]))
            #elif elemType == VMAP.sElementType.TRIANGLE_6:
            #    raise NotImplementedError("Element type not imlemented: {} in element #{}".format(elemType, elem[0]))
            #elif elemType == VMAP.sElementType.TRIANGLE_6:
            #    raise NotImplementedError("Element type not imlemented: {} in element #{}".format(elemType, elem[0]))
            
            else:
                raise NotImplementedError("Element type not imlemented: {} in element #{}".format(elemType, elem[0]))
        mesh = v.Mesh([self.points, faces]).c("red").alpha(1).lw(1) if len(faces) > 0 else v.TetMesh([self.points, tets], mapper='tetra').tomesh(fill=False).c("red").alpha(1)
        #mesh = v.Mesh([self.points, faces]).c("red").alpha(1).lw(1)
        #tetMesh = v.TetMesh([self.points, tets]).c("red").alpha(1) if len(tets) > 0 else v.Cube()
        pcld = v.Points(self.points, c="blue").ps(3)
        #mesh = v.merge(mesh, tetMesh)
        return mesh, pcld#mesh
            
        
        