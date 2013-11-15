from ..objects import File
from .mp4 import Mp4Processor
from .webm import WebmProcessor
from .ogv import OgvProcessor

class GifProcessor():
    def process_blocking(file):
        Mp4Processor.convert(file)
        WebmProcessor.convert(file)

    def process_async(file):
        OgvProcessor.convert(File)
