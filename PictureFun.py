import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimage

dir_path = "C:/Users/cxd/Desktop/Kunst/Pepe"

print(os.listdir(dir_path))
concat_path = [os.path.join(dir_path, item) for item in os.listdir(dir_path)]
print(concat_path)
one_c_path = concat_path[2]
with open(one_c_path,'r') as file:
    print(file)
print()

# img = mpimage.imread(one_c_path)
#
# plt.imshow(img)
