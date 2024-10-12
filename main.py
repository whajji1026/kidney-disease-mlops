from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline


STAGE_Name = "Data Ingestion stage"


try:
    logger.info(f">>>>>>> stage {STAGE_Name} started <<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_Name} completed <<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

