



import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


equation = pyeq3.Models_2D.Polynomial.Linear()

pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)

##########################################################

# first solve with no bounds
equation.Solve()

print("Fitted Parameters With No Bounds:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print()

##########################################################

# now with an upper bound
equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded

equation.Solve()

print("Fitted Parameters With One Upper Bound:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
()

##########################################################

# now with a lower bound
equation.upperCoefficientBounds = [] # reset to have no upper bounds
equation.lowerCoefficientBounds = [-8.0, None] # None means the parameter is unbounded

equation.Solve()

print("Fitted Parameters With One Lower Bound:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print()

##########################################################

# now with an upper bound and a fixed coefficient
# note that fixed coefficients override bounds
equation.fixedCoefficients = [-8.5, None] # None means the parameter is not fixed
equation.upperCoefficientBounds = [-9.0, None] # None means the parameter is unbounded
equation.lowerCoefficientBounds = [] # reset to have no lower bounds

equation.Solve()

print("Fitted Parameters With One Upper Bound And One Fixed Coefficient (fixed coeffs override bounds):")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
