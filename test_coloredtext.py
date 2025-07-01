import utilsuite
ct = utilsuite.coloredText()
ct.print("This is a red text", color='r') # Print text in red color in terminal
ct.print("This is a green text", color='g')
ct.print("This is a blue text", color='b')
ct.print("This is a yellow text", color='y')
ct.print("This is a magenta text", color='m')
ct.print("This is a cyan text", color='c')
ct.print("This is a white text", color='w')
ct.print("This is a black text", color='k')
ct.print("This is a orange text", color='o', style='bold')

import utilsuite
us, logline = utilsuite.utilitySuite()
import time
us.timer.tic('process')
us.timer.tic('step1')
time.sleep(1)
us.timer.toc('step1')
us.timer.tic('step2')
time.sleep(2)
us.timer.toc('step2')
us.timer.toc('process', Hz=True)