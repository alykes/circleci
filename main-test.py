#import the add function and ensure it is working correctly
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 10
        assert Add(8,8) == 100
        print("Add funtion is working correctly")

if __name__ == '__main__':
        TestAdd()
