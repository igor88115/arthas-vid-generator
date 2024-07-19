import pandas as pd

class Arthas_input:
    def __init__(self, video_link):
        self.video_link = video_link


def get_input_from_excel(file_path):
    df = pd.read_excel(file_path)
    result = []
    for index, row in df.iterrows():
        result.append(Arthas_input(row["video link"]))
    return result

