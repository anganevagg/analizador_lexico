import re

# simbolos de la gramatica

# gramatica del programa
re_expr = r"[0-9]*"
re_expr = f"({re_expr}\+{re_expr})|({re_expr}\-{re_expr})"
re_stmt = fr"{re_expr}"
re_stmt_lst = fr""
re_stmt_lst += fr"({re_stmt};{re_stmt_lst};)|({re_stmt})"
re_stmt = fr"{re_stmt_lst}"
re_program = fr"{re_stmt_lst}"
results = re.finditer(re_program, "1+11;1-1;2+2;2+2;2+2;")

for result in results:
	print(result.group())