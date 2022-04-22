# class Clothing:    
#     """
#     >>> blue_shirt = Clothing("shirt", "blue")
#     >>> blue_shirt.category
#     'shirt'
#     >>> blue_shirt.color
#     'blue'
#     >>> blue_shirt.is_clean
#     True
#     >>> blue_shirt.wear()
#     >>> blue_shirt.is_clean
#     False
#     >>> blue_shirt.clean()
#     >>> blue_shirt.is_clean
#     True
#     """
#     def __init__(self, category, color):
#         self.category = category
#         self.color = color
#         self.is_clean = True
    
#     def wear(self):
#         self.is_clean = False
    
#     def clean(self):
#         self.is_clean = True

class StudentGrade:
    """
    >>> grade1 = StudentGrade("Arfur Artery", 300)
    >>> grade1.is_failing()
    False
    >>> grade2 = StudentGrade("MoMo OhNo", 158)
    >>> grade2.is_failing()
    True
    >>> grade1.failing_grade
    159
    >>> grade2.failing_grade
    159
    >>> StudentGrade.failing_grade
    159
    >>>
    """    
    failing_grade = 159
    def __init__(self, student_name, num_points):
        self.student_name = student_name
        self.num_points = num_points
    def is_failing(self):
        return self.num_points < StudentGrade.failing_grade
        
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)