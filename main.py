from winequality import logger
from winequality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from winequality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from winequality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from winequality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from winequality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
