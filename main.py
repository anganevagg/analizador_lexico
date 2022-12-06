import re

re_blank_space = r"(( |\n|\t)*)"
re_braquet_open = r"\("
re_braquet_close = r"\)"
re_sqr_braquet_open = r"\["
re_sqr_braquet_close = r"\]"
re_key_open = r"\{"
re_key_close = r"\}"

re_var_logic_comp = r"<=|<|==|>|>="

re_boolean = r"(true|false)"
re_int = r"[0-9]*"
re_float = rf"{re_int}.{re_int}"
re_while = r"while"


re_aritmetic_operation_stmt = rf"{re_int}|{re_float}(+|-|\*|/|%)"

re_condition_expr = f"(|{re_boolean})()*"
re_var = r"var [a-zA-Z]*"
re_var_stmt = fr"{re_var}{re_blank_space}(=({re_blank_space}({re_boolean}|{re_int}|{re_float})|({re_condition_expr})))*"
re_expr = fr"({re_var_stmt}{re_blank_space};{re_blank_space})*"

re_while_stmt = f"{re_while}{re_braquet_open}{re_condition_expr}{re_braquet_close}{re_blank_space}{re_key_open}{re_blank_space}{re_expr}{re_blank_space}{re_key_close}"


text = """
var i = 1;
while(true)
{
  var a = 10.5;
	var c = true;
	var d= 1*3;
}
"""

regex = {
	"while statement": re_while_stmt,
	"var assignation": re_var_stmt,

}

for k,v in regex.items():
	for i in re.finditer(regex[k], text):
		print(f"found {k} in positions {i.start()} to {i.end()} with content: \n{i.group()}")
