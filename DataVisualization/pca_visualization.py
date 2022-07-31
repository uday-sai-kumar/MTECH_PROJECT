from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
def pca_vis(_dataframe):
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(_dataframe[_dataframe.columns[:-1]])
   # _dataframe['pca-one'] = pca_result[:, 0]
   # _dataframe['pca-two'] = pca_result[:, 1]
    ax=plt.figure(figsize=(16, 10)).gca(projection='3d')
    ax.scatter(
        xs=pca_result[:, 0],
        ys=pca_result[:, 1],
        zs=pca_result[:, 2],
        c=_dataframe['b_or_m'],
    )
    ax.set_xlabel('pca-one')
    ax.set_ylabel('pca-two')
    ax.set_zlabel('pca-three')
    #plt.scatter(x=pca_result[:, 0], y=pca_result[:, 1], c=_dataframe['b_or_m'])
    #plt.legend(handles=plt.lege()[0])
    #plt.legend(['one', 'two'])
    plt.legend(labels=list(_dataframe['b_or_m']))
    #plt.show()
    plt.show()
    #sns.scatterplot(
       # x=pca_result[:, 0], y=pca_result[:, 1],)
