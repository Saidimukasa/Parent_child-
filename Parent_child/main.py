# Using the main Function to Call the Other Functions
from Parent import Parent
from Child import Child
def main():
    parent = Parent("John","Doe",45,"Male")
    child = Child("Jane","Doe",15,"Male")
    parent.Fullname()
    child.Childfull_name()  
main()