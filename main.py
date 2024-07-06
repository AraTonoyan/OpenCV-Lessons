import cv2
# pip install opencv-python



img = cv2.imread('assets/ararat.jpg', 1)  # nkar@ popoxakani mecha vercnum, isk erkrord popoxakan@
# -1 nkar@ mgacnuma u tapncik maser chi toxum
# 0 moxraguyni erangnerova sarqum
# 1 vonc ka tenc mnuma


# img = cv2.resize(img, (400,400))
# chapsera tali es depqum 400@ 400-i vra

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# es dzevov asum enq ira laynutyun@@ etqan angam mecacni kam poqracni u nuyn dzevov erkarutyun@


img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# ROTATE_(qani astichan)_(CLOCKWISE or COUNTERCLOCKWISE)

# cv2.imwrite('new_img.jpg', img)
# save-a anum taza anunov: araji argument taza anun, erkrord@ en popoxakan@ vorum vor nkarna

cv2.imshow("Ararat", img)  # arajin argument@ nkarari vernagir@ isk erkrord@ popoxakan@ vorum nkarna
cv2.waitKey(0)  # asuma qani milivarkyan bacac mna, isk 0 nshanakuma minchev dzerov paki kam klavyaturai vra knopka sexmi(pritom sexmelu jamanak ira arjeq@ darnuma KeyCode @)
cv2.destroyAllWindows()  # amenaverchum jnjuma bolor patuhanner@


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

img = cv2.imread('assets/ararat.jpg', -1)

# print(img.shape)
# arajin height: erkrord width: errord RGB aliqneri qanak@

# print(img)
# blue, green, red
# [165 122  83]
# [165 122  83]
# [165 122  83]

# orinak
# [255 0 0] kapuyt
# [150 0 0] erknaguyn
# [0 255 0] kanach
# [0 0 255] karmir


# print(img[0])
# araji tox@ nkari

# print(img[59])
# 59rd tox@


# print(img[65][400])
# 65rd toxi (pixelnerov hashvac)
# 400rd pixel@


# import random
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
# cikla frum minchev 100rd tox@ u random pixelner a dnum


# tag = img[50:110, 600:710]
# img[150:210, 310:420] = tag
# nkari mi masi pikselneri tvyalner@ pahuma tag popoxakani mech
# nkari mi urish hatvaci pixcelner@ poxum dra het

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time
import numpy as np

cap = cv2.VideoCapture(0)  # LOAD THE CAMERA
# mechi argument@ petqa en jamanak ete unenq shat kameraner u uzum enq hamarakalel


"""cap.read-i masin"""
# x, y = cap.read()
# print(cap.read)
# cap.read @ lista vori mech ka erku tvyal
# 1@ true ka false: ete kameran normal vichakuma anjataca veradarnuma True isk ete miacaca kam chi ashxatum False
# 2@ pixelner@: henc et pahin nkara nkarum u et nkari pixelneri tvyalner@ ira mech pahum
# x, y @ henc et erku tvyalnern en

"""true u false"""
# print(x)

"""pixels"""
# print(y)
# print(y.shape)


"""nkar@ tpel"""
# cv2.imshow('Image', y)
# x = cv2.waitKey(5000)
# print(x)
# cv2.destroyAllWindows()

# while True:
# ret, frame = cap.read()
# anverch cikli mech an@ndhat nkaruma u darnuma video

# image = np.zeros(frame.shape, np.unit8)
#
# cv2.imshow("frame", frame) # arajn vernagir erkrord kamera, sovoran nkarei nman nkar@ tpuma, uxaki ciklov
#
#
# if cv2.waitKey(500) == ord('q'): # asuma vor 1 milivarkyan mek kadr poxvi u ete sexmenq q kangni
#     break
#
# cap.release() # kara kameran miacni
# cv2.destroyAllWindows()


while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)  # nuyn nkari principov uxaki cikli mech u arag arag nkar@ poxuma darnum video

    if cv2.waitKey(1) == ord('q'):
        # asuma vor ete sexmenq q kangni u es milivarkyanic avtomat kaxvaca cikli aragutyun@
        break

cap.release()  # anjatuma kameran verjnakan
cv2.destroyAllWindows()
