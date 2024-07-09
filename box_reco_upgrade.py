import cv2
import numpy as np

box_left = cv2.imread('screens_objects/box_left.png', cv2.IMREAD_UNCHANGED)
box_right = cv2.imread('screens_objects/box_right.png', cv2.IMREAD_UNCHANGED)
box_front = cv2.imread('screens_objects/box_front.png', cv2.IMREAD_UNCHANGED)

gamescreen = cv2.imread('screens_game/_box_middle.png', cv2.IMREAD_UNCHANGED)

def match_and_get_rectangles(gamescreen, box):
    result = cv2.matchTemplate(gamescreen, box, cv2.TM_CCOEFF_NORMED)
    threshold = .55 # plus de faux positif à partir de 0.5. Des faux négatifs à partir de 0.7 (les faux négatifs ne sont pas grave et normaux car on a plusieurs images)
    yloc, xloc = np.where(result >= threshold)
    w = box.shape[1]
    h = box.shape[0]

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])  

    return rectangles

rectangles_left = match_and_get_rectangles(gamescreen, box_left)
rectangles_right = match_and_get_rectangles(gamescreen, box_right)
rectangles_front = match_and_get_rectangles(gamescreen, box_front)

all_rectangles = rectangles_left + rectangles_right + rectangles_front

for (x, y, w, h) in all_rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255, 0, 0), 1) 

grouped_rectangles, weights = cv2.groupRectangles(all_rectangles, groupThreshold=1, eps=0.2)

for (x, y, w, h) in grouped_rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0, 0, 255), 2)  
    print(f"il y a une box en x={x} y={y}")

cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()
