from ..objects import File

class OgvProcessor():
    def process_blocking(file):
        Mp4Processor.convert(file)
        WebmProcessor.convert(file)
        PngProcessor.convert(file)

    def process_async(file):
        pass

    @staticmethod
    def convert(file):
        pass
