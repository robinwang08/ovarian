import pandas
import sys
import numpy

from stats import bootstrap_grouped_ci, permutation_grouped_test, bootstrap_ci, permutation_test
from sklearn.metrics import accuracy_score, recall_score

df = pandas.read_csv(sys.argv[1])

gold = 'Actual'
gold_val = numpy.array(df[gold])
#with_ai = ['Expert 1 + AI', 'Expert 2 + AI', 'Expert 3 + AI', 'Expert 4 + AI']
with_ai = ['AI1', 'AI2', 'AI3']
without_ai = ['E1', 'E2', 'E3']

def specificity(y_pred, y_true):
    return recall_score(y_true=y_true, y_pred=y_pred, pos_label=0)

def average_group(predictions, gold_val, metric):
    return numpy.mean([metric(y_pred=predictions[:,i], y_true=gold_val) for i in range(predictions.shape[-1])])

def difference_stats(predictions1, predictions2, gold_val, metric):
    ci = bootstrap_ci(predictions1, predictions2, gold_val, metric, return_dist=False)

    return {
        "ai": metric(y_pred=predictions1, y_true=gold_val),
        "no-ai": metric(y_pred=predictions2, y_true=gold_val),
        "delta": metric(y_pred=predictions1, y_true=gold_val) - metric(y_pred=predictions2, y_true=gold_val),
        "p": permutation_test(predictions1, predictions2, gold_val, metric),
        "ci": ci
    }

def difference_stats_grouped(predictions1, predictions2, gold_val, metric):
    ci = bootstrap_grouped_ci(predictions1, predictions2, gold_val, metric, return_dist=False)

    return {
        "ai": average_group(predictions1, gold_val, metric),
        "no-ai": average_group(predictions2, gold_val, metric),
        "delta": average_group(predictions1, gold_val, metric) - average_group(predictions2, gold_val, metric),
        "p": permutation_grouped_test(predictions1, predictions2, gold_val, metric),
        "ci": ci
    }

metrics = {
    "accuracy": accuracy_score,
    "sensitivity": recall_score,
    "specificity": specificity,
}

results = list()
for i in range(1, 4):
    no_ai = 'E{}'.format(i)
    ai = 'AI{}'.format(i)

    ai_val = numpy.array(df[ai])
    no_ai_val = numpy.array(df[no_ai])
    for k, v in metrics.items():
        results.append({
            "evaluator": "E-{}".format(i),
            "metric": k,
            **difference_stats(ai_val, no_ai_val, gold_val, v)
        })

ai_val = numpy.array(df[with_ai])
no_ai_val = numpy.array(df[without_ai])

for k, v in metrics.items():
    results.append({
        "evaluator": "averaged",
        "metric": k,
        **difference_stats_grouped(ai_val, no_ai_val, gold_val, v)
    })

results_df = pandas.DataFrame(results)
results_df.to_csv("new_experts2.csv")
print(results_df)
