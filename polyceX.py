import c4d
from c4d import gui, utils

# poly_center(op, polygon) from Niklas Rosenstein
def poly_center(op, polygon):
    # Determine whether you passed an index or a Polygon object
    if not isinstance(polygon, c4d.CPolygon):
        polygon = op.GetPolygon(polygon)
    indices = [polygon.a, polygon.b, polygon.c]
    # Determine whether the polygon is a triangle or a quadrangle
    if polygon.c != polygon.d:
        indices.append(polygon.d)
    # Gather a list of the points' Vectors
    vectors = map(lambda i: op.GetPoint(i), indices)
    # Compute the average of the Vectors
    return sum(vectors) / len(vectors)

def main():
    if not op : return
    maxPolyCnt = op.GetPolygonCount()
    maxPointCnt = op.GetPointCount()
    gm=op.GetMg()    
    bcdt = c4d.BaseContainer()
    bcdt[c4d.MDATA_DISCONNECT_PRESERVEGROUPS] = False
    doc.StartUndo() 
    disk = utils.SendModelingCommand(c4d.MCOMMAND_DISCONNECT, list = [op], mode = 2, bc=bcdt, doc = doc)
    if disk:        
        utils.SendModelingCommand(c4d.MCOMMAND_EXPLODESEGMENTS, list = [op], doc = doc)
        triopch = op.GetChildren()
        bc = c4d.BaseContainer()
        for i in xrange(len(triopch)):
            bc[c4d.MDATA_ADDPOINT_POINT] = gm.Mul(poly_center(triopch[i], 0)) 
            utils.SendModelingCommand(c4d.ID_MODELING_POINT_ADD_TOOL, list = [triopch[i]], mode = 2, bc=bc, doc = doc)
        c4d.CallCommand(100004768) # Select Children
        c4d.CallCommand(16768) # Connect Objects + Delete
        c4d.CallCommand(14039) # Optimize...
        op.Message(c4d.MSG_UPDATE)        
        c4d.EventAdd()
    doc.EndUndo() 
if __name__=='__main__':
    main()
