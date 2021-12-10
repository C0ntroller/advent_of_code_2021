


with open("day09_data.txt") as file:
    heights = list(map(list, [x.strip() for x in file.readlines()]))
    risks = []
    basin_sizes = []
    for i in range(len(heights)):
        heights[i] = list(map(int, heights[i]))

    limity = len(heights)
    limitx = len(heights[0])

    def find_basin_size(x, y):
        if x < 0 or x >= limitx or y < 0 or y >= limity: return 0
        if heights[x][y] == 9: return 0
        heights[x][y] = 9
        return 1 + find_basin_size(x-1,y) + find_basin_size(x+1,y) + find_basin_size(x,y-1) + find_basin_size(x,y+1)

    for i in range(limity):
        for j in range(limitx):
            surround = [
                heights[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 10, #top left
                heights[i][j-1] if j-1 >= 0 else 10, #left
                heights[i+1][j-1] if i+1 < limity and j-1 >= 0 else 10, #bottom left
                heights[i+1][j] if i+1 < limity else 10, #bottom
                heights[i+1][j+1] if i+1 < limity and j+1 < limitx else 10, #bottom right
                heights[i][j+1] if j+1 < limitx else 10, # right
                heights[i-1][j+1] if i-1 >= 0 and j+1 < limitx else 10, #top right
                heights[i-1][j] if i-1 >= 0 else 10, #top
            ]
            if list(filter(lambda x: x < heights[i][j], surround)) == []:
                risks.append(heights[i][j]+1)
                basin_sizes.append(find_basin_size(j, i))
                
    
    print(sum(risks))
    basin_res = 1
    for i in range(3):
        e = max(basin_sizes)
        basin_sizes.remove(e)
        basin_res *= e
    print(basin_res)