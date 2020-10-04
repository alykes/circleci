#import the add function and ensure it is working correctly
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 11
        print("Add funtion is working correctly")

if __name__ == '__main__':
        TestAdd()
