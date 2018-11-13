import c4d
import random

def hfg_UseFace(op):
    tag = c4d.BaseTag(1040609)
    tag[c4d.hfg_UseFaceIncludeAttribute] = True
    return op.InsertTag(tag)

def main():

    if not op:
        c4d.gui.MessageDialog('Please select Polygons')

    bs = op.GetPolygonS()
    selda = bs.GetAll(op.GetPolygonCount())
    if bs.GetCount() < 1: return

    seltag = op.MakeTag(c4d.Tpolygonselection)
    seltag.SetName(''.join(['OrnatrixS', str(random.randrange(1, 100))]))
    tag_sel = seltag.GetBaseSelect()
    bs.CopyTo(tag_sel)

    doc.StartUndo()
    ornatrix = c4d.BaseObject(1040603)

    orn_tags = ornatrix.MakeTag(1040939), hfg_UseFace(ornatrix), ornatrix.MakeTag(1040610), ornatrix.MakeTag(1040608), ornatrix.MakeTag(c4d.Tphong)
    ornatrix[c4d.ho_MeshLink] = seltag
    doc.InsertObject(ornatrix)
    doc.AddUndo(c4d.UNDOTYPE_NEW, ornatrix)
    c4d.EventAdd()

if __name__ == '__main__':
    main()