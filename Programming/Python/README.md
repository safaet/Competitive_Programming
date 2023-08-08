| Topic                   | Syntax and Examples                             |
|-------------------------|------------------------------------------------|
| **Basic Syntax**        |                                                |
| Print to console        | `print("Hello, world!")`                        |
| Variable assignment     | `x = 10`                                       |
| Conditional statement  | `if x > 5:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("x is greater than 5")` |
| Looping                 | `for i in range(5):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(i)` |
| **Data Types**          |                                                |
| Integer                 | `int_var = 42`                                 |
| Float                   | `float_var = 3.14`                             |
| String                  | `str_var = "Hello"`                            |
| Boolean                 | `bool_var = True`                              |
| **Lists and Tuples**    |                                                |
| List                    | `my_list = [1, 2, 3]`                          |
| Tuple                   | `my_tuple = (1, 2, 3)`                         |
| **Dictionaries**        |                                                |
| Dictionary              | `my_dict = {"key": "value"}`                   |
| **Functions**           |                                                |
| Define a function       | `def add(a, b):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b` |
| Call a function         | `result = add(3, 4)`                          |
| **Control Flow**        |                                                |
| If statement            | `if condition:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code` |
| If-else statement       | `if condition:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code` |
| **Loops**               |                                                |
| For loop                | `for item in sequence:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code` |
| While loop              | `while condition:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code` |
| **List Comprehensions** |                                                |
| Create a new list       | `squared = [x**2 for x in range(10)]`          |
| **String Manipulation** |                                                |
| Slicing a string        | `substring = my_string[0:5]`                  |
| String length           | `length = len(my_string)`                     |
| String formatting       | `formatted = f"Value: {x}"`                   |
| **Classes and Objects** |                                                |
| Define a class          | `class MyClass:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self, value):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self.value = value` |
| Create an object        | `obj = MyClass(10)`                           |
| Access object attribute | `obj.value`                                   |
| **Modules and Packages**|                                                |
| Import a module         | `import module_name`                          |
| Import specific object  | `from module_name import function`            |
| **Exception Handling**  |                                                |
| Try-except block        | `try:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code`<br>`except ExceptionType:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`# Code` |
| **File Handling**       |                                                |
| Read from a file        | `with open("file.txt", "r") as file:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`content = file.read()` |
| Open a file  (other method) | `fileref = open("fileName.txt", "r")`  |
| Close a file          | `fileref.close()`|
| Read full file           | `fileref.read()`  |
| Read file line by line   | `lines = fileref.readlines()` <br> `for line in lines: ` <br>&nbsp;&nbsp;&nbsp;&nbsp; `print(line)`|
| Remove empty line     | `print(line.strip())` |
| Write to a file       |  `fileref = open("fileName.txt", "w")` <br> `fileref.write(value)`  |
| Using with to open files |  `fname = 'mydata.txt'` <br> `with open(fname, 'w') as md:` <br>&nbsp;&nbsp;&nbsp;&nbsp; `for num in range(10):` <br>&nbsp;&nbsp;&nbsp;&nbsp; `md.write(str(num))` <br>&nbsp;&nbsp;&nbsp;&nbsp; `md.write('\n)`
| **Virtual Environment** |                                                |
| Create virtual env      | `python -m venv env_name`                     |
| Activate env            | `source env_name/bin/activate` (Linux/macOS)  |
| Deactivate env          | `deactivate`                                  |
| **Pip (Package Manager)**|                                               |
| Install a package       | `pip install package_name`                    |
| Example: requests       | `pip install requests`                        |
| **Comments**            |                                                |
| Single-line comment     | `# This is a single-line comment`             |
| Multi-line comment      | `"""`<br>&nbsp;&nbsp;`This is a`<br>&nbsp;&nbsp;`multi-line comment`<br>`"""` |
| **Useful Libraries**    |                                                |
| requests                | HTTP requests                                 |
| numpy                   | Numerical operations                          |
| pandas                  | Data manipulation                             |
| matplotlib              | Data visualization                           |
| tkinter                 | GUI toolkit                                  |
| datetime                | Date and time manipulation                   |
| os                      | Operating system interface                   |
| random                  | Random number generation                     |
