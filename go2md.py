# In: golang code
# Out: one line for md(markdown) table format.
# Tips: Replaced as the following rules.
# \t: &nbsp;&nbsp;&nbsp;
# \n: <br>
def go2md(filepath):
  lines=[]
  with open(filepath,'r') as f:
    for line in f.readlines():
      lines.append(line.replace("\t","&nbsp;&nbsp;&nbsp;").replace("\n","<br>"))
  return "".join(lines)

if __name__=="__main__":
  import sys
  if len(sys.argv) < 3: print("Format: python go2md.py xxx.go")
  go2mod(sys.argv[2])
