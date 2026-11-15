__version__ = "0.0.0"
__author__ = "Miguel Vieira Machado Pim"

from .infra.data.telco_kaggle_dataset import TelcoDataHandler

from .interfaces.data.data_handler import IDataHandler

__all__ = ["TelcoDataHandler", "IDataHandler"]