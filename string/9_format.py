'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title :  Write a Python program to display formatted text (width=50) as output.

'''
import textwrap
def format_text(text , width = 50):
    words = text.split()
    lines =[]
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= width:
            current_line += word +' '
        else:
            lines.append(current_line.strip())
            current_line = word+ ' '
    lines.append(current_line.strip())
    format_text = '\n' .join(lines)
    return format_text
    # formatted_text = textwrap.wrap(text,width=width)
    # f_text = '\n'.join(formatted_text)
    # return formatted_text
def main():
    input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    output = format_text(input_text)
    print(f" {output}")
if __name__ =="__main__":
    main()
