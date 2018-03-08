import xml.etree.ElementTree as ET
import argparse

def main(file_name):
    import xml.etree.ElementTree as ET
    tree = ET.parse(file_name)
    root = tree.getroot()

    for testsuite in root.iter('testsuite'):
        numberFailed = 0;
        for neighbor in testsuite.iter('testcase'):
            print (neighbor)
            # time = "0.094"
            neighbor.set('time', '0.1')
            failure = neighbor.find('failure')

            if failure is not None:
                print ("Has failure element")
                neighbor.remove(failure)
                failure.set('message', failure.text)
                neighbor.append(failure)
                numberFailed += 1;
        testsuite.set('failures', str(numberFailed))

    tree.write('testresults/junit/junitformatted.xml')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, dest='file_name',
                        help='File Name to add time to.')

    args = parser.parse_args()

    main(args.file_name)
