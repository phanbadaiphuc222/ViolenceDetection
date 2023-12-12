import cv2

# Path to the input video file
video_path = "C:/Users/OS/Desktop/FinalThesis/Frames/kicking.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Initialize variables
frame_count = 0
output_dir = "ML"

# Loop through the video frames
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Break the loop if no more frames are available
    if not ret:
        break

    # Save the frame as an image file
    frame_output_path = f'{output_dir}frame_{frame_count:04d}.jpg'
    cv2.imwrite(frame_output_path, frame)

    # Display the extracted frame (optional)
    cv2.imshow('Frame', frame)

    # Increment the frame count
    frame_count += 1

    # Press 'q' to quit the extraction process
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
