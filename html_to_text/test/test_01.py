# add parent directory to path.
import sys 
sys.path.append("..")

# import module.
from html_to_text import *

def main():
    
    h2t = HtmlToText()
    
    print("-----")
    print(h2t.text("sample_files/testLists.html"))
    
    print("-----")
    print(h2t.text("<p class='hi'>Hello World!</p>", is_raw=True))
    
    print("-----")
    html = open("sample_files/test.html").read()
    soup = ModifyHTML(html, "html5lib")
    soup.shift_links()
    soup.remove_images()
    print(h2t.text(str(soup), is_raw=True))

if __name__ == "__main__":
    main()

