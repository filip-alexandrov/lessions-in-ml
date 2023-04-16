import cv2
import math


def extract_frames(video_path, output_path):
    # Load the video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get the frames per second (fps) of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))
    interval = 1 * fps

    # Frame index starts at 0
    frame_index = 0

    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # If the current frame index is divisible by the interval, save the frame
        if frame_index % interval == 0:
            frame_name = f"{output_path}/frame_{frame_index // interval:04d}.png"
            cv2.imwrite(frame_name, frame)
            print(f"Saved frame {frame_name}")

        # Increment the frame index
        frame_index += 1

    # Release the video object
    video.release()
    print("Done extracting frames.")


if __name__ == "__main__":
    video_path = "path/to/your/video.mp4"
    output_path = "path/to/output/frames"

    extract_frames(video_path, output_path)
