
def generateFrames(fm, fs, fu):
    frames = []
    # Empty space color
    ec = (0, 0, 0)
  
    noFrame = []
   # Create a basic background
    for i in range(0,24):
        noFrame.append([])
        for j in range(0, 24):
            noFrame[i].append(ec)
            
    frameSilver = [
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fm, ],
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ]    
    ]
    
    frameGold = [    
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ],
        [fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, ],
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ]     
        
    ]
    
    frameDiamond = [
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ],
        [fm, fu, fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, fu, fm, ],
        [fm, fm, fs, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fs, fm, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fm, fs, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fs, fm, fm, ],
        [fm, fu, fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, fu, fm, ],
        [fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, ] 
    ]
    
    frameInvert = [
        [fu, fu, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fu, fu, ],
        [fu, fm, fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, fm, fu, ],
        [fm, fm, fs, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fs, fm, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fm, ],
        [fm, fm, fs, fs, fs, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, fs, fs, fs, fm, fm, ],
        [fu, fm, fm, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fs, fm, fm, fu, ],
        [fu, fu, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fm, fu, fu, ]
    ]
  
    frames.append(noFrame)
    frames.append(frameSilver)
    frames.append(frameGold)
    frames.append(frameDiamond)
    frames.append(frameInvert)
    
    return frames