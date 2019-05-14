Create Module.
Preconditions: 
  - Assume file you create is called "myModule.py"
  - File must have ".py" extension
  - Save .py file in a location accessible by your new Python code. 
  - When using a function from a module, use the syntax: module_name.function_name.
Main Success Scenario:
  1. Create myModule.py file. 
  2. Paste below code in the file and save changes
        def greeting(name):
          print("Hello, " + name) 
  3. Use new module
        import mymodule

        mymodule.greeting("Jonathan")
          
