from PIL import Image
import numpy as np
import os
from random import randint
from layers.a import bgs
from layers.b import frames
from layers.c import bodies
from layers.d import body_patterns
from layers.e import eyes

dirname = os.path.dirname(__file__)
dimensions = 480, 480
successCount = 0
    
for i in range(0, 6666):
    # Background color (basic)
    bg = (randint(0,255), randint(0,255), randint(0,255)) 
    # Background alt color (dots and stripes)
    bl = (randint(0,255), randint(0,255), randint(0,255))
   
    # Pass in the bg colors we want to use 
    bgArray = bgs.generateBgs(bg, bl)

    frameNum = randint(0, 10000)  
    
    ### Frame stuff: fr is the main frame color, fs is the shaded color ###
    # Epic frame, diamond
    if frameNum >= 9975:
        fr = (129, 252, 255)
        fs = (98, 223, 226)
        fu = (102, 51, 153)
        # Pass in the frame colors we want to use 
        frameArray = frames.generateFrames(fr, fs, fu)
        frameLayer = frameArray[3]
    # Rare frame, gold
    elif frameNum >= 8900 and frameNum < 9900:
        fr = (243, 206, 86)
        fs = (213, 179, 59)
        # No special colors on this frame, so white placeholder
        fu = (255, 255, 255)
        # Pass in the frame colors we want to use 
        frameArray = frames.generateFrames(fr, fs, fu)
        frameLayer = frameArray[2]
    # Uncommon frame, silver
    elif frameNum >= 5900 and frameNum < 8900:
        fr = (220, 220, 220)
        fs = (192, 192, 192)
        # No special colors on this frame, so white placeholder
        fu = (255, 255, 255)
        # Pass in the frame colors we want to use 
        frameArray = frames.generateFrames(fr, fs, fu)
        frameLayer = frameArray[1]
    # Common frame, bronze
    else:
        fr = (139, 104, 29)
        fs = (111, 80, 0)
        # No special colors on this frame, so white placeholder
        fu = (255, 255, 255)
         # Pass in the frame colors we want to use 
        frameArray = frames.generateFrames(fr, fs, fu)
        frameLayer = frameArray[0]

    invertChance = randint(0, 1000000)

    if (invertChance >= 999990):
        # Invert all colors except frame which will be unique
        ol = (abs((ol[0] - 255)), abs((ol[1] - 255)), abs((ol[2] - 255)))
        eh = (abs((eh[0] - 255)), abs((eh[1] - 255)), abs((eh[2] - 255)))
        eb = (abs((eb[0] - 255)), abs((eb[1] - 255)), abs((eb[2] - 255)))
        sk = (abs((sk[0] - 255)), abs((sk[1] - 255)), abs((sk[2] - 255)))
        bf = (abs((bf[0] - 255)), abs((bf[1] - 255)), abs((bf[2] - 255)))
        bs = (abs((bs[0] - 255)), abs((bs[1] - 255)), abs((bs[2] - 255)))
        # Although we want black, we can't use 0,0,0 since that's ignored
        fr = (1, 1, 1)
        fs = (27, 27, 27)
        fu = (255, 255, 255)
        # Pass in the frame colors we want to use 
        frameArray = frames.generateFrames(fr, fs, fu)
        frameLayer = frameArray[4]
       
    # Outline color - Always black by default (but not 0,0,0 so we can have it not be ignored)
    ol = (1,1,1) 
    # Main body color
    bf = (randint(0, 255), randint(0,255), randint(0, 255))
    bodyArray = bodies.generateBodies(ol, bf)
    bodyLayer = bodyArray[0]

    # Body stripes color
    bs = (randint(0, 255), randint(0,255), randint(0, 255))
    bodyPatternArray = body_patterns.generatecodyPatterns(bs)
    
    # Generate a number to determine which body pattern to use
    patternNum = randint(0, 2000)
    
    # Rarest - checkers
    if (patternNum > 1750):
        bodyPatternLayer = bodyPatternArray[1]
    # Then vertical stripes
    elif (patternNum < 1750 and patternNum >= 950):
        bodyPatternLayer = bodyPatternArray[2]
    # Then horizontal stripes
    else:
        bodyPatternLayer = bodyPatternArray[0]
    
     # Eye hole color
    eh = (randint(0,255), randint(0,255), randint(0,255))
    # Eyeball color
    eb = (randint(0, 255), randint(0,255), randint(0, 255))
    # Skin color
    sk = (randint(0, 255), randint(0,255), randint(0, 255))

    eyesArray = eyes.generateEyes(ol, eh, eb, sk)

    # Generate a number to determine which eye to use
    eyeNum = randint(0, 10000)
    
    # Rarest - cyclops
    if (eyeNum >= 7500):
        eyeLayer = eyesArray[1]
    # Then slit
    else:
        eyeLayer = eyesArray[0]
  
    # This determines which background type to use    
    bgTypeNum = randint(0, 10000)
    
    # Rarest variation - moon image
    if (bgTypeNum >= 9998):
        mainLayer = bgArray[4]
    else:
        bgPatternNum = randint(0,10000)
        # Rarest - dots
        if (bgPatternNum >= 9950):
            mainLayer = bgArray[2]
        # 2nd rarest - diagonal stripes
        elif (bgPatternNum >= 9050 and bgPatternNum < 9950):
            mainLayer = bgArray[1]
        # 3rd rarest - vertical stripes
        elif (bgPatternNum > 7250 and bgPatternNum < 9050):
            mainLayer = bgArray[3]
        # Most common - solid color
        else:
            mainLayer = bgArray[0]
    
    # This section compares two layer matrices and merges them on 'empty color' data - pixels with (0,0,0) are considered empty space and should not be included 
    
    for a in range(len(mainLayer)):
        for b in range(len(mainLayer[a])):
                if frameLayer[a][b] != (0,0,0):
                    mainLayer[a][b] = frameLayer[a][b]
      
   # Compare main layer with body layer
    for a in range(len(mainLayer)):
        for b in range(len(mainLayer[a])):
                if bodyLayer[a][b] != (0,0,0):
                    mainLayer[a][b] = bodyLayer[a][b]
                      
    # Compare main layer with body pattern layer
    for a in range(len(mainLayer)):
        for b in range(len(mainLayer[a])):
                if bodyPatternLayer[a][b] != (0,0,0):
                    mainLayer[a][b] = bodyPatternLayer[a][b]
          
    # Compare main layer with eye layer          
    for a in range(len(mainLayer)):
        for b in range(len(mainLayer[a])):
                if eyeLayer[a][b] != (0,0,0):
                    mainLayer[a][b] = eyeLayer[a][b]
    successCount += 1
    print("Successes: " + str(successCount))          
                        
    # Convert the python array to a numpy array so we can run PIL on it               
    array = np.array(mainLayer, dtype=np.uint8)

    # Save the current image to a local folder
    newImage = Image.fromarray(array)
    newImage = newImage.resize(dimensions, resample = 0)
    imgName = dirname + '/minimos/' + str(i) + '.png'
    newImage.save(imgName)
 
print("Generation complete!")       