.. _trailer:

The story behind Yann 
=====================

I am `Ragav Venkatesan`_, the author of Yann. I started doing convolutional neural networks
in the begining of 2015. I am not that big in c++, so I started looking at `theano`_ and started 
following and implementing their tutorials. As I started reading new papers and coding new 
technologies, I slowly integrated them into what was soon developing into a toolbox. My lab mates at
`Visual Representaiton and Processing Group`_ also started getting into CNN research and started 
using my toolbox so I formalized it and hosted it on `GitHub`_. Originall it was a completely 
unstructured and completely demodularized toolbox and went with the name samosa. The codebase 
still exists in older commits on the git.

After considerable effort being put in to make this toolbox modular, and testing it out in 
using the toolbox on some of my own research. This began as a pet project and now I am proud to 
notice that it is a level which I am comfortable sharing with the rest of DL community with.

This toolbox is also slated to be used with the course CSE 591: Introduction to Deep Learning for 
Computer Vision at ASU in Spring of 2017. With more features being added into the toolbox, I figured
I would clean it up, formalize it and write some good documentation so that many people could use 
it. Thus after being rechristened as Yann, this toolbox was born.

.. warning ::
    
    This is a personal toolbox that I am maintaining. I promise nothing. There are only now 
    unit tests being written, although I try to make sure everything is perfectly working. 
    I encourage anyone to use it, contribute to it and write on top of it with that caveat.  

.. tip ::

    I am working on tutorials and quickstart guides for this toolbox. As such, I try to go in detail
    in these tutorials, but I am assuming a pre-requisite training and knowledge on CNNs and 
    Neural Neworks. If you are here looking for a tutorial for those and are disappointed with the 
    material here, please read Prof. Yoshua Bengio's book on Deep Learning, or read the examples 
    from `theano tutorials`_. Theano tutorials also will help understand `theano`_ which is the 
    backend I used for this toolbox.

.. _theano: http://deeplearning.net/software/theano/ 
.. _GitHub: https://github.com/ragavvenkatesan/yann
.. _Ragav Venkatesan: http://www.public.asu.edu/~rvenka10/
.. _Visual Representaiton and Processing Group: http://www.public.asu.edu/~bli24/Research.html
.. _Lasagne: https://github.com/Lasagne/Lasagne
.. _Keras: http://keras.io/
.. _Caffe: http://caffe.berkeleyvision.org/
.. _Blocks: https://blocks.readthedocs.io/en/latest/
.. _theano tutorials: http://deeplearning.net/software/theano/tutorial/examples.html 

What is in the toolbox ? 
========================

I started with the beautiful `theano's tutorials 
<http://deeplearning.net/software/theano/tutorial/>`_. While I started building on top of the 
tutorials and started doing research in this material, I started adding features to it that were 
published. The code here is still fundamentally the theano tutorials only. 
The code that is here in yann has the following popular features that all deep net 
toolboxes seem to have. Among many others there are:

+ **CNNs with easy architecture management:** Because layers can take origins as inputs, pretty much
  any architecture that can be drawn on a blackboard can be constructed using this toolbox. 

+ **Dataset handling capabilities:** I have provided features to setup data as simple matlab files 
  that can be loaded in python and run in batches for training. Alternatively, there is also a 
  wrapper to `skdata's`_ dataset interface and plans dfor adding the `Fuel`_ interface also.
  As of now, I have cifar10, mnist, extended mnists , caltech101, caltech256. I will add more as I 
  can. 

+ **Data visualization capabilities:** Visualize the activities of select images (or random) from 
  the trainset on each layer after select number of epochs of training. Also view filters after 
  select number of epochs. I find this very effective for my understanding.

+ **Techniques from recent publications:** This is where things change a lot and for someone who is 
  getting into deep learning fresh without much theoretical machine learning, I am hoping it would 
  be really helpful. With only a few flags and parameters, you could 
  switch entire optimization methods, including gradient descent, adaGrad, rmsProp add momentums 
  like Polyak Momentum, Nesterov’s accelerated gradients etc. One switch converts the whole networks
  into a max-margin formulation from a softmax formulation. All of these options are plug and play
  or more like add and cook.
  
  I intended this for the scientists in my lab, and students in my class
  who wouldn’t now have to spend days reading the theory behind these methods, but just try them 
  first and if they work, then think of reading them. Most new methods that are recently published 
  and are added including but not limited to: 

   - Dropouts[1]
   - adaGrad[2]
   - Polyak Momentum[3]
   - Nesterov's Accelerated Gradients [4]
   - rmsProp [5]
   - Adam [8]   
   - Maxout and Mixed out Networks [6]
   - FitNets [9]
   - VGG-19 [10]
   - InceptionNet [11]

+ My personal research papers on CNNs were all written using this toolbox and all the codes are in 
  pantry. 

.. _skdata's: https://jaberg.github.io/skdata/
.. _Fuel: https://github.com/mila-udem/fuel
.. _Sebastien Bubeck's: https://blogs.princeton.edu/imabandit/2013/04/01/acceleratedgradientdescent/

.. rubric:: References
 
.. [#]   Srivastava, Nitish, et al. "Dropout: A simple way to prevent neural networks from 
         overfitting." The Journal of Machine Learning Research 15.1 (2014): 1929-1958.
.. [#]   John Duchi, Elad Hazan, and Yoram Singer. 2011. Adaptive subgradient methods for online 
         learning and stochastic optimization. JMLR
.. [#]   Polyak, Boris Teodorovich. "Some methods of speeding up the convergence of iteration 
         methods." USSR Computational Mathematics and Mathematical Physics 4.5 (1964): 1-17. 
         Implementation was adapted from Sutskever, Ilya, et al. "On the importance of 
         initialization and momentum in deep learning." Proceedings of the 30th international 
         conference on machine learning (ICML-13). 2013.
.. [#]   Nesterov, Yurii. "A method of solving a convex programming problem with convergence rate O 
         (1/k2)."   Soviet Mathematics Doklady. Vol. 27. No. 2. 1983. Adapted 
         from `Sebastien Bubeck's`_ blog.
.. [#]   Yann N. Dauphin, Harm de Vries, Junyoung Chung, Yoshua Bengio,"RMSProp and equilibrated 
         adaptive learning rates for non-convex optimization", or arXiv:1502.04390v1
.. [#]   Goodfellow, Ian J., et al. “Maxout networks.” arXiv preprint arXiv:1302.4389 (2013).
.. [#]   Yu, Dingjun, et al. “Mixed Pooling for Convolutional Neural Networks.” Rough Sets and 
         Knowledge Technology. Springer International Publishing, 2014. 364-375.
.. [#]   Kingma, Diederik, and Jimmy Ba. "Adam: A method for stochastic optimization." arXiv 
         preprint arXiv:1412.6980 (2014).
.. [#]   Romero, Adriana, et al. "Fitnets: Hints for thin deep nets." arXiv preprint arXiv:1412.6550 
         (2014).
.. [#]   Simonyan, Karen, and Andrew Zisserman. "Very deep convolutional networks for large-scale 
         image recognition." arXiv preprint arXiv:1409.1556 (2014).
.. [#]   Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Vanhoucke, 
         V. and Rabinovich, A., 2015. Going deeper with convolutions. In Proceedings of the IEEE 
         Conference on Computer Vision and Pattern Recognition (pp. 1-9).
