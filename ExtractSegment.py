import c4d
from c4d import utils

def main():
    target = doc.GetActiveObject()    
    if not target: return
    if target.GetType() != 5101: return    
    settings = c4d.BaseContainer()    
    ctar = target.GetClone(0)    
    res = utils.SendModelingCommand(command = c4d.MCOMMAND_SPLINE_BREAKSEGMENT,
                                list = [ctar],
                                mode = c4d.MODELINGCOMMANDMODE_POINTSELECTION,
                                bc = settings,
                                doc = doc)
    ctar.Message(c4d.MSG_UPDATE)
    res = utils.SendModelingCommand(command = c4d.MCOMMAND_SELECTINVERSE,
                                list = [ctar],
                                mode = c4d.MODELINGCOMMANDMODE_POINTSELECTION,
                                bc = settings,
                                doc = doc)
    ctar.Message(c4d.MSG_UPDATE)
    res = utils.SendModelingCommand(command = c4d.MCOMMAND_DELETE,
                                list = [ctar],
                                mode = c4d.MODELINGCOMMANDMODE_POINTSELECTION,
                                bc = settings,
                                doc = doc)                                
    c4d.EventAdd()
    ctar[c4d.SPLINEOBJECT_CLOSED]=False
    doc.InsertObject(ctar)
if __name__=='__main__':
    main()
