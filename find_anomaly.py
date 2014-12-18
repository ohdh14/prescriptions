import pandas as pd
import data_prep
import numpy as np
import sklearn
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn.decomposition as decomposition
import sklearn.covariance as cov
#import sklearn.SVM as svm

features = pd.read_csv('features_practice_all.csv')
outliers_fraction = 0.25

# Gaussify features
for col in features.columns:
  feat = features[col].values
  p = data_prep.gaussify(feat)
  print "P: ", p
  feat = data_prep.apply_gauss_transform(feat, p)
  features[col] = feat

# Do PCA
features = features.dropna().values
#features = features.values

pca = decomposition.PCA(n_components=2)
features = pca.fit(features).transform(features)
print features.shape

# Gaussify features
#for i_c, col in enumerate(features.T):
#  #feat = features[col].values
#  p = data_prep.gaussify(col)
#  #print "P: ", p
#  col = data_prep.apply_gauss_transform(col, p)
#  features[:,i_c] = col


clf = cov.EllipticEnvelope(contamination=0.001)

clf.fit(features)
y_pred = clf.decision_function(features).ravel()
threshold = stats.scoreatpercentile(y_pred, 100 * outliers_fraction)
y_pred = y_pred > threshold

# Plotting:
xx, yy = np.meshgrid(np.linspace(-3, 4, 500), np.linspace(-4, 2, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.subplot(1, 2, 1)
plt.title("Gaussian covariance Outlier detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                 cmap=plt.cm.Blues_r)
plt.contour(xx, yy, Z, levels=[threshold],
                    linewidths=2, colors='red')
plt.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                 colors='orange')
plt.scatter(features[:, 0], features[:, 1], c='black')
plt.axis('tight')


####
clf = sklearn.svm.OneClassSVM(kernel="rbf", gamma=3, nu=0.95 * outliers_fraction + 0.05,)
                                     #kernel="rbf", gamma=3)
clf.fit(features)
y_pred = clf.decision_function(features).ravel()
threshold = stats.scoreatpercentile(y_pred, 100 * outliers_fraction)
y_pred = y_pred > threshold

# Plotting:
xx, yy = np.meshgrid(np.linspace(-3, 4, 500), np.linspace(-4, 2, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.subplot(1, 2, 2)
plt.title("SVM Outlier detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                 cmap=plt.cm.Blues_r)
plt.contour(xx, yy, Z, levels=[threshold],
                    linewidths=2, colors='red')
plt.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                 colors='orange')
plt.scatter(features[:, 0], features[:, 1], c='black')
plt.axis('tight')

plt.show()
