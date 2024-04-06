## AirBnB Clone Console - User Guide

This document outlines the initial stages of a project to create a command-line interface (CLI) for an AirBnB clone application. The CLI allows users to manage data programmatically.

**Project Structure**

The core functionalities are implemented in the following files:

* `models/base_model.py`: Defines a base class for all other model classes.
* `models/engine/file_storage.py`: Handles persistent file storage.
* `console.py`: Provides the command-line interface for user interaction.
* Additional class files are created for specific data types (e.g., `User`, `Place`, etc.)

**Getting Started**

1. Clone this repository.
2. Locate the `console.py` file and run it: 

```
./console.py
```

3. You should see the `(hbnb)` prompt, indicating you're in the AirBnB console.

**Commands**

The console supports various commands to manage data objects. Here's a summary:

* **create <class_name>**: Creates a new instance of the specified class.
* **destroy <class_name> <id>**: Deletes an existing object based on class and ID.
* **show <class_name> <id>**: Displays details of a specific object.
* **all**: Shows all objects stored or all objects of a particular class (if specified).
* **update <class_name> <id>**: Updates attributes of an existing object.
* **quit**: Exits the console program.

**Advanced Syntax**

The console also supports an alternative syntax using class methods:

* `<class_name>.all()`: Retrieves all objects of a class.
* `<class_name>.destroy(<id>)`: Deletes an object based on ID.
* `<class_name>.update(<id>, <attribute_name>, <attribute_value>)`: Updates a specific attribute of an object.
* `<class_name>.update(<id>, <dictionary>)`: Updates multiple attributes using a key-value dictionary.

**Examples**

**Primary Command Syntax**

1. **Create an object:**

```
(hbnb) create User
```

2. **Show an object:**

```
(hbnb) show User 98bea5de-9cb0-4d78-8a9d-c4de03521c30
```

3. **Destroy an object:**

```
(hbnb) destroy User 99f45908-1d17-46d1-9dd2-b7571128115b
```

4. **Update an object:**

```
(hbnb) update User 98bea5de-9cb0-4d78-8a9d-c4de03521c30 name "Todd the Toad"
```

**Alternative Syntax**

1. **Show all User objects:**

```
(hbnb) User.all()
```

2. **Destroy a User:**

```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
```

3. **Update User (by attribute):**

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name="Fred the Frog")
```

This guide provides a basic understanding of the AirBnB clone console's functionalities. Refer to the codebase for further details and class-specific information.testing repo
