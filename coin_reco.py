import cv2
import numpy as np
gamescreen = cv2.imread('screens_game/_lot_of_coin.png', cv2.IMREAD_UNCHANGED)
chest = cv2.imread('screens_objects/coin_ok.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(gamescreen, chest, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = chest.shape[1]
h = chest.shape[0]

threshold = .60
yloc, xloc = np.where(result >= threshold)

rectangles = []
for (x, y) in zip(xloc, yloc):
    if x<860 or y>90: # évite le faux positif du compteur en haut à droite
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])



rectangles, weights = cv2.groupRectangles(rectangles, 1, 2)

for (x, y,w ,h) in rectangles:
    cv2.rectangle(gamescreen, (x, y), (x + w, y + h), (0,0,255), 2)
    print(f"il y a un coin en x={x} y={y}")

cv2.imshow('gamescreen', gamescreen)
cv2.waitKey()
cv2.destroyAllWindows()



