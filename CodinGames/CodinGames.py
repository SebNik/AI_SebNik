def map_checkpoints(c):
    # this function creates a map of the checkpoints
    r_cirle = 600
    map_c = []
    c_count = 0
    map_c.append(c[0])
    for a in range(0, len(c) - 1):
        start_x = c[0][0]
        start_y = c[0][1]
        for i in range(1, len(c) - 1):
            distance = ((start_x - c[i][0]) ** 2 + (start_y - c[i][1]) ** 2) ** 0.5
            if distance <= r_cirle and c_count == 0:
                c_count = i
            if distance <= r_cirle and c_count != 0:
                # print(c, c_count, map_c, distance)
                map_c[c_count - 1][0] = (map_c[c_count - 1][0] + c[i][0]) / 2
                map_c[c_count - 1][1] = (map_c[c_count - 1][1] + c[i][1]) / 2
                # print(c_count, map_c)
            elif c[i] not in map_c:
                map_c.append(c[i])
    return map_c, c_count


# setting any start points
x = 0
y = 0
# list of checkpoints
checkpoints = []
# game loop for game
while True:
    # getting the prev var set
    prevX = x
    prevY = y
    # reading in the values
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in
                                                                                               input().split()]
    # getting the x, y from the opponent
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # adding checkpoints in list
    checkpoints.append([next_checkpoint_x, next_checkpoint_y])
    if len(checkpoints) > 2:
        map_coor, count = map_checkpoints(checkpoints)
    # in case this is the first value
    if prevX == 0:
        prevX = x
        prevY = y

    # distance
    if next_checkpoint_dist < 1500:
        thrust = 30
    if next_checkpoint_dist < 650:
        thrust = 19
    else:
        thrust = 100

    # angle
    if abs(next_checkpoint_angle) > 90:
        thrust = 0

    if abs(next_checkpoint_angle) < 50 and next_checkpoint_dist < 2600 and (
            (next_checkpoint_x - 8000) ** 2 + (next_checkpoint_y - 4500) ** 2) ** 0.5 > 3000:
        # next_checkpoint_x = 8000
        # next_checkpoint_y = 4500
        next_checkpoint_x = int(map_coor[count - 1][0])
        next_checkpoint_y = int(map_coor[count - 1][1])
        thrust = 30

    # boost when checkpoint distance is 7000 and angle is 0
    if next_checkpoint_dist > 7000 and (-5 < next_checkpoint_angle < 5):
        thrust = "BOOST"

    print(str(next_checkpoint_x - (x - prevX) * 3) + " " + str(next_checkpoint_y - (y - prevY) * 3) + " " + str(thrust))


# this is the attack pod
def pod_2_dumm(d):
    if d['my_opponent_1'][5] > d['my_opponent_2'][5]:
        to_attack = 'my_opponent_1'
    elif d['my_opponent_1'][5] < d['my_opponent_2'][5]:
        to_attack = 'my_opponent_2'
    else:
        to_attack = 'my_opponent_1'

    # with same speed vector movement in next thing
    next_opp_x = (d[to_attack][2] * 20 / 17) + d[to_attack][0]
    next_opp_y = (d[to_attack][3] * 20 / 17) + d[to_attack][1]

    # checking where I would land when deploying shiel now
    # angle_r_x = math.cos(d['mypod_2'][4]*math.pi/180)
    # angle_r_y = math.sin(d['mypod_2'][4]*math.pi/180)
    x_with_shield = d['mypod_2'][2] + d['mypod_2'][0]
    y_with_shield = d['mypod_2'][3] + d['mypod_2'][0]
    # cal the distance with shield to opp
    distance_with_shield = ((next_opp_x - x_with_shield) ** 2 + (next_opp_y - y_with_shield) ** 2) ** 0.5
    # check size of distance
    if distance_with_shield < 1000:
        print(str(int(next_opp_x)) + ' ' + str(int(next_opp_y)) + ' SHIELD')
    else:
        print(str(int(next_opp_x)) + ' ' + str(int(next_opp_y)) + ' 100')