import pandas as pd
import utils.data_prep as data_prep
import scikit-learn as sklearn
import scikit-learn.covariance as cov
import scipy.stats
import matplotlib.pyplot as plt


features = pd.read_csv('features_practice.csv')
outliers_fraction = 0.25

# Gaussify features
for col in features.columns:
  feat = features[col].values
  p = data_prep.gaussify(feat)
  print "P: ", p
  feat = data_prep.apply_gauss_transform(feat, p):
  features[col] = feat

clf = cov.EllipticEnvelope(contamination=.1)

clf.fit(features.values)
y_pred = clf.decision_function(features.values).ravel()
print y_pred
threshold = stats.scoreatpercentile(y_pred, 100 * outliers_fraction)
y_pred = y_pred > threshold

# Plotting:
xx, yy = np.meshgrid(np.linspace(-7, 7, 500), np.linspace(-7, 7, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plot = plt.plot() #subplot(1, 2, i + 1)
plot.set_title("Outlier detection")
plot.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                 cmap=plt.cm.Blues_r)
a = plot.contour(xx, yy, Z, levels=[threshold],
                    linewidths=2, colors='red')
plot.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                 colors='orange')
b = plot.scatter(X[:-n_outliers, 0], X[:-n_outliers, 1], c='white')
c = plot.scatter(X[-n_outliers:, 0], X[-n_outliers:, 1], c='black')
plot.axis('tight')
