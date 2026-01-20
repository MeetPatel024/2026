class solution:
    def prec(self,ch):
        if ch=="+" or ch=="-":
            return 1
        if ch=="/" or ch=="*":
            return 2
        if ch=="^":
            return 3
        return 0
    
    def InfixToPostfix(self,s):
        stack = []
        result = []

        for char in s:
            if ("a"<=char <="z") or ("A"<=char<="Z") or ("0"<=char<="9"):
                result.append(char)
            elif char=="(":
                stack.append(char)
            elif char==")":
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.prec(stack[-1]) >=self.prec(char):
                    result.append(stack.pop())
                stack.append(char)
        
        while stack:
            result.append(stack.pop())
        return ("".join(result))

x = "((a+b)^c)*u"
y="a^(b^c)"
p1 = solution()
s1=p1.InfixToPostfix(x)
s2=p1.InfixToPostfix(y)
print(s1)
print(s2)
