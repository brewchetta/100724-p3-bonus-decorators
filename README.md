# Class Methods, and Attributes

## Learning Goals

- Class attributes

- Class methods

## Exercises

### Class Methods / Attributes

1. Give the `Fish` a class attribute `all_fish` which starts as an empty list.

2. When a new `Fish` is created, append it to `Fish.all_fish`.

3. Create a new class method `num_fish` which returns the length of `Fish.all_fish`.

4. Create a class method `all_fish_names` which returns a list of all the names for `Fish` instances. *HINT: You can use list comprehension for this!*

5. Create a class method `average_length` which returns the average length in inches for all `Fish` instances. *HINT: The average is the sum of lengths / number of fish. There are several ways of getting the average in Python...*

## Questions to Ask Yourself

1. What is the difference between a class and an instance?

2. How can we define a class attribute? What is the scope of a class attribute?

3. What happens if an instance also creates an attribute with the same name?

4. How is a class method declared? What is the scope of a class method?

5. When does it make sense to build a class method versus an instance method?