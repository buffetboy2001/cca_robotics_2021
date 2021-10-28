# Let's Learn Basic Python

Python can be a wonderfully basic computer programming language. It can be used to create very complex, professional computer programs, but it can also be used to learn how to program a computer. It's a great place to start before trying to learn a more complex language like C++ or Java. Let's walk through some basic commands and get comfortable with Python.

You'll need Visual Studio Code on your computer for this tutorial. Open Code and then start a new file. Save that new file with the name: `learning_python.py`.

## Strings and Displaying Them

A `string` is any collection of letters and numbers. It can be a phrase, a sentence, or even a single character. In Python, you create `strings` like this.

```python
my_string = "hello world"
```

It's that simple. In your python code, you now have a variable `my_string` that has the value of `hello world`.

Try it in Code.

Now, let's display the value stored in the variable. You do that using the `print` command, like this:

```python
print(my_string)
```

Put those two lines together in Code and run the program.

```python
my_string = "hello world"
print(my_string)
```

## Working with Numbers

Now let's learn about numbers and mathematical operators. In python you can also set variable to a numeric value like this:

```python
my_number = 9
```

And you can display it again like you did the string:

```python
my_number = 9
print(my_number)
```

The mathematical operations are pretty simple to learn too. You just need to use `+`, `-`, `*`, `/`, & `=`.

```python
my_number = 3 + 6
```

```python
my_number = 12 - 3
```

```python
my_number = 3 * 3
```

```python
my_number = 27 / 3
```

All of these result in `my_number` having a value of `9`. Try them all in Code and make sure you use the `print` statement to see the result.

You can even use the normal algebraic rules to group mathematical operations together. Try this:

```python
my_value = (3 * 3) / 9 + 8
```

What value is this? Try it in Code.

## Functions

So far, our code has been running from the top of the file to the bottom. But, your python code may be starting to get a little messy with all the things you've tried.  What if you could organize your code and keep everything compartmentalized? You can do that! We call them functions and they look like this:

```python
def my_function():
```

Any lines of code that you want to be inside of the function must be tab indented. Like this:

```python
def my_function():
    my_value = (3 * 3) / 9 + 8
    print(my_value)
```

You can have as many functions as you want a your file. And you can use any name you want, so long as each function has its own unique name. Let's organize all the code you've written into functions.

```python
def print_a_string():
    my_string = "hello world"
    print(my_string)

def print_a_number():
    my_number = 9
    print(my_number)

print_a_string()
print_a_number()
```

But now see how the code works? What is calling your functions? It's not really top to bottom anymore, is it?

### Making Functions More Powerful

Now, functions are great for keeping your python code organized. But, they can do more than that. They can also be made to perform abstract logic. What if you could pass variables to a function and have logic that did something different with each new value that was passed to the function? Let's reuse the `print_a_string` function above and make it print *anything*.

```python
def print_a_string(this_string):
    print(this_string)

print_a_string("hello world")
print_a_string("One Fish, Two Fish, Red Fish, Blue Fish")
```

You can just keep calling your function and it will print each thing you send to it!

This is really powerful!

## The Comment

You can organize you python code with functions using the `def` statement. But, what if you want to leave yourself a note in your code that is just for you to read. You can do that with a comment using the `#` character. Like this:

```python
def print_a_string():
    my_string = "hello world"
    print(my_string)

def print_a_number():
    my_number = 9
    print(my_number)

# call the functions I wrote above
print_a_string()
print_a_number()
```

Anything after a `#` and on the same line will be ignored by python when you run your code. This is super handy for making notes in your code! Use comments!!

## `if-else` Statement

Computer programs ask us to build programs using a kind of logic called truth logic. We use truth statements to make our code do different things. This can involve testing variables for their values. We do this with `if` and `else` comparison statements. This is super powerful! Use it like this:

```python
a = 3
if a < 3:
    print("a is less than 3")
else:
    print("a is greater than or equal to 3")
```

Try this in Code. Which print statement will display when you run the code?

Now, put this into its own function also. Remember, this helps keep the code organized.

## The `main` Statement

So far, our code has been running from the top of the file to the bottom. And sometimes it jumps back up to a function we've written. But, there is a special function that we call the `main` that can be used to tell python where to start running your code. It has a strange sequence of letters, but that's ok. It looks like this:

```python
if __name__ == "__main__":
```

If you put this in your python code file, the code will start running right there at the `main` and *not at the top of the file*. This can be a really powerful way to organize your code. Like this:

```python
def print_a_string():
    my_string = "hello world"
    print(my_string)

def print_a_number():
    my_number = 9
    print(my_number)

# my logic starts here
if __name__ == "__main__":
    print_a_string()
    print_a_number()
    print("all done...bye-bye")
```

Try this in Code. What happens and why?

Most *good* python code will have a `main` function in it to keep things organized.

## The `import` Statement

What if you have python code in a file that is very nicely organized with functions. And you want to write more code but in a different file that calls those functions? That may sound odd, but it actually happens quite often as your python programs get larger. You can do this by using the `import` statement.

To try this, you'll need to open another file and save it as `more_python.py`. At the top of that file use the import statement like this:

```python
import learning_python
```

Once you have this in your code, you can call any function (`def`) that is in that file by using the name of the file and then a period. Like this:

```python
import learning_python

learning_python.print_a_string("I'm learning python!")
```

Good job! You've learned all of the basics that you'll need to read and write python code for your robot. Go forth and write code.

![](pics/python_thumbnail_small.jpg)

---

**Module Complete**
