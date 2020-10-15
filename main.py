# Import modules
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range as range
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.simple as simple_for
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.nested_loop.nested as nested
import basics.repetitions.while_loop.ascii as ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as simple_while
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.nested_decision.nested as nested_decision
import basics.decisions.simple_decisions.comparison_operators as comparison_operators
import basics.decisions.simple_decisions.counter as counter
import basics.decisions.simple_decisions.if_elif_else as if_elif_else
import basics.decisions.simple_decisions.if_else as if_else
import basics.decisions.simple_decisions.if_decision as if_decision
import basics.decisions.simple_decisions.modulo_operator as modulo_operator
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.decision_review as decision_review
import basics.modules.guess_the_number as guess_the_number
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop 
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values_function
import basics.functions.simple_function as simple_function


# Define function to import modules
def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()
  if (response == "simple message"):
    simple_message.run()
  elif (response == "multiline message"):
    multiline_message.run()
  elif (response == "escape characters"):
    escape_characters.run()
  elif (response == "ascii robot"):
    ascii_robot.run()
  elif (response == "data types"):
    data_types.run()
  elif (response == "string operators"):
    string_operators.run()
  elif (response == "user input"):
    user_input.run()
  elif (response == "characters"):
    characters.run()
  elif (response == "count down"):
    count_down.run()
  elif (response == "membership operators"):
    membership_operators.run()
  elif (response == "range"):
    range.run()
  elif (response == "reverse"):
    reverse.run()
  elif (response == "simple for") or (response == "simple for loop"):
    simple_for.run()
  elif (response == "nesting"):
    nesting.run()
  elif (response == "nested"):
    nested.run()
  elif (response == "ascii"):
    ascii.run()
  elif (response == "count"):
    count.run()
  elif (response == "factorial"):
    factorial.run()
  elif (response == "len"):
    len.run()
  elif (response == "simple while") or (response == "simple while loop"):
    simple_while.run()
  elif (response == "sum 100"):
    sum_100.run()
  elif (response == "sum user") or (response == "sum user numbers"):
    sum_user_numbers.run()
  elif (response == "nestception"):
    nestception.run()
  elif (response == "nested decision"):
    nested_decision.run()
  elif (response == "comparison operators"):
    comparison_operators.run()
  elif (response == "counter"):
    counter.run()
  elif (response == "if elif else"):
    if_elif_else.run()
  elif (response == "if else"):
    if_else.run()
  elif (response == "if"):
    if_decision.run()
  elif (response == "modulo"):
    modulo_operator.run()
  elif (response == "and operator"):
    and_operator.run()
  elif (response == "decision review"):
    decision_review.run()
  elif (response == "or operator"):
    or_operator()
  elif (response == "guess the number"):
    guess_the_number.run()
  elif (response == "ascii character"):
    ascii_character.run()
  elif (response == "ascii code"):
    ascii_code.run()
  elif (response == "function calls") or (response == "function call"):
    function_calls.run()
  elif (response == "function with loop"):
    function_with_loop.run()
  elif (response == "function with nesting"):
    function_with_nesting.identify()
  elif (response == "function with parameter"):
    function_with_parameter.run()
  elif (response == "function with parameters"):
    function_with_parameters.run()
  elif (response == "multiple functions"):
    multiple_functions.create_ladder()
  elif (response == "return values"):
    return_values_function.run()
  elif (response == "simple function"):
    simple_function.listen()



# Define function to navigate by
def run():
  is_running = True

  while(is_running):
    print("What would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[q] Quit")
    response = input()

    if (response == "a"):
      run_block_a()
      print("\n+ + + program complete + + +\n")
    elif (response == "q"):
      break
    else:
      print("Invalid option! Please try again.")

run()