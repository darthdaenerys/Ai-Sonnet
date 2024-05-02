import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('metrics.csv')


plt.style.use('ggplot')
fig,axs=plt.subplots(nrows=1,ncols=2,figsize=(12,4))
axs[0].plot(df['loss'],label='loss')
axs[0].set_xlabel('Epochs')
axs[0].set_ylabel('Loss')
axs[0].set_title('Loss')
axs[0].legend()
axs[1].plot(df['accuracy']*100, label='accuracy',color='green')
axs[1].set_xlabel('Epochs')
axs[1].set_ylabel('Accuracy')
axs[1].set_title('Accuracy')
axs[1].legend()
plt.tight_layout()
plt.show()