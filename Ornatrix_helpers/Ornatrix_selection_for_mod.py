import c4d
import random

def main():

    if not op:
        c4d.gui.MessageDialog('Please select Polygons')
        return
    if not isinstance(op, c4d.PolygonObject):
        c4d.gui.MessageDialog('Please select Polygons!')
        return
    
    bs = op.GetPolygonS()
    selda = bs.GetAll(op.GetPolygonCount())
    if bs.GetCount() < 1: 
        c4d.gui.MessageDialog('Please select Polygons!!')
        return

    seltag = op.MakeTag(c4d.Tpolygonselection)
    seltag.SetName(''.join(['OrnatrixS', str(random.randrange(1, 100))]))
    tag_sel = seltag.GetBaseSelect()
    bs.CopyTo(tag_sel)

    doc.StartUndo()

    orn_ho = c4d.BaseObject(1050340)
    orn_ho.MakeTag(c4d.Tphong)

    orn_gfm = c4d.BaseObject(1050342)
    orn_gfm[c4d.gfm_InputMeshAttribute] = seltag

    orn_edg = c4d.BaseObject(1050454)

    orn_ha = c4d.BaseObject(1050343)
    orn_ha[c4d.hfg_UseFaceIncludeAttribute] = True

    orn_ha.InsertUnder(orn_ho)
    orn_edg.InsertUnder(orn_ho)
    orn_gfm.InsertUnder(orn_ho)

    doc.InsertObject(orn_ho)
    doc.AddUndo(c4d.UNDOTYPE_NEW, orn_ho)
    c4d.EventAdd()

if __name__ == '__main__':
    main()