import os
from IPython.display import display, Image

root = '../notMNIST_small'
data_folders = [os.path.join(root, d) for d in sorted(os.listdir(root))]
folder = data_folders[0]

# Display 10 images in notebook
for file in os.listdir(folder)[:10]:
    display(Image(filename=os.path.join(folder, file)))
