import cv2
from main import handDetector
detector=handDetector()
def user_input():
    n=0
    c=0
    tipIds = [4, 8, 12, 16, 20]
    cap=cv2.VideoCapture(0)
    try:
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)
            if len(lmlist) != 0:
                fingers = []

                if lmlist[tipIds[0]][1] > lmlist[5][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                if fingers[0]==1 and sum(fingers)==1:
                    tot=6
                else:

                # print(sum(fingers))
                    tot = sum(fingers)
                cv2.putText(img, str(tot), (300, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                if n!=tot:
                    n=tot
                    c=0
                else:
                    c+=1
                if c==15:
                    cv2.destroyAllWindows()
                    return n
            cv2.imshow("lets play",img)
            if cv2.waitKey(10) == ord('q'):
                break
    except KeyboardInterrupt:
        pass

# print(user_input())
