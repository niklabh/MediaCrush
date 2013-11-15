from ..objects import File
from .webm import WebmProcessor
from .ogv import OgvProcessor

class Mp4Processor():
    def process_blocking(file):
        WebmProcessor.convert(file)
        PngProcessor.convert(file)

    def process_async(file):
        OgvProcessor.convert(file)

    @staticmethod
    def convert(file):
        pass
