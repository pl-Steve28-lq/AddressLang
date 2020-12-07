# AddressLang
Esolang similar with Internet address!

## How to code AddressLang?
AddressLang is looks like strange Internet address.

### Init
```
(http or https) :// (Your program name, author, etc..) /
ex) https://HelloWorld.Steve28.com/
```
> http : Pass the unknown letter.<br>
> https : Strict check. If unknown letter detected, then raise CompileError.

### Code
Code Blocks are divided by `/` keyword.<br><br>

> Commands : Plus, Minus, Left, Right, Print, Input, Jump<br>

Plus ~ Input has same logic in BrainF\*\*k, `+ - > < . ,`.<br>
Jump command save value of memory that pointer points, and jump (saved memory + 1) th block at the code block ends.<br><br><br>

> Alphabet
a = Plus, b = Minus, c = Left, d = Right, e = Print, f = Input, g = Jump, h is Plus again, and go on.<br>
Capital Letters are replaced by Lower Letters.
