Python is the best programming language to develop simple utilities thanks to its simpleness.
# pyutils
A collection of handy python utilites
### Functions
Func.|Input|Output
-----|:-----:|:-----:
file2list|A<br>B<br>C|['A','B','C']
list2file|['A','B','C']|A<br>B<br>C
file2byte||
byte2file||
runscript|'cd ~; mkdir test; touch hello.tx; cd -'|
string2datetime||
go2md|func main() {<br>&nbsp;&nbsp;&nbsp;var i interface{} = "hello"<br>&nbsp;&nbsp;&nbsp;s := i.(string)<br>&nbsp;&nbsp;&nbsp;fmt.Println(s)<br>&nbsp;&nbsp;&nbsp;s, ok := i.(string)<br>&nbsp;&nbsp;&nbsp;fmt.Println(s, ok)<br>&nbsp;&nbsp;&nbsp;f, ok := i.(float64)<br>&nbsp;&nbsp;&nbsp;fmt.Println(f)<br>}<br>|func main() {<\br>&\nbsp;&\nbsp;&\nbsp;var i interface{} = "hello"<\br>&\nbsp;&\nbsp;&\nbsp;s := i.(string)<\br>&\nbsp;&\nbsp;&\nbsp;fmt.Println(s)<\br>&\nbsp;&\nbsp;&\nbsp;s, ok := i.(string)<\br>&\nbsp;&\nbsp;&\nbsp;fmt.Println(s, ok)<\br>&\nbsp;&\nbsp;&\nbsp;f, ok := i.(float64)<\br>&\nbsp;&\nbsp;&\nbsp;fmt.Println(f)<\br>}<\br>

### Additioanl One-Line Functions
### Functions
Func.|Usage
-----|:-----:
list2string|"".join(items)|
