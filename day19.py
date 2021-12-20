with open("day19_data.txt") as data:
    d = [x.split("\n") for x in data.read().split("\n\n")]
    scanner_map = {}
    for block in d:
        coords = [tuple(map(int, c.split(","))) for c in block[1:] if c != ""]
        scanner_map[block[0]] = coords
    
# Scanner 0 is (0,0,0) and has correct x, y and z allignement
unique_beacons = scanner_map["--- scanner 0 ---"].copy()
del scanner_map["--- scanner 0 ---"]

