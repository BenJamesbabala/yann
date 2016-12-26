import theano.tensor as T

def cross_entropy ( a , b ):
    """
    This function produces a point-wise cross entropy error between ``a`` and ``b``
    
    Args:
        a: first input
        b: second input

    Returns: 
        theano shared variable: Computational graph with the error.
    """
    return T.mean(T.nnet.categorical_crossentropy(a.flatten(2),b.flatten(2)))

def l2 ( a,  b ): 
    """
    This function produces a point-wise L2 error between ``a`` and ``b``
    
    Args:
        a: first input
        b: second input

    Returns: 
        theano shared variable: Computational graph with the error.
    """    
    return T.sqrt(T.sum((a - b) ** 2 ))
    
def l1 ( a, b ):
    """
    This function produces a point-wise L1 error between ``a`` and ``b``
    
    Args:
        a: first input
        b: second input

    Returns: 
        theano shared variable: Computational graph with the error.
    """        
    return T.sum( abs (a - b) )    
            
def rmse ( a,  b ): 
    """
    This function produces a point-wise root mean squared error error between ``a`` and ``b``
    
    Args:
        a: first input
        b: second input

    Returns: 
        theano shared variable: Computational graph with the error.
    """        
    return T.sqrt(T.mean((a - b) ** 2))