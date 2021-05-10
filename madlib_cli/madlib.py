import os
import re

def welcome():
    print(f"""
    ***************************************   welcome in the Madlib Game .... *************************************
    in this game i will ask you to enter some thing
    lets go .....
    """)
# welcome()
call_path="assets/madlib_template.txt"
# f= open("madlib_cli/madlib_template.txt", "r")
def read_template(path):
    # with open("assets/madlib_template.txt", "r") as f:        # To automaticly close the file when we exit this block
    #     f_content=f.read()
    #     print(f_content)
  if os.path.exists(path):
    with open(path, 'r') as f:
      content = f.read()
      return content
  else:
    raise FileNotFoundError("path does not exist")
    
# read_template("../assets/madlib_template.txt")
    
def parse_template(content):
  """To  take in the contents of a file and finds all the words between curly braces And returns the string without those words and a tuple that house all the words found withon the curly braces
  """
  stripped_words = tuple(re.findall("(?<={).+?(?=})",content))

  content = re.sub("(?<={).+?(?=})", '', content)
    
  return content, stripped_words
content, stripped_words = parse_template(read_template('assets/madlib_template.txt'))
# parse_template(read_template('assets/madlib_template.txt'))

def get_user_inputs(stripped_words):
  """ stakes the words stripped out of the content and replaces each word with user input
  """

  user_input_list = []

  for word in stripped_words:
    user_input = input(f'Input {word}: ')

    if user_input.lower() == 'quit':
      return print('You have ended the game! Bye')
    else:
      user_input_list.append(user_input)

  return tuple(user_input_list)


def merge(content,tuple_of_words):
  """will take in the contents of a file and a tuple of words(i.e Noun, adj, etc.). It returns the content with the new words entered
  """
  for word in tuple_of_words:
    content = re.sub("{(.*?)}", word, content, 1)
      
  return content
  
  
def write_template(content):
  """writes content to a file
  """
  tmp_file_path = 'assets/madlib_template_output.txt'
  try:
    os.remove(tmp_file_path)
  except FileNotFoundError:
    pass

  with open('assets/madlib_template_output.txt', 'w') as story:
     story.write(content)

  return tmp_file_path


welcome()
read_template('assets/madlib_template.txt')
content, stripped_words = parse_template(read_template('assets/madlib_template.txt'))
new_words = get_user_inputs(stripped_words)
new_content = merge(content,new_words)
write_template(new_content)
print(new_content)