from typing import Any
from .fuzzy_rule import FuzzyRule
from .fuzzy_variable_output import FuzzyVariableOutput
from .fuzzy_variable_input import FuzzyVariableInput
import matplotlib.pyplot as plt


class FuzzySystem:
    """
    A type-1 fuzzy system based on Mamdani inference system
    Reference:
    ----------
    Mamdani, Ebrahim H., and Sedrak Assilian.
    "An experiment in linguistic synthesis with a fuzzy logic controller."
    Readings in Fuzzy Sets for Intelligent Systems. Morgan Kaufmann, 1993. 283-289.
    """
    def __init__(self) -> None:
        """
        Initializes fuzzy system.
        data structures required:
            input variables -- dict, having format {variable_name: FuzzyVariableInput, ...}
            output variables -- dict, having format {variable_name: FuzzyVariableOutput, ...}
            rules -- list of FuzzyRule
            output_distribution -- dict holding fuzzy output for each variable having format
                                {variable_name: FuzzySet, ...}
        """
        self.input_variables = {}   # a dict of input variables
        self.output_variables = {}  # a dict of output variables
        self.rules = []     # a list that contains FuzzyRules

    def __str__(self) -> str:
        """
        string representation of the system.
        Returns:
        --------
        str: str, string representation of the system in the form
                Input:
                input_variable_name(set_names)...
                Output:
                output_variable_name(set_names)...
                Rules:
                IF [antecedent clauses] THEN [consequent clauses]
        """
        ret_str = 'Input: \n'
        for n, s in self.input_variables.items():
            ret_str = ret_str + f'{n}: ({s})\n'
        ret_str = ret_str + 'Output: \n'
        for n, s in self.output_variables.items():
            ret_str = ret_str + f'{n}: ({s})\n'
        ret_str = ret_str + 'Rules: \n'
        for rule in self.rules:
            ret_str = ret_str + f'{rule}\n'
        return ret_str

    def add_input_variable(self, var: FuzzyVariableInput) -> None:
        """
        TODO:
         Add a FuzzyVariableInput `var` to `self.input_variables`
        :param var: the input fuzzy variable
        """
        # Write the code below

        pass

    def add_output_variable(self, var: FuzzyVariableOutput) -> None:
        """
        TODO:
         Add a FuzzyVariableOutput `var` to `self.output_variables`
        :param var: the output fuzzy variable
        """
        # Write the code below

        pass

    def get_input_variable(self, name: str) -> FuzzyVariableInput:
        """
        TODO:
         Get a FuzzyVariableInput given by `name`
        :param name: name of variable
        """
        var = None
        # Write your code below

        return var

    def get_output_variable(self, name: str) -> FuzzyVariableOutput:
        """
        TODO:
         Get a FuzzyVariableOutput given by `name`
        :param name: name of variable
        """
        var = None
        # Write your code below

        return var

    def clear_output_distributions(self) -> None:
        """
        Used for each iteration. The fuzzy result is cleared
        """
        map(lambda output_var: output_var.clear_output_distribution(), self.output_variables.values())

    def add_rule(self, antecedent_clause_names: dict, consequent_clause_names: dict) -> None:
        """
        TODO:
         Adds a new rule to the system from dictionaries of antecedent and consequent clause names
        :param antecedent_clause_names: a dict of clause, having the form {variable_name: set_name, ...}
        :param consequent_clause_names: having the form {variable_name: set_name, ...}
        """
        # create a new rule
        new_rule = FuzzyRule()
        # add antecedent clauses
        for var_name, set_name in antecedent_clause_names.items():
            # write your code here
            # get the input variable and corresponding fuzzy set for the antecedent clause
            # and then add the clause to `new_rule`

            pass

            # add consequent clauses
            for var_name, set_name in consequent_clause_names.items():
                # write your code here
                # get the output variable and corresponding fuzzy set for the consequent clause
                # and then add the clause to `new_rule`

                pass

        # add the new rule

        pass

    def evaluate_output(self, input_values: Any) -> Any:
        """
        Executes the fuzzy inference system for a set of inputs
        :param input_values: a dict containing the inputs to the systems in the form {input_variable_name: value, ...}
        :return: a dict, containing the outputs from the systems in the form {output_variable_name: value, ...}
        """
        # clear the fuzzy consequences as we are evaluating a new set of inputs.
        # can be optimized by comparing if the inputs have changes from the previous
        # iteration.
        self.clear_output_distributions()
        # Fuzzify the inputs. The degree of membership will be stored in each set
        for input_name, input_value in input_values.items():
            self.input_variables[input_name].fuzzify(input_value)
        # evaluate rules
        for rule in self.rules:
            rule.evaluate()
        # finally, defuzzify all output distributions to get the crisp outputs
        output = {}
        for output_var_name, output_var in self.output_variables.items():
            output[output_var_name] = output_var.get_crisp_output()
        return output

    def evaluate_output_info(self, input_values: Any) -> Any:
        """
        Executes the fuzzy inference system for a set of inputs
        :param input_values: a dict containing the inputs to the systems in the form {input_variable_name: value, ...}
        :return: a dict containing the outputs from the systems in the form {output_variable_name: value, ...}
        """
        info = {}
        # clear the fuzzy consequences as we are evaluating a new set of inputs.
        # can be optimized by comparing if the inputs have changes from the previous
        # iteration.
        self.clear_output_distributions()
        # Fuzzify the inputs. The degree of membership will be stored in
        # each set
        fuzzification_info = []
        for input_name, input_value in input_values.items():
            fuzzification_info.append(self.input_variables[input_name].fuzzify_info(input_value))
        info['fuzzification'] = '\n'.join(fuzzification_info)
        # evaluate rules
        rule_info = []
        for rule in self.rules:
            rule_info.append(rule.evaluate_info())
        info['rules'] = '\n'.join(rule_info)
        # finally, defuzzify all output distributions to get the crisp outputs
        output = {}
        for output_var_name, output_var in self.output_variables.items():
            output[output_var_name], info = output_var.get_crisp_output_info()
        return output, info

    def plot_system(self):
        total_var_count = len(self.input_variables) + len(self.output_variables)
        if total_var_count < 2:
            total_var_count = 2
        fig, axs = plt.subplots(total_var_count, 1)
        fig.tight_layout(pad=1.0)
        for idx, var_name in enumerate(self.input_variables):
            self.input_variables[var_name].plot_variable(ax=axs[idx], show=False)
        for idx, var_name in enumerate(self.output_variables):
            self.output_variables[var_name].plot_variable(ax=axs[len(self.input_variables) + idx], show=False)
        plt.show()
