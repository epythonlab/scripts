// {header_file}

#include <iostream>
#include <string>

class {class_name} {
public:
    // Constructor
    {class_name}() {}

    // Getters and setters
{property_getters_setters}

private:
{property_declarations}
};

// Getters
{property_getters}

// Setters
{property_setters}

int main() {
    // Create an instance of {class_name}
    {class_name} obj;

    // Use getters and setters
    obj.set{name}("John Doe");
    obj.set{age}(30);
    obj.set{height}(1.75);

    std::cout << "Name: " << obj.get{name}() << std::endl;
    std::cout << "Age: " << obj.get{age}() << std::endl;
    std::cout << "Height: " << obj.get{height}() << std::endl;

    return 0;
}
