import random
# import os
# form score import get_machine_input
import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        return lmlist


def main():
    wCam,hCam=640,480
    cap=cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)
    # folderPath="computerhand"
    # myList=os.listdir(folderPath)
    # print(myList)
    # overlayList=[]
    # for imPath in myList:
    #     image=cv2.imread(f'{folderPath}/{imPath}')
    #     overlayList.append(image)
    pTime = 0
    cTime = 0
    # cap = cv2.VideoCapture(0)
    detector = handDetector()
    tipIds=[4,8,12,16,20]
    score=0
    c=0
    play="play"
    try:
        c=0
        while True:
            time_series = []
            for i in range(6):
                time_series.append(random.randint(1, 6))

            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)
            if len(lmlist) != 0:
                fingers=[]

                if lmlist[tipIds[0]][1]<lmlist[5][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmlist[tipIds[id]][2]<lmlist[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                # print(sum(fingers))
                tot=sum(fingers)
                score+=tot
                r=random.randint(0,5)
                # print(r,c)
                # r=get_machine_input(time_series)
                if c%35==0 and tot==r:


                    # print(score)
                    play="out"
                else:
                    c+=1

                # cv2.put
                if play=="play":
                    cv2.putText(img, 'score:' + str(score//35), (300, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    # h, w, d = overlayList[r].shape
                    # img[0:h, 0:w] = overlayList[r]
                else:
                    cv2.putText(img, 'OUT', (300, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),
                                3)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime






            img=cv2.resize(img,(1000,600))


            cv2.putText(img,'Batting',(480,480),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

            cv2.imshow("lets play",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return score


def main2():
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    # folderPath = "computerhand"
    # myList = os.listdir(folderPath)
    # print(myList)
    # overlayList = []
    # for imPath in myList:
    #     image = cv2.imread(f'{folderPath}/{imPath}')
    #     overlayList.append(image)
    pTime = 0
    cTime = 0
    # cap = cv2.VideoCapture(0)
    detector = handDetector()
    tipIds = [4, 8, 12, 16, 20]
    score2 = 0
    c = 0
    play = "play"
    try:
        c = 0
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)
            if len(lmlist) != 0:
                fingers = []

                if lmlist[tipIds[0]][1] < lmlist[5][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                # print(sum(fingers))
                tot = sum(fingers)
                r = random.randint(0, 5)
                score2 += r

                # print(r, c)
                if c % 35 == 0 and tot == r:

                    # print(score)
                    play = "out"
                else:
                    c += 1

                # cv2.put
                if play == "play":
                    cv2.putText(img, 'score:' + str(score2 // 35), (300, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0),
                                2)
                    # h, w, d = overlayList[r].shape
                    # img[0:h, 0:w] = overlayList[r]
                else:
                    cv2.putText(img, 'OUT', (300, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),
                                3)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            img = cv2.resize(img, (1000, 600))

            cv2.putText(img,'Bowling',(480,480),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

            cv2.imshow("lets play", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return score2


if __name__ == "__main__":
    s=main()
    s2=main2()
    if s>s2:
        print("you won by " + str((s-s2)%25)+" runs")
    elif s%25==s2%25:
        print("draw")
    else:
        print("you loose by "+ str((s2-s)%25)+" runs")




