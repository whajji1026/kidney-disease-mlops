from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_Name = "Data Ingestion stage"

class DataIngestionTrainingPipline:
    def __init__(self) :
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__=='__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_Name} started <<<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_Name} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

