count = 0
# y1, y2 = -10, -5
# x1, x2 = 20, 30
y1, y2 = -260, -200
x1, x2 = 25, 67
for y_start in range(y1, -y1 + 1):
    for x_start in range(0, x2 * 5):
        y = x = 0
        y_vel = y_start
        x_vel = x_start
        while y > y1:
            # print(f"{y=}")
            x += x_vel
            y += y_vel
            y_vel -= 1
            x_vel -= 1
            if x_vel < 0:
                x_vel = 0
            if y <= y2 and y >= y1 and x >= x1 and x <= x2:
                count += 1
                break
print(count)
