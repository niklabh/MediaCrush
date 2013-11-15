from ..objects import File
from .mp4 import Mp4Processor
from .ogv import OgvProcessor

class WebmProcessor():
    def process_blocking(file):
        Mp4Processor.convert(file)
        PngProcessor.convert(file)

    def process_async(file):
        OgvProcessor.convert(file)

    @staticmethod
    def convert(file):
        pass
