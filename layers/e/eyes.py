# el = eye outline color
# eh = eye 'hole' color (slit)
# eb = eyeball color
# sk = skin color (for cyclops)
def generateEyes(el, eh, eb, sk):
    # Empty space color
    ec = (0, 0, 0)
    eyes = []
    
    eyesSlit = [
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, el, el, el, el, el, el, el, el, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, el, eh, eb, eb, eh, eh, eb, eb, eh, el, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, el, el, el, el, el, el, el, el, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
            [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec]        
    ]
    
    eyesCyclops = [
        
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, el, el, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, el, sk, sk, el, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, el, eb, eb, sk, el, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, el, el, el, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec],
        [ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec, ec]
             
    ]
    
    eyes.append(eyesSlit)
    eyes.append(eyesCyclops)
    return eyes
    