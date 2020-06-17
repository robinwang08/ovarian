import pandas
import sys
import numpy
import math

from sklearn.metrics import accuracy_score, recall_score

df = pandas.read_csv(sys.argv[1])

gold = 'Actual'
gold_val = numpy.array(df[gold])
#with_ai = ['Expert 1 + AI', 'Expert 2 + AI', 'Expert 3 + AI', 'Expert 4 + AI']
#with_ai = ['Expert 1 + AI', 'Expert 2 + AI', 'Expert 3 + AI', 'Expert 4 + AI']

without_ai = ['Model1', 'Model2', 'Model3', 'Model4']

def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i]==y_hat[i]==1:
           TP += 1
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FP += 1
        if y_actual[i]==y_hat[i]==0:
           TN += 1
        if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
           FN += 1

    return(TP, FP, TN, FN)


def specificity(y_pred, y_true):
    return recall_score(y_true=y_true, y_pred=y_pred, pos_label=0)

def average_group(predictions, gold_val, metric):
    return numpy.mean([metric(y_pred=predictions[:,i], y_true=gold_val) for i in range(predictions.shape[-1])])

metrics = {
    "accuracy": accuracy_score,
    "sensitivity": recall_score,
    "specificity": specificity,
}

def old_adjusted_wald(p, n, z=1.96):
    p_adj = (n * p + (z**2)/2)/(n+z**2)
    n_adj = n + z**2
    span = z * math.sqrt(p_adj*(1-p_adj)/n_adj)
    return round(max(0, p_adj - span),2), round(min(p_adj + span, 1.0),2)

results = list()

avgtpr = 0
avgtnr = 0
avgsen = 0
avgspec = 0
avgacc = 0
leng = 0

for i in range(1, 5):
    no_ai = 'Model{}'.format(i)
    ai = 'Expert {} + AI'.format(i)

    ai_val = numpy.array(df[ai])
    no_ai_val = numpy.array(df[no_ai])


    TP, FP, TN, FN = perf_measure(gold_val, no_ai_val)
    TPFN = TP + FN
    avgtpr = avgtpr + TPFN

    TNFP = TN+FP
    TPR = TP / TPFN

    avgsen = avgsen + TPR


    avgtnr = avgtnr + TNFP
    b = old_adjusted_wald(TPR,TPFN)
    TNR = TN / TNFP
    avgspec = avgspec + TNR

    c = old_adjusted_wald(TNR, TNFP)
    accuracy = accuracy_score(gold_val, no_ai_val)
    avgacc = avgacc + accuracy
    leng = len(gold_val)
    d = old_adjusted_wald(accuracy, leng)
    print('Expert {} acc '.format(i) + str(accuracy) + " CI " + str(d))
    print('Expert {} sensitivity '.format(i) + str(TPR) + " CI " + str(b))
    print('Expert {} spec '.format(i) + str(TNR) + " CI " + str(c))


avgtpr = avgtpr / 4
avgtnr = avgtnr / 4
avgsen = avgsen / 4
avgspec = avgspec / 4
avgacc = avgacc / 4

x = old_adjusted_wald(avgsen, avgtpr)
y = old_adjusted_wald(avgspec, avgtnr)
z = old_adjusted_wald(avgacc, leng)

print(str(z))
print(str(x))
print(str(y))



