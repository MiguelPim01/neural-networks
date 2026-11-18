from abc import ABC

import kagglehub

class IDataHandler(ABC):
    """
    Interface que estabele o contrato da aplicação com todo o restante da aplicação.
    
    Funções:
        - `load_data_from_kaggle()`
    """
    def __init__(self, kaggle_link: str, data_dir: str):
        super().__init__()
        
        self.kaggle_link = kaggle_link
        self.data_dir = data_dir
        
    def load_data_from_kaggle(self):
        """
        Carrega um dataset do kaggle e persiste ele localmente.
        """
        print("Fazendo download de dados do repositório Kaggle: ", self.kaggle_link)
        
        path = kagglehub.dataset_download(
            self.kaggle_link, 
            output_dir=self.data_dir
        )
                        
        print("Dados copiados para a pasta: ", path)