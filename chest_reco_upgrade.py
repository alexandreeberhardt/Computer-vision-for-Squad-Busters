import cv2
import numpy as np

# les 3 vues des coffres
chest_left = cv2.imread('screens_objects/chest_left.png', cv2.IMREAD_UNCHANGED)
chest_right = cv2.imread('screens_objects/chest_right.png', cv2.IMREAD_UNCHANGED)
chest_front = cv2.imread('screens_objects/chest_front.png', cv2.IMREAD_UNCHANGED)

gamescreen = cv2.imread('screens_game/_double_chest.png', cv2.IMREAD_UNCHANGED)

def match_and_get_rectangles(gamescreen, chest):
    result = cv2.matchTemplate(gamescreen, chest, cv2.TM_CCOEFF_NORMED)
    threshold = .60 # plus de faux positif à partir de 0.5. Des faux négatifs à partir de 0.7 (les faux négatifs ne sont pas grave et normaux car on a plusieurs images)
    yloc, xloc = np.where(result >= threshold)
    w = chest.shape[1]
    h = chest.shape[0]

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])  

    return rectangles

rectangles_left = match_and_get_rectangles(gamescreen, chest_left)
rectangles_right = match_and_get_rectangles(gamescreen, chest_right)
rectangles_front = match_and_get_rectangles(gamescreen, chest_front)
all_rectangles = rectangles_left + rectangles_right + rectangles_front

#for (x, y, w, h) in all_rectangles:
#    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (255, 0, 0), 1)  

grouped_rectangles, weights = cv2.groupRectangles(all_rectangles, groupThreshold=1, eps=0.2)

for (x, y, w, h) in grouped_rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0, 0, 255), 2)  
    print(f"il y a un coffre en x={x} y={y}")

cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()
