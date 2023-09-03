import matplotlib.pyplot as plt
e=[12,22,3,4,5,5,5,6,6,55,5,56,78,67,87,56,8,7,69]
bins=[10,20,30,40,50,60,70,80]
plt.hist(e,bins,histtype='bar',rwidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Emp Details")
plt.show()