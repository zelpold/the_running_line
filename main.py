import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw


def create_video_opencv(message, width=100, height=100, fps=24, time=3):
    out_video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    x, y = width, height//4
    font = ImageFont.truetype("Uni_Sans_Heavy.otf", height-height//4)
    for t in range(fps * time):
        img_with_text = Image.new(mode="RGB", size=(width, height), color=(209, 123, 193))
        x -= (font.getlength(message)+font.getlength(message[0]))/(fps * time)
        draw = ImageDraw.Draw(img_with_text)
        draw.text((x, y), message, (255, 255, 255), font=font)
        frame = cv2.cvtColor(np.array(img_with_text), cv2.COLOR_RGB2BGR)
        out_video.write(frame)
    out_video.release()


create_video_opencv("some_Text для воспроизведения")
