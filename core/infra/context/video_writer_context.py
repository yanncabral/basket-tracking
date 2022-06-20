from pathlib import Path
import cv2
from numpy.typing import ArrayLike
from pyparsing import Optional




class VideoWriter:

    def __init__(self, path: Path) -> None:
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self._writer: Optional[cv2.VideoWriter] = None
        self._path = str(path)
    
    def write(self, frame: ArrayLike):
        if not self._writer:
            self._writer = cv2.VideoWriter(self._path, self.fourcc, 6, (frame.shape[1], frame.shape[0]), True)
        
        self._writer.write(frame)
        

    def close(self):
        self._writer.release()



class VideoWriterContext:
    def __init__(self, path: Path):
        self.writer = VideoWriter(path=path)
         
    def __enter__(self) -> VideoWriter:
        return self.writer
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.writer:
            self.writer.close()


# writer = None
# writer = cv2.VideoWriter("output-vid.mp4", fourcc, 6, (img_dst.shape[1], img_dst.shape[0]), True)
# points_from_camera = np.array(sorted([[16, 752], [1903, 716], [227, 477], [1641, 456]]))

# frame_num = 0
# # while frame_num < 10:
# while cap.isOpened():
#   ret, frame = cap.read()
#   if ret == True and frame_num < 30:
#     print(f"rendering frame {frame_num}")
#     minimap = pega_a_bola(frame)
#     if not writer:
#       writer = cv2.VideoWriter("output-vid.mp4", fourcc, 6, (frame.shape[1], frame.shape[0]), True)
#     # minimap = getMinimapFromFrame(frame)
#     # cv2_imshow(minimap)
#     writer.write(minimap)
#   if frame_num == 300:
#     break

#     # break
#   frame_num += 1

# cap.release()
# writer.release()
# del writer