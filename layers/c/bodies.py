# ol = outline color
# bm = main body color
def generateBodies(ol, bm):
    
    # Empty space color
    ec = (0, 0, 0)
    bodies = []
    
    bodyBasic = [
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ol, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, bm, bm, ol, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, ol, bm, bm, bm, bm, bm, bm, bm, bm, bm, bm, ol, ol, bm, ol, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ol, ol, ol, bm, bm, bm, bm, bm, ol, ol, ol, bm, ol, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, ol, ec, ol, ec, ec, ec, ec, ec],
            [ec, ec, ec, ol, ol, ol, ol, ol, ol, bm, bm, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ol, bm, bm, bm, bm, bm, ol, bm, bm, ol, ol, ol, ol, ol, ol, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ol, bm, bm, ol, ol, ol, ol, bm, ol, bm, bm, bm, bm, bm, bm, ol, ol, ec, ec, ec, ec, ec],
            [ec, ec, ol, ol, ol, ec, ec, ec, ol, bm, ol, bm, bm, ol, ol, ol, ol, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ol, bm, bm, ol, ol, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ol, bm, bm, bm, ol, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ol, ol, bm, bm, bm, ol, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, bm, bm, bm, bm, bm, ol, bm, bm, bm, bm, bm, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec]          
    ]
    
    bodies.append(bodyBasic)
    return bodies
    