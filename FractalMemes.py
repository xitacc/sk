import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.infty)

def mandelbrot(n_rows:[int,float], n_columns:int, iterations:int):
    x_cor = np.linspace(-2,1,n_rows)
    y_cor = np.linspace(-2,1,n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
            # print((i/x_len)*100,"% completed")
    # print(output.T)
    # print(output)
    # plt.imshow(output.T, cmap="hot")
    basename = 'MandelFractal z3 '+' x '+str(n_columns)+' y '+str(n_rows)+' depth '+str(iterations)
    plt.imsave(basename+'.png', output.T)
    with open(basename+'.txt','w') as f:
        f.write(str(output.T))
# tarr = np.zeros((2,3))
# tarr[:][0]=3
# print(tarr)
# print(tarr.T)
# mandelbrot(1000, 1000, 15)
mandelbrot(1001, 1001, 251)


