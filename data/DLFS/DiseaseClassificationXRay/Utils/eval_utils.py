import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

   
# Evaluation of Model

# Results after training the model
train_results = None
valid_results = None

class_labels = [
    'Cardiomegaly'
    , 'Emphysema'
    , 'Effusion'
    , 'Hernia'
    , 'Infiltration'
    , 'Mass'
    , 'Nodule'
    , 'Atelectasis'
    , 'Pneumothorax'
    , 'Pleural_Thickening'
    , 'Pneumonia'
    , 'Fibrosis'
    , 'Edema'
    , 'Consolidation'
]



def true_positives(y, y_pred, threshold=0.5):
    """
    Returns: 
        True Positives (int)
    Args:
        - y (np.array): ground truth , num_examples
        - y_pred (np.array): model output , num_examples
        - threshold (float): threshold deciding for positive prediction of a model
    """
	
	# Thresholded predictions (1 if >=threshold, 0 otherwise )
    thresholded_preds = (y_pred >= threshold)
    return np.sum((y == 1) & (thresholded_preds == 1))


def true_negatives(y, y_pred, threshold=0.5):
    """
    Returns:
        True Negatives (int)
    Args:
        - y (np.array): ground truth , num_examples
        - y_pred (np.array): model output , num_examples
        - threshold (float): threshold deciding positive prediction of a model
    """
    
    # Thresholded predictions (1 if pred >= threshold, 0 otherwise )
    thresholded_preds = (y_pred >= threshold)
    return np.sum((y == 0 ) & (thresholded_preds == 0 ))


def false_positives(y, y_pred, threshold=0.5):
    """
    Returns:
        False positives (int)
    Args:
        - y (np.array): ground truth , num_examples
        - y_pred (np.array): model output , num_examples
        - threshold (float): threshold deciding positive prediction of a model
    """
    
    # Thresholded predictions (1 if >=threshold, 0 otherwise )
    thresholded_preds = (y_pred >= threshold)
    return np.sum((y == 0 ) & (thresholded_preds == 1 ))
    
    
def false_negatives(y, y_pred, threshold=0.5):
    """
    Returns:
        False Negatives (int)
    Args:
        - y (np.array): ground truth , num_examples
        - y_pred (np.array): model output , num_examples
        - threshold (float): threshold deciding positive prediction of a model
    """
    
    # Thresholded predictions (1 if >=threshold, 0 otherwise )
    thresholded_preds = (y_pred >= threshold)
    return np.sum((y == 1 ) & (thresholded_preds == 0 ))
    
# Todo
# - Accuracy
# - Prevalance
# - Sensitivity and Specificity
# - PPV and NPV









