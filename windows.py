import sys
import cursor
import colorizer
import boxes
import templates



class Window():
    """" A """
    
    # Defaults
    title           =
    
    borderHor       =
    borderVert      =
    corner          =
    style           =
    borderColor     =
    borderBlink     =
    
    bgStyle         =
    bgColor         =
    bgTrans         =
    
    
    txtColor        =
    txtBlink        =
    lineBreakOrSnip =
    
    layer           =
    nice            =
    show            = True
    
    allBlink        =
    allColor        =
   
    
    
    
    
    
    
    def __init__(self, height, width, optics=templates.default, **kwargs):
        self.height = height
        self.width = width
        self.optics = optics




def test():
    pass


# Main
if __name__ == '__main__':
    for instruction in sys.argv[1:]:
        exec(instruction)