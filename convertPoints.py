######################################################
######################################################
#### In this program we can get the points of the ####
#### plot and make the chage of basis to get the  ####
#### points and make the fit.                     ####
######################################################
######################################################

import matplotlib.pyplot as plt
import os
from pylab import *
from sys import *

def convert_points(filesArray):

    x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[]
    name = ' '
    #walk along the array of file paths
    for x in range(0,len(filesArray)):
        try:
            #We now try to
            pathFile = filesArray[x]
            name = pathFile
            rfile = open(pathFile+'.dat', 'r')
            if rfile:
                for line in rfile:
                    a, b, c, d, e, f = [float(t) for t in line.split()]
                    x1.append(pow(10,a))
                    y1.append(pow(10,b))
                    if c != 0:
                        xizq.append(abs(pow(10,a)-pow(10,c)))
                    else:
                        xizq.append(0.0)
                    if d != 0:
                        xder.append(abs(pow(10,a)-pow(10,d)))
                    else:
                        xder.append(0.0)
                    if e != 0:
                        yarr.append(abs(pow(10,b)-pow(10,e)))
                    else:
                        yarr.append(0.0)
                    if f != 0:
                        yaba.append(abs(pow(10,b)-pow(10,f)))
                    else:
                        yaba.append(0.0)
                
            final_array = open(name+'.dat','w')

            for elem in range(0,len(x1)):
                final_array.write(str(x1[elem])+'\t')
                final_array.write(str(y1[elem])+'\t')
                final_array.write(str(xizq[elem])+'\t')
                final_array.write(str(xder[elem])+'\t')
                final_array.write(str(yarr[elem])+'\t')
                final_array.write(str(yaba[elem])+'\t')
                final_array.write('\n')
            final_array.close()
            x1,y1,xizq,xder,yarr,yaba=[],[],[],[],[],[] #Clean the list for the new file
        except ValueError as err:
            print("Error OS: {0}".format(err))
            print("Tengo un error numerico en "+name+'\n')
        except OverflowError as err:
            print("Error OS: {0}".format(err))
            print("Tengo un desborde en "+name+'\n')
        except IOError as err:
            print("Error OS: {0}".format(err))
            print("No existe el archivo "+name+'\n')
        except:
            print "Revisa tus archivos"+'\n'
            
            



            

def plot():
    path = str(os.getcwd())+'/'
    cont = 1
    mark = ""
    plt.figure('Errores')
    for exp in filesArray:
        if 1<= cont <= 7:
            mark = "o"
        if 8<= cont <= 14:
            mark = "x"
        X,Y, X_izq, X_der, Y_arr, Y_aba = loadtxt(path+exp+'.dat', unpack = True)
        plt.errorbar(X,Y,Y_arr,Y_aba, linestyle="none", marker=mark, markersize=4.0, capsize=3.0,label = str(cont))
        X,Y, X_izq, X_der, Y_arr, Y_aba = [],[],[],[],[],[]
        cont = cont +1
    a=plt.gca()
    a.set_yscale('log')
    a.set_xscale('log')
    plt.legend(filesArray, loc='best')
    plt.show()

    





filesArray = ['atom','fermi','hess','ned','uvot','xrt','xrt-prima']

convert_points(filesArray)
plot()
