import re

class TestSuite():
    
    def __init__(self):
        self.forbidden = {
            'py':{
                #Don't use print
                "print":r"print\(",
                #Don't clutter my namespace
                "import star":r"from\s.*?\simport\s\*",
                #Don't use \ to continue a statmen to the next line.
                #Use implicit continuation via parens (...\n...)
                "backslash continue":r"\\\s*$" },
         'lua':{}   
        }


    def run(self, files):
        err = 0
        for file_name in files:
            try:
                result = 0
                result = self.check_file(file_name)
                if result == 1:
                    err = 1
            except Exception as _ee:
                print(_ee)
        return err
        
    def check_file(self, file_name):
        file_type = self.get_type(file_name)
        err = 0
        if file_type in self.forbidden:
            line_num = 0
            with open(file_name, 'r') as code:
                for line in code:
                    line_num += 1
                    for key, regex in self.forbidden[file_type].items():
                        if re.search(regex, str(line)):
                            print("\n"+("-"*24)+file_name+("-"*24))
                            print("The use of "+key+" is forbidden")
                            print(str(line_num)+": "+line+"\n")
                            err = 1
            return err
        else:
            return 0
            
    def get_type(self, file_name):
        _languages = {"python":"py", "lua":"lua"}
        
        file_type = re.search(r"\.(py)|(lua)$", file_name).group(1)
        if file_type:
            return file_type
        else:
            with open(file_name) as f:
                first_line = f.readline()
                shabang = re.search(r"^#!/.*([Pp]ython)|([Ll]ua)", first_line).group(1)
                if shabang:
                    return _languages[str.lower(shabang)]
        return None
