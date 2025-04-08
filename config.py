input_config = {
    "elevation": {
        "prompt": "\nElevation relative to treeline:\n <TL = below\n TL = at\n >TL = above\n",
        "map": {'>TL': 0.0, 'TL': 1.0, '<TL': 2.0}
    },
    "aspect": {
        "prompt": "\nSlope aspect (N, NE, E, SE, S, SW, W, NW):\n",
        "map": {'N': 2.0, 'NE': 1.0, 'E': 0.0, 'SE': 3.0, 'S': 6.0, 'SW': 7.0, 'W': 5.0, 'NW': 4.0}
    },
    "snow_type": {
        "prompt": "\nSnow type (L, WL, SS, HS, WS, SF, U for unknown):\n",
        "map": {'SS': 0, 'HS': 1, 'WS': 5, 'WL': 2, 'L': 4, 'U': 6, 'SF': 3}
    },
    "transportation": {
        "prompt": "\nTransportation method (AS=ski, AR=snowboard, AI=snowshoe, AF=hike, AM=snowmobile, AV=other, N=natural):\n",
        "map": {'N': 0, 'AS': 1, 'AV': 2, 'AR': 9, 'AI': 16, 'AM': 8, 'AF': 11}
    },
    "slope_size": {
        "prompt": "\nSlope size (R1=very small to R5=very large):\n",
        "map": {'R1': 1, 'R2': 0, 'R3': 2, 'R4': 3, 'R5': 4}
    },
    "area": {
        "prompt": "\nColorado zone (FR, SF, VS, SA, AS, GU, NSJ, SSJ, SC):\n",
        "map": {'FR': 2, 'GU': 1, 'VS': 3, 'AS': 4, 'SA': 5, 'NSJ': 0, 'SSJ': 6, 'SF': 7, 'SC': 8}
    }
}

danger_levels = {
    1: "D1 - Safe to go out",
    2: "D1 - Safe to go out",
    0: "D2 - Slightly dangerous. Use caution.",
    3: "D2 - Slightly dangerous. Use caution.",
    4: "D3 - Danger high. Avalanches may move vehicles.",
    7: "D3 - Danger high. Avalanches may move vehicles.",
    6: "D4 - Extreme danger. Avalanches may destroy structures.",
    10: "D5 - Check if the mountain is still standing."
}