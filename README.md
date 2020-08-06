# PHPUnserializeTool
A simple tool for PHP unserialize


## Use

* `python3 tool.py`

## Example

```txt
Input PHP class name:test              
Input class variables numbers:4
Input 1 var([[role|]type|]name|value):a|a
Input 2 var([[role|]type|]name|value):protected|s|b|bb
Input 3 var([[role|]type|]name|value):private|s|c|ccc
Input 4 var([[role|]type|]name|value):default|i|d|12345
unserialize = O:4:"test":4:{s:1:"a";s:1:"a";s:4:"\x00*\x00b";s:2:"bb";s:7:"\x00test\x00c";s:3:"ccc";s:1:"d";i:12345;}
payload(origin) = O:4:"test":5:{s:1:"a";s:1:"a";s:4:"\x00*\x00b";s:2:"bb";s:7:"\x00test\x00c";s:3:"ccc";s:1:"d";i:12345;}
payload(url) = O:4:"test":5:{s:1:"a";s:1:"a";s:4:"%00*%00b";s:2:"bb";s:7:"%00test%00c";s:3:"ccc";s:1:"d";i:12345;}
payload(x1) = O:+4:"test":+5:{s:+1:"a";s:+1:"a";s:+4:"\x00*\x00b";s:+2:"bb";s:+7:"\x00test\x00c";s:+3:"ccc";s:+1:"d";i:+12345;}
payload(base64) = Tzo0OiJ0ZXN0Ijo1OntzOjE6ImEiO3M6MToiYSI7czo0OiIAKgBiIjtzOjI6ImJiIjtzOjc6IgB0ZXN0AGMiO3M6MzoiY2NjIjtzOjE6ImQiO2k6MTIzNDU7fQ==
payload(x1|base64) = TzorNDoidGVzdCI6KzU6e3M6KzE6ImEiO3M6KzE6ImEiO3M6KzQ6IgAqAGIiO3M6KzI6ImJiIjtzOis3OiIAdGVzdABjIjtzOiszOiJjY2MiO3M6KzE6ImQiO2k6KzEyMzQ1O30=
```

* `role` mean the property modifier ==> ['default','protected','private']

  sure u can input 'pro' for `protected` and 'pri' for `private`
  
* `type` mean the property type ==> ['s','d','N'] 
  
  s => string
  
  d => double
  
  n => NULL
 
 * `name` is the property name and `value` is it's value
