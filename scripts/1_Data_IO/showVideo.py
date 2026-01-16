import cv2 as cv

# Function to open a video from a given path
def open_video(path: str): 
    
    # Read the video
    vid = cv.VideoCapture(path)

    if not vid.isOpened():
        raise IOError("Video not found")

    return vid

# Acquire video
video = open_video('assets/videos/video1.mp4')

# Get height e width of video
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

# Compute video aspect ratio
aspect_ratio = width/height

# Resize window of video
target_width=800
target_height=int(target_width/aspect_ratio)

# Create window to show the video
cv.namedWindow("BMW M3 E46", cv.WINDOW_NORMAL)
cv.resizeWindow("BMW M3 E46", target_width, target_height)

# Video reproduction
while True:
    # Acquire frame and get a boolean value ret to check if i've read correctly the frame and numpy array frame
    success, frame = video.read()
    
    # Check frame readed correctly
    if not success:
        break
    
    # Resize frame to ensure aspect ratio of video
    frame_resized = cv.resize(frame, (target_width, target_height))
        
    # Show the frame
    cv.imshow("BMW M3 E46", frame)
    
    # Wait 25ms to intercept keyboard input AND last 8 bit of keyboard input corresponds ASCII CODE of ESC (27)
    if cv.waitKey(25) & 0xFF==27:
        break
    
# Release resources (video file or webcam or internal buffers)
video.release()
cv.destroyAllWindows()
