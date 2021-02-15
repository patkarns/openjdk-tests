import sys
import os
import ast

def main():
    print(sys.argv)
    print(os.getenv('TARGET_LIST'))
    
    sanity_format = "sanity.{}"
    formattedTests = []
    
    targetNames = ast.literal_eval(os.getenv('TARGET_LIST'))
    
    print(targetNames)
    
    for argument in targetNames:
        print(argument)
        formattedTests.append(sanity_format.format(argument))
    
    allTests = ','.join(formattedTests)    
    testTargets = 'TESTLIST={}'.format(allTests)
    
    print(testTargets)
    
    print('::set-output name=test_targets_str::{}'.format(testTargets))

if __name__ == "__main__":
    main()
