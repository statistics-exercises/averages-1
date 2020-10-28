import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       self.assertTrue( len(this_x)==100, "you have plotted the wrong number of coordiantes" )
       for i in range( len(this_x) ) :
           self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your plot are incorrect" )
           self.assertTrue( yv<1 and yv>0, "one or more y coordinate in your plot is not between 0 and 1" )
       mean = sum(this_y) / len(this_y) 
       bar = np.sqrt(1/12/100)*st.norm.ppf( (0.99 + 1) / 2 )
       self.assertTrue( np.fabs( mean - 0.5 )<bar, "you seem to be plotting variables from the wrong statistical distribution" )
