import os
import re

def welcome():
    print(f"""
    ***************************************   welcome in the Madlib Game .... *************************************
    in this game i will ask you to enter some thing
    lets go .....
    """)
welcome()
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
    
read_template(call_path)
    
def parse_template(content):
  """To  take in the contents of a file and finds all the words between curly braces And returns the string without those words and a tuple that house all the words found withon the curly braces
  """
  stripped_words = tuple(re.findall("(?<={).+?(?=})",content))

  content = re.sub("(?<={).+?(?=})", '', content)
    
  return content, stripped_words
content, stripped_words = parse_template(read_template('assets/madlib_template.txt'))
# parse_template(read_template('assets/madlib_template.txt'))