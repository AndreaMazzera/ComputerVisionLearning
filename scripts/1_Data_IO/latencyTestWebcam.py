import time
import cv2 as cv

# 0 = default pc webcam 
camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Error")
    exit()
    
prev_time = time.time()
latencies = []

# Video reproduction
while True:
    t_capture = time.time()
    # Acquire frame and get a boolean value ret to check if i've read correctly the frame and numpy array frame
    success, frame = camera.read()
    t_after = time.time()
    
    # Check frame readed correctly
    if not success:
        break
      
    current_latency = t_after - t_capture
    latencies.append(current_latency)    
    
    # Draw latency info on screen
    cv.putText(
        frame,                      
        f"Latency [ms]: {current_latency*1000:1f}",                    
        (10,30),                 
        cv.FONT_HERSHEY_SIMPLEX,    
        1,                          
        (0,255,255),               
        thickness=2                 
    ) 
    
    # Show the frame
    cv.imshow("Webcam Latency Test", frame)
    
    # Wait 25ms to intercept keyboard input AND last 8 bit of keyboard input corresponds ASCII CODE of ESC (27)
    if cv.waitKey(25) & 0xFF==27:
        break

mean_latency: float = sum(latencies)/len(latencies) 
min_latency: float = min(latencies)
max_latency: float = max(latencies)

print(f"Mean Average: {mean_latency*1000:1f} ms")
print(f"Minimum Latency: {min_latency*1000:1f} ms")
print(f"Maximum Latency: {max_latency*1000:1f} ms")


# Release resources (video file or webcam or internal buffers)
camera.release()
cv.destroyAllWindows()
