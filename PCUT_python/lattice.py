def lattice(lx,ly):
    Ns = 2*lx*ly; Np = Ns/2;
    bpn  = [[0 for x in range(4)] for y in range(Ns)]
    bp2s = [[0 for x in range(4)] for y in range(Ns)]
    bsp  = [[0 for x in range(2)] for y in range(Ns)]
    for x1 in range(0, lx):
        for y1 in range(0, ly):
            s1 = x1+y1*lx
            x2 = (x1+1) % lx
            y2 = y1
            bpn[s1][0] = x2+y2*(lx)
            bpn[s1][2] = (x1-1) % lx+y2*(lx)
            bp2s[s1][0] = s1
            bp2s[s1][2] = s1+Np
            bp2s[s1][3] = x2+y2*(lx)+Np
            x2 = x1
            y2 = (y1+1) % ly
            bpn[s1][3] = x2+y2*lx
            bp2s[s1][1] = x2+y2*lx
            bpn[s1][1] = x2+(y1-1) % ly*lx

            bp2s[s1+Np][0] = bp2s[s1][2]
            bp2s[s1+Np][1] = bp2s[s1][3]
            bp2s[s1+Np][2] = bp2s[s1][1]
            bp2s[s1+Np][3] = bp2s[s1][0]

            bpn[s1+Np][0] = bpn[s1][1]
            bpn[s1+Np][1] = bpn[s1][2]
            bpn[s1+Np][2] = bpn[s1][3]
            bpn[s1+Np][3] = bpn[s1][0]
    
    for x1 in range(0,Ns):
        bsp[0][x1] = x1;
        bsp[1][x1] = bpn[1][x1];

        bsp[0][bp2s[2][x1]] = x1;
        bsp[1][bp2s[2][x1]] = bpn[3][x1];      

    return bpn, bp2s, bsp
