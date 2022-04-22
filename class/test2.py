class Clothing:    
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """
    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True
    
    def wear(self):
        self.is_clean = False
    
    def clean(self):
        self.is_clean = True
        
        
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)