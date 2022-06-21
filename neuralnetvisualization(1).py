# -*- coding: utf-8 -*-
"""NeuralNetvisualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16dJN1yeYx6XR_3hFcwUlCZeSGyQce2iY
"""

def NeuralNetvisualization(model,size=12,colortext='blue',sizetext=8):
  La = []
  for layer in model.layers:
      if layer.get_weights() != []:
        if isinstance(layer.get_weights()[0][0], np.ndarray):
          La.append(layer)

  # Pegar o número de bolas
  Nbolas = []
  NEdgesPbola = []
  for layer in La:
    Nbolas.append(len(layer.get_weights()[0])+1)
    NEdgesPbola.append(len(layer.get_weights()[0][0]))
  Nbolas.append(1)
  NEdgesPbola.append(0)

  # Começar figura 
  fig, ax = plt.subplots(figsize=(size,size))
  Inputs = ['Viés']+Attributes
  deltax=16/(len(Nbolas)-1)
  # i=0
  i=0
  delta = 16/(Nbolas[i]-1)
  for j in range(0,Nbolas[i]):
    circle = plt.Circle((0, delta*j), radius=1, facecolor='white',edgecolor='black')
    plt.text(0, delta*j, Inputs[j],horizontalalignment='center',verticalalignment='center')
    ax.add_patch(circle)
    for k in range(0,NEdgesPbola[i]):
      xini = (i)*deltax + 1
      xfim = (i+1)*deltax - 1
      yini = delta*j
      if Nbolas[i+1] == 1:
        yfim = 8
      else:
        yfim = 16/(Nbolas[i+1]-1)*(k+1)
      dx = xfim-xini
      dy = yfim-yini
      plt.arrow(xini,yini,dx/2,dy/2,length_includes_head=True,head_width=0.2,shape='full',overhang=0.3,color='k',alpha=0.3)
      plt.arrow(xini+dx/2,yini+dy/2,dx/2,dy/2,length_includes_head=True,head_width=0,color='k',alpha=0.3)
      if j != 0:
        plt.text(xini+1*dx/7,yini+1*dy/7,str(round(La[i].get_weights()[0][j-1][k],3)),color=colortext,
                horizontalalignment='center',verticalalignment='center',backgroundcolor='white',size=sizetext)
      elif j ==0:
        plt.text(xini+1*dx/7,yini+1*dy/7,str(round(La[i].get_weights()[1][k],3)),color=colortext,
                horizontalalignment='center',verticalalignment='center',backgroundcolor='white',size=sizetext)

  # i do meio
  for i in range(1,len(Nbolas)-1):
    delta = 16/(Nbolas[i]-1)
    for j in range(0,Nbolas[i]):
      circle = plt.Circle((deltax*i, delta*j), radius=1, facecolor='white',edgecolor='black')
      if j==0:
        plt.text(deltax*i, delta*j, 'Viés',horizontalalignment='center',verticalalignment='center')
      else:
        plt.text(deltax*i, delta*j, '__/',horizontalalignment='center',verticalalignment='center')
      ax.add_patch(circle)
      for k in range(0,NEdgesPbola[i]):
        xini = (i)*deltax + 1
        xfim = (i+1)*deltax - 1
        yini = delta*j
        if Nbolas[i+1] == 1:
          yfim = 8
        else:
          yfim = 16/(Nbolas[i+1]-1)*(k+1)
        dx = xfim-xini
        dy = yfim-yini
        plt.arrow(xini,yini,dx/2,dy/2,length_includes_head=True,head_width=0.2,shape='full',overhang=0.3,color='k',alpha=0.3)
        plt.arrow(xini+dx/2,yini+dy/2,dx/2,dy/2,length_includes_head=True,head_width=0,color='k',alpha=0.3)
        if j != 0:
          plt.text(xini+1*dx/7,yini+1*dy/7,str(round(La[i].get_weights()[0][j-1][k],3)),color=colortext,
                  horizontalalignment='center',verticalalignment='center',backgroundcolor='white',size=sizetext)
        elif j ==0:
          plt.text(xini+1*dx/7,yini+1*dy/7,str(round(La[i].get_weights()[1][k],3)),color=colortext,
                  horizontalalignment='center',verticalalignment='center',backgroundcolor='white',size=sizetext)
  # i final
  i=len(Nbolas)-1
  circle = plt.Circle((deltax*i, 8), radius=1, facecolor='white',edgecolor='black')
  ax.add_patch(circle)
  plt.text(deltax*i, 8, Target[0], horizontalalignment='center',verticalalignment='center')
  plt.xlim(-2,deltax*i + 3)
  plt.ylim(-2,20)
  plt.grid(False)
  plt.axis('off')
  plt.show()