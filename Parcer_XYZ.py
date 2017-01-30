import c4d
from c4d import storage, gui

def ParseXYZ():
    select = storage.LoadDialog(title="Select the *.txt file.")
    if not select: return

    try:
        fn = open(select)
    except IOError, e:
        gui.MessageDialog(e)
        return
    
    #split the file into line list
    lines = fn.readlines()
    
    #how many lines? so points
    count = len(lines)
    
    #create polygon object with point count of lines
    mypoly = c4d.PolygonObject(pcnt=count, vcnt=1)
        
    mypoly.ResizeObject(((count) + 1) * 4, (count) + 1)
    
    for i, line in enumerate(lines):
        #split line into components
        coord = line.split(",")
        #ignore corrupt line
        if len(coord)<3: continue
        
        try:
            x = float(coord[0])
            y = float(coord[1])
            z = float(coord[2])
            
            p0 = 0 + (i*4)
            p1 = 1 + (i*4)
            p2 = 2 + (i*4)
            p3 = 3 + (i*4)

            mypoly.SetPoint(p0, c4d.Vector(-1 + x, y, -1 + z))
            mypoly.SetPoint(p1, c4d.Vector(-1 + x, y,  1 + z))
            mypoly.SetPoint(p2, c4d.Vector( 1 + x, y,  1 + z))
            mypoly.SetPoint(p3, c4d.Vector( 1 + x, y, -1 + z))

            mypoly.SetPolygon(i, c4d.CPolygon(p0, p1, p2, p3) )
            
        except ValueError, e:
            continue
        
        #update status bar
        c4d.StatusSetBar(int(float(i)/count*100))
        
        #set point of object
        pos = c4d.Vector(x, y, z)
        mypoly.SetPoint(i, pos)
    
    #set name
    mypoly.SetName("Point Mesh")
    #update the object after you set all points
    mypoly.Message(c4d.MSG_UPDATE)
    #insert object to document
    doc.InsertObject(mypoly)
    #send event
    c4d.EventAdd()
    #reset status bar
    c4d.StatusClear()
        

if __name__=='__main__':
    ParseXYZ()