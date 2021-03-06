import os
import logging


class Config(object):
    IMAGE_SIZE = 200

    # Should change trials to 10
    TRIALS = 10
    BATCH_SIZE = 16

    EPOCHS = 500
    PATIENCE = 100
    SAMPLES_VALIDATION = 300
    VALIDATION_SPLIT = 0.2
    TEST_SPLIT = 0.1

    EXPERTS = "/media/user1/my4TB/robin/ovarian/ovarian_data/csv/Ovarian_Experts.csv"

    DEVELOPMENT = True
    DEBUG = True
    PRINT_SQL = False
    SECRET = "example secret key"
    LOG_LEVEL = logging.DEBUG

    #RAW_NRRD_ROOT = "/media/user1/my4TB/robin/ovarian/ovarian_data/segmenter2"
    RAW_NRRD_ROOT = "/media/user1/my4TB/robin/ovarian/ovarian_data/raw"

    RAW_FEATURES = [
        "/media/user1/my4TB/robin/ovarian/ovarian_data/csv/Ovarian_Outcome.csv",
        "/media/user1/my4TB/robin/ovarian/ovarian_data/csv/Ovarian_Institution.csv",
        "/media/user1/my4TB/robin/ovarian/ovarian_data/csv/Ovarian_Clinical.csv",
        "/media/user1/my4TB/robin/ovarian/ovarian_data/csv/Ovarian_Sort.csv",
        # "C:/research/ovarian/ovarian_data/csv/",
        ]

    #DATA = "/media/user1/my4TB/robin/ovarian/ovarian_data/segmenter2-data/data"
    DATA = "/media/user1/my4TB/robin/ovarian/ovarian_data/data"
    PREPROCESSED_DIR = os.path.join(DATA, "preprocessed")
    TRAIN_DIR = os.path.join(DATA, "train")
    TEST_DIR = os.path.join(DATA, "test")
    VALIDATION_DIR = os.path.join(DATA, "validation")

    #FEATURES_DIR = "/media/user1/my4TB/robin/ovarian/ovarian_data/segmenter2-data/features"
    FEATURES_DIR = "/media/user1/my4TB/robin/ovarian/ovarian_data/features"
    NRRD_FEATURES = os.path.join(FEATURES_DIR, "nrrd-features.pkl")
    FEATURES = os.path.join(FEATURES_DIR, "training-features.pkl")
    PREPROCESS = os.path.join(FEATURES_DIR, "preprocess.pkl")
    MULTIPLE_LESIONS = os.path.join(FEATURES_DIR, "multiple-lesions.csv")

    INPUT_FORM = "all"

    OUTPUT = "/media/user1/my4TB/robin/ovarian/ovarian_data/output"
    DB_URL = "sqlite:///{}/results.db".format(OUTPUT)
    MODEL_DIR = os.path.join(OUTPUT, "models")
    STDOUT_DIR = os.path.join(OUTPUT, "stdout")
    STDERR_DIR = os.path.join(OUTPUT, "stderr")
    DATASET_RECORDS = os.path.join(OUTPUT, "datasets")

    MAIN_TEST_HOLDOUT = 0.20
    NUMBER_OF_FOLDS = 4
    SPLIT_TRAINING_INTO_VALIDATION = 0.20


config = Config()
