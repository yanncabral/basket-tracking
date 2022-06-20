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
        if self._writer:
            self._writer.release()


class VideoWriterContext:
    
    def __init__(self, path: Path):
        self.writer = VideoWriter(path=path)
         
    def __enter__(self) -> VideoWriter:
        return self.writer
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.writer.close()