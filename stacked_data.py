from config import config
from data import data
from keras.models import load_model
from keras import backend as K
import math
from uuid import uuid4, UUID

from db import Result

def load(result):
    path = "{}/models/{}-{}.h5".format(config.OUTPUT, result.uuid, result.model)
    return load_model(path)

def stacked_data(
        uuids=[],
        epochs=config.EPOCHS,
        ):
    results = [ Result.query.filter(Result.uuid == uuid).first() for uuid in uuids ]
    assert len(results) > 0, "no models found"
    assert len(set([result.split_uuid for result in results])) == 1, "all models must be trained on the same split"
    assert len(set([result.label_form for result in results])) == 1, "all models must be trained on the same label"
    training = dict()
    training_fixed = dict()
    validation = dict()
    test = dict()
    for result in results:
        if result.input_form in training:
            continue
        t, v, te = data(
                seed=UUID(result.split_uuid),
                input_form=result.input_form,
                label_form=result.label_form,
                train_shuffle=True,
                validation_shuffle=False,
                train_augment=True,
                validation_augment=False,
            )
        tf, _, _ = data(
                seed=UUID(result.split_uuid),
                input_form=result.input_form,
                label_form=result.label_form,
                train_shuffle=False,
                validation_shuffle=False,
                train_augment=False,
                validation_augment=False,
            )
        training[result.input_form] = t
        training_fixed[result.input_form] = tf
        validation[result.input_form] = v
        test[result.input_form] = te
    # generate labels
    train_labels = list()
    training_fixed_labels = list()
    validation_labels = list()
    test_labels = list()
    first_training = list(training.values())[0]
    first_training_fixed = list(training_fixed.values())[0]
    first_validation = list(validation.values())[0]
    first_test = list(test.values())[0]
    for _ in range(epochs):
        train_labels += first_training.next()[1].tolist()
    for _ in range(math.ceil(len(first_validation)/config.BATCH_SIZE)):
        validation_labels += first_validation.next()[1].tolist()
    for _ in range(math.ceil(len(first_training_fixed)/config.BATCH_SIZE)):
        training_fixed_labels += first_training_fixed.next()[1].tolist()
    for _ in range(math.ceil(len(first_test)/config.BATCH_SIZE)):
        test_labels += first_test.next()[1].tolist()
    first_training.reset()
    first_training_fixed.reset()
    first_validation.reset()
    first_test.reset()
    # generate predictions
    train_predictions = list()
    train_fixed_predictions = list()
    validation_predictions = list()
    test_predictions = list()
    for result in results:
        model = load(result)
        t = training[result.input_form]
        tf = training_fixed[result.input_form]
        v = validation[result.input_form]
        te = test[result.input_form]
        train_predictions.append(model.predict_generator(t, steps=epochs).flatten())
        train_fixed_predictions.append(model.predict_generator(tf, steps=math.ceil(len(tf)/config.BATCH_SIZE)).flatten())
        validation_predictions.append(model.predict_generator(v, steps=math.ceil(len(v)/config.BATCH_SIZE)).flatten())
        test_predictions.append(model.predict_generator(te, steps=math.ceil(len(te)/config.BATCH_SIZE)).flatten())
        t.reset()
        tf.reset()
        v.reset()
        te.reset()
        K.clear_session()
        del model
    return train_predictions, validation_predictions, test_predictions, train_labels, validation_labels, test_labels, train_fixed_predictions, training_fixed_labels
