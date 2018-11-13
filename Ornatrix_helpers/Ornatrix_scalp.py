import c4d

def main():
    
    if not op or not op.CheckType(c4d.Opolygon):
        c4d.gui.MessageDialog('Please select Polygons')
        
    points = op.GetAllPoints()
    polys = op.GetAllPolygons()
    sel = op.GetPolygonS()
    new_polys = []
    
    for i, v in enumerate(sel.GetAll(len(polys))):
        if not v:
            continue
        new_polys.append(polys[i])

    obj = c4d.PolygonObject(len(points), len(new_polys))

    obj.SetAllPoints(points)

    for i, p in enumerate(new_polys):
            obj.SetPolygon(i, p)
            
    if obj:
        settings = c4d.BaseContainer()
        settings[c4d.MDATA_OPTIMIZE_UNUSEDPOINTS] = True
        settings[c4d.MDATA_OPTIMIZE_POINTS] = False
        settings[c4d.MDATA_OPTIMIZE_POLYGONS] = False
        opt = c4d.utils.SendModelingCommand(command = c4d.MCOMMAND_OPTIMIZE,
                                            list = [obj],
                                            mode =c4d.MODELINGCOMMANDMODE_ALL,
                                            bc = settings,
                                            doc = doc)
        op.CopyTagsTo(obj, True, True, False)
        obj.Message(c4d.MSG_UPDATE)
        if opt:
            doc.StartUndo()            
            obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
            obj.SetName('Scalp')            
            obj.InsertUnder(op)
            ornatrix = c4d.BaseObject(1040603)
            orn_tags = ornatrix.MakeTag(1040939), ornatrix.MakeTag(1040609), ornatrix.MakeTag(1040610), ornatrix.MakeTag(1040608), ornatrix.MakeTag(c4d.Tphong)
            ornatrix[c4d.ho_MeshLink] = obj
            doc.InsertObject(ornatrix)
            doc.AddUndo(c4d.UNDOTYPE_NEW, ornatrix)
            doc.AddUndo(c4d.UNDOTYPE_NEW, obj)
            doc.EndUndo()
            c4d.EventAdd()

if __name__ == '__main__':
    main()