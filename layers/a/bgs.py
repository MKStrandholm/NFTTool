def generateBgs(bg, bl):
    bgs = []    
        
    bgBasic = []
    bgDiagonal = []
    bgVertical = []

    # Create a basic background
    for i in range(0,24):
        bgBasic.append([])
        for j in range(0, 24):
            bgBasic[i].append(bg)
            
    # Create a diagonal background
    switch = 0
    for i in range(0, 24):
        bgDiagonal.append([])
        if switch == 0:
            switch = 1 
        else:
            switch = 0
        for j in range(0, 24):
            if switch == 0:
                bgDiagonal[i].append(bg)
                switch = 1
            else:
                bgDiagonal[i].append(bl)
                switch = 0
                
    bgDots =   [
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bg, bg, bg],
                    [bg, bl, bl, bg, bg, bg, bl, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bl, bl, bg, bg, bg, bg, bg, bg, bg, bl, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bl, bg, bg],
                    [bg, bg, bl, bg, bg, bg, bl, bl, bl, bg, bg, bg, bl, bl, bg, bg, bg, bg, bl, bl, bl, bl, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bg, bg, bg, bg, bl, bl, bl, bl, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bl, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg],
                    [bg, bg, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bl, bg],
                    [bg, bg, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bl, bg, bg, bg, bg, bg],
                    [bg, bg, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bl, bl, bg, bg, bg, bg, bg, bg, bg, bl, bg, bg, bg],
                    [bg, bg, bl, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
                ]
                
    # Create a normal vertical striped background
    switch = 0
    for i in range(0, 24):
        bgVertical.append([])
        for j in range(0, 24):
            if switch == 0:
                bgVertical[i].append(bg)
                switch = 1
            else:
                bgVertical[i].append(bl)
                switch = 0
                
    
    # Hardcoded moon background 
    
    # sk = sky
    # ml = moon (light)
    # md = moon (dark)
    # gr = ground
    # tr = trees
    # td = background dark trees
    sk = (55, 61, 85)
    ml = (190, 188, 183)
    md = (144, 141, 134)
    gr = (38, 37, 31)
    tr = (58, 54, 44)
    td = (43, 43, 43)
    
    bgMoon = [        
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, ml, ml],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, ml, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, md, md, ml],
                [sk, sk, ml, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, md, md, ml],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, md, md, ml],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, md, md, ml],
                [sk, sk, sk, sk, sk, sk, sk, ml, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, md, md, ml, ml],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, md, ml, ml, ml],
                [sk, ml, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk],
                [sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk],
                [sk, sk, sk, sk, sk, sk, sk, ml, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk],
                [sk, sk, sk, tr, sk, sk, tr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk],
                [sk, sk, sk, tr, sk, sk, tr, sk, sk, tr, tr, sk, sk, sk, sk, ml, sk, sk, sk, sk, sk, sk, sk, tr],
                [sk, tr, sk, tr, tr, sk, tr, tr, sk, tr, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, tr, sk, sk],
                [sk, tr, tr, tr, tr, tr, tr, tr, tr, tr, sk, sk, sk, tr, sk, tr, sk, sk, sk, sk, sk, sk, tr, tr],
                [td, tr, tr, tr, tr, tr, sk, sk, sk, sk, sk, sk, sk, sk, tr, tr, tr, sk, tr, sk, td, sk, tr, td],
                [td, td, td, td, tr, tr, td, td, td, sk, tr, tr, sk, td, td, td, tr, tr, td, td, td, td, tr, td],
                [td, td, gr, gr, tr, tr, gr, gr, td, td, td, tr, td, td, td, td, tr, td, td, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, tr, tr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr]
            ]


    bgs.append(bgBasic)
    bgs.append(bgDiagonal)
    bgs.append(bgDots)
    bgs.append(bgVertical)
    bgs.append(bgMoon)
    return bgs