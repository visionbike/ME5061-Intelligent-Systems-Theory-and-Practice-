from typing import Any
from .fuzzy_variable import FuzzyVariable
from .fuzzy_set import FuzzySet
from .fuzzy_clause import FuzzyClause


class FuzzyRule:
    """
    A fuzzy rule of type
    IF [antecedent clauses] THEN [consequent clauses]
    """

    def __init__(self) -> None:
        """
        Initializes the fuzzy rule
        Two data structures are necessary:
        1. Antecedent clauses list
        2. Consequent clauses list
        """
        self.antecedents = []   # list of antecedents clauses
        self.consequents = []   # list of consequents clauses

    def __str__(self) -> str:
        """
        String representation of the rule
        :return: string representation of the rule in the form IF [antecedent clauses] THEN [consequent clauses]
        """
        ante = ' and '.join(map(str, self.antecedents))
        cons = ' and '.join(map(str, self.consequents))
        return f'IF {ante} THEN {cons}'

    def add_antecedent_clause(self, var: FuzzyVariable, f_set: FuzzySet) -> None:
        """
        TODO:
         Creat new antecedent clause using FuzzyClause from `var` and `f_set`
         Then add the created antecedent clause to `self.antecendents`
        :param var: the clause variable in 'variable is set'
        :param f_set: another fuzzy set
        """
        clause = None
        # Write your code below

        pass

    def add_consequent_clause(self, var: FuzzyVariable, f_set: FuzzySet) -> None:
        """
        TODO:
         Creat new consequent clause using FuzzyClause from `var` and `f_set`
         Then add the created consequent clause to `self.consequents`
        Adds a consequent clause to the rule
        :param var: the clause variable in 'variable is set'
        :param f_set: another fuzzy set
        """
        clause = None
        # Write your code below

        pass

    def evaluate(self) -> None:
        """
        Evaluation of the rule.
        The antecedent clauses are executed and the minimum degree of membership is retained.
        This is used in the consequent clauses to min with the consequent set
        The values are returned in a dict of the form {variable_name: scalar min set, ...}
        :return: a dict resulting sets in the form {variable_name: scalar min set, ...}
        """
        # rule dom initialize to 1 as min operator will be performed
        rule_strength = 1
        # execute all antecedent clauses, keeping the minimum of the
        # returned doms to determine the rule strength
        for ante_clause in self.antecedents:
            rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)
        # execute consequent clauses, each output variable will update its output_distribution set
        for consequent_clause in self.consequents:
            consequent_clause.evaluate_consequent(rule_strength)

    def evaluate_info(self) -> str:
        """
        Evaluation of the rule.
        The antecedent clauses are executed and the minimum degree of membership is retained.
        This is used in teh consequent clauses to min with the consequent set
        The values are returned in a dict of the form {variable_name: scalar min set, ...}
        :return:  a dict that resulting sets in the form {variable_name: scalar min set, ...}
        """
        # rule dom initialize to 1 as min operator will be performed
        rule_strength = 1
        # execute all antecedent clauses, keeping the minimum of the
        # returned doms to determine the rule strength
        for ante_clause in self.antecedents:
            rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)
        # execute consequent clauses, each output variable will update its output_distribution set
        for consequent_clause in self.consequents:
            consequent_clause.evaluate_consequent(rule_strength)
        return f'{rule_strength} : {self}'
