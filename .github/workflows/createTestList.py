import sys
import os

def main():
    print(sys.argv)
    print(os.getenv('TEST_LIST'))
    
    sanity_format = "sanity.{}"
    formattedTests = []
    
    for argument in os.getenv('TEST_LIST'):
        formattedTests.append(sanity_format.format(argument))
    
    allTests = ','.join(formattedTests)    
    testTargets = 'TESTLIST={}'.format(allTests)
    
    print(testTargets)
    
    print('::set-output name=test_targets_str::{}'.format(testTargets))

if __name__ == "__main__":
    main()
