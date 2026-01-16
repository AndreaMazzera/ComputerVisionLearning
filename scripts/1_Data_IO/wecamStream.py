import cv2 as cv

# 0 = default pc webcam 
camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Error")
    exit()
    
# Webcam properties
print(f"Camera Frame Width: {camera.get(cv.CAP_PROP_FRAME_WIDTH)}" )
print(f"Camera Frame Height: {camera.get(cv.CAP_PROP_FRAME_HEIGHT)}" )
print(f"Camera Frame Rate: {camera.get(cv.CAP_PROP_FPS)}" )
print(f"Camera Brightness: {camera.get(cv.CAP_PROP_BRIGHTNESS)}" )
print(f"Camera Contrast: {camera.get(cv.CAP_PROP_CONTRAST)}" )
print(f"Camera Saturation: {camera.get(cv.CAP_PROP_SATURATION)}" )
print(f"Camera Exposure: {camera.get(cv.CAP_PROP_EXPOSURE)}" )
print(f"Camera Gain: {camera.get(cv.CAP_PROP_GAIN)}" )
print(f"Camera Codec: {camera.get(cv.CAP_PROP_FOURCC)}" )

# Video reproduction
while True:
    # Acquire frame and get a boolean value ret to check if i've read correctly the frame and numpy array frame
    success, frame = camera.read()
    
    # Check frame readed correctly
    if not success:
        break
            
    # Show the frame
    cv.imshow("Camera", frame)
    
    # Wait 25ms to intercept keyboard input AND last 8 bit of keyboard input corresponds ASCII CODE of ESC (27)
    if cv.waitKey(25) & 0xFF==27:
        break
    
# Release resources (video file or webcam or internal buffers)
camera.release()
cv.destroyAllWindows()
