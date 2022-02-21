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
  output="".join(lines)
  print(output)
  ## prove
  with open("output.md",'w') as f:
    f.write("function|example\n")
    f.write("--------|-----\n")
    f.write("sample |"+output+"\n")

if __name__=="__main__":
  import sys
  if len(sys.argv) < 2: print("Format: python go2md.py filepath")
  else: go2md(sys.argv[1])
