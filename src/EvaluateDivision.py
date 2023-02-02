from typing import List


class Solution:
    varStack = [];
    valStack = [];
    varSet = set();
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answers = [];
        self.varStack = [];
        invertedEquations = [];
        invertedValues = [];
        for index, equation in enumerate(equations):
            innerEq = [equation[1], equation[0]];
            invertedEquations.append(innerEq);
            invertedValues.append(1 / values[index]);
            self.varSet.add(equation[1]);
            self.varSet.add(equation[0]);

        for query in queries:
            #print(query[0] + '/' + query[1]);

            if query[0] == query[1]:
                if query[0] in self.varSet:
                    answers.append(1);
                else:
                    answers.append(-1);
                continue;
            self.varStack = [];
            self.valStack = [];
            self.addToStackUntilDenominator(query[0], query[1], equations, values);
            #print(self.varStack);
            product = 1;
            if len(self.varStack) > 0 and self.varStack[0][0] == query[0] and self.varStack[len(self.varStack) - 1][
                1] == query[1]:
                for value in self.valStack:
                    product *= value;
                answers.append(product);
            else:
                self.varStack = [];
                self.valStack = [];
                self.addToStackUntilDenominator(query[0], query[1], invertedEquations, invertedValues);
                if len(self.varStack) > 0 and self.varStack[0][0] == query[0] and self.varStack[len(self.varStack) - 1][
                    1] == query[1]:
                    for value in self.valStack:
                        product *= value;
                    answers.append(product);
                else:
                    answers.append(-1);
        return answers;

    def addToStackUntilDenominator(self, numerator: str, denominator: str, equations: List[List[str]],
                                   values: List[float]) -> List[int]:
        for index, equation in enumerate(equations):
            if numerator == equation[0]:
                self.varStack.append(equation);
                self.valStack.append(values[index]);
                if denominator == equation[1]:
                    return;
                else:
                    self.addToStackUntilDenominator(equation[1], denominator, equations, values);


sol = Solution();
'''print(sol.calcEquation([["b", "c"], ["a", "b"], ["c", "d"]], [2.0, 3.0, 6.0],
                 [["a", "d"], ["b", "a"], ["a", "e"], ["a", "a"], ["a", "b"], ["x", "x"]]));'''
print(sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                       [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]));
print(sol.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],
                        [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]));
print(sol.calcEquation([["a","b"]],[0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]));