import sys

def main():
    print(sys.argv)

    sanity_format = "sanity.{}"
    foramttedTests = []
    
    for argument in sys.argv:
        formattedTests.append(sanity_format.format(argument))
    
    allTests = formattedTests.join(',')
    testTargets = 'TESTLIST={}'.format(allTests)
    
    print(testTargets)
    
    print('::set-output name=test_targets_str::{}'.format(testTargets))


if __name__ == "__main__":
    main()
