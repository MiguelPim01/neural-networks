from src import TelcoDataHandler

def main():
    # 1. Fazendo download dos dados necessários para treinamento
    telco_kaggle_link = "blastchar/telco-customer-churn"
    telco_data_dir = "data/raw/telco"
    
    telco_data_handler = TelcoDataHandler(telco_kaggle_link, telco_data_dir)
    telco_data_handler.load_data_from_kaggle()

if __name__ == "__main__":
    main()