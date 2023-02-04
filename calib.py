import numpy
import cv2
import pickle
import glob

obp = []
imp = []
cRow = 9
cCol = 6

objp = numpy.zeros((cRow*cCol,3), numpy.float32)
objp[:,:2] = numpy.mgrid[0:cRow,0:cCol].T.reshape(-1, 2)

images = glob.glob('img/*.jpg')
imageSize = None 

for iname in images:
    img = cv2.imread(iname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    board, corners = cv2.findChessboardCorners(gray, (cRow,cCol), None)

    obp.append(objp)
    
    corners_acc = cv2.cornerSubPix(
        image=gray, 
        corners=corners, 
        winSize=(11, 11), 
        zeroZone=(-1, -1),
        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
    imp.append(corners_acc)
    if not imageSize:
        imageSize = gray.shape[::-1]

    img = cv2.drawChessboardCorners(img, (cRow, cCol), corners_acc, board)
    cv2.imshow('Chessboard', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

calibration, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
        objectPoints=obp,
        imagePoints=imp,
        imageSize=imageSize,
        cameraMatrix=None,
        distCoeffs=None)
    
f = open('calib.pckl', 'wb')
pickle.dump((cameraMatrix, distCoeffs, rvecs, tvecs), f)
f.close()