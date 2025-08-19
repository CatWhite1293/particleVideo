import cv2
import os

video_path = "video.mp4"
output_path = "image"
os.makedirs(output_path, exist_ok=True)
file = open("data/pv/functions/video.mcfunction", "w")


def video2image():
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_name = os.path.join(output_path, f"{frame_count}.jpg")
        cv2.imwrite(frame_name, frame)
        frame_count += 1

    cap.release()
    print(f"提取完成，共 {frame_count} 帧。")
    return frame_count


def gen_datapack():
    os.makedirs("data", exist_ok=True)
    count = len([f for f in os.listdir("./image")])

    # file.write("scoreboard objectives remove time\n")
    file.write("scoreboard objectives add time dummy\n")


    tick = 0
    for image in range(0,count):
        file.write(f'execute if score time time matches {tick} run particleex image end_rod ~ ~3 ~ {image}.jpg 0.175 0 0 0 not 9.0 0 0 0 10 "vy=0" 1 null\n')
        tick += 15

if __name__ == '__main__':
    #video2image()
    gen_datapack()







