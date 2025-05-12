from app import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
    print("Test passed!")
    
if __name__ == "__main__":
    test_hello_world()
