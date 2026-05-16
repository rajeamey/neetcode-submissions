class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["4","13","5","/","+"]
        elements = []
        for token in tokens:
            if token not in ["+", "-", "/", "*"]:
                elements.append(token)
            else:
                if elements:
                    first = elements.pop()
                    second = elements.pop()
                    elements.append(str(int(eval(token.join([second, first])))))

        return int(elements[0])