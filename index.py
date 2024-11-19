import time

def call_three_times(func):
    def wrapper_function( *args, **keyword_args ):
        print( func( *args, **keyword_args ) )
        print( func( *args, **keyword_args ) )
        print( func( *args, **keyword_args ) )
    return wrapper_function


def runtime(func):
    def wrapper( *args, **kargs ):
        start_time = int(time.time())
        returned_item = func(*args, **kargs)
        end_time = int(time.time())
        total_runtime = end_time - start_time
        print( f"RUNTIME: {total_runtime}" )
        return returned_item

    return wrapper


@call_three_times
def say_howdy():
    return "howdy howdy howdy"

@call_three_times
def say_oogla_boogla():
    return "oogla boogla"

@runtime
@call_three_times
@runtime
def declare_something(string):
    return f"I DECLARE {string}"

@runtime
def divide(first_num, second_num):
    time.sleep(5)
    return first_num / second_num

def call_twice( function, *args, **keyword_args ):
    print( function( *args, **keyword_args ) )
    print( function( *args, **keyword_args ) )