from neural_networks import IDataHandler

class TelcoDataHandler(IDataHandler):
    """
    Classe para lidar com dados vindos do Kaggle para o dataset Telco.
    """
    def __init__(self, kaggle_link: str, data_dir: str):
        super().__init__(kaggle_link, data_dir)