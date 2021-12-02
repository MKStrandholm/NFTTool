def generatecodyPatterns(sc):
    
    # Empty space cecor
    ec = (0, 0, 0)
    bodyPatterns = []
    
    bodyPatternHorizontal = [
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, ec, ec, sc, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, sc, sc, sc, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, sc, sc, sc, sc, sc, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, sc, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, sc, ec, ec, sc, sc, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, sc, sc, ec, sc, sc, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec]         
    ]
    
    bodyPatternDiagonal = [
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, sc, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, sc, ec, sc, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec] 
        
        
    ]
    
    bodyPatternVertical = [
        
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, sc, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, sc, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, sc, ec, sc, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, sc, ec, ec, ec, ec, sc, ec, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, sc, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, sc, ec, sc, ec, ec, ec, sc, ec, sc, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec]
        
        
        
    ]
    
    bodyPatterns.append(bodyPatternHorizontal)
    bodyPatterns.append(bodyPatternDiagonal)
    bodyPatterns.append(bodyPatternVertical)
    return bodyPatterns
    