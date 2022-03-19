from typing import Any
from numpy.typing import NDArray
import numpy as np


class FuzzySet:
    precision: int = 3

    def __init__(self, name: str, domain_min: float, domain_max: float, res: int) -> None:
        """
        Initialize the fuzzy set
        :param name: name of the set
        :param domain_min: the minimum of the set
        :param domain_max: the maximum of the set
        :param res: the number of steps between the minimum and maximum value
        """
        self.domain_min = domain_min    # the minimum value of the value domain
        self.domain_max = domain_max    # the maximum value of the value domain
        self.res = res
        # initialize the domain values
        self.domain = np.linspace(domain_min, domain_max, res)  # a list that contains discrete value in the value domain
        # initialize the degree-of-membership values
        self.dom = np.zeros(self.domain.shape)  # a list that contains degree of membership values estimated from self.domain
        #
        self.name = name
        self._last_dom_value = 0

    def __getitem__(self, x_val: float):
        return self.dom[np.abs(self.domain - x_val).argmin()]

    def __setitem__(self, x_val: float, dom: float):
        self.dom[np.abs(self.domain - x_val).argmin()] = round(dom, self.precision)

    def __str__(self) -> str:
        """
        :return: string of pair degree-of-membership and corresponding domain value
        """
        return ' + '.join([str(a) + '/' + str(b) for a, b in zip(self.dom, self.domain)])

    def __get_last_dom_value(self) -> float:
        return self._last_dom_value

    def __set_last_dom_value(self, d: float) -> None:
        self._last_dom_value = d

    last_dom_value = property(__get_last_dom_value, __set_last_dom_value)

    @property
    def empty(self) -> bool:
        return np.all(self.dom == 0)

    @classmethod
    def create_trapezoidal(cls,
                           name: str,
                           domain_min: float,
                           domain_max: float,
                           res: int,
                           a: float,
                           b: float,
                           c: float,
                           d: float) -> Any:
        """
        TODO:
         Implement trapezoidal membership function, following the formula from `fuzzy_logic_and_fuzzy_set.ipynb`
        :param name: name of the trapezoidal function
        :param domain_min: the minimum value of the trapezoidal function
        :param domain_max: the maximum value of the trapezoidal function
        :param res: the number of steps between the minimum and maximum value
        :param a: the special input
        :param b: the special input
        :param c: the special input
        :param d: the special input
        :return: trapezoidal membership function
        """
        # initialize the result
        t1fs = cls(name, domain_min, domain_max, res)
        # retrieve the degree-of-membership of the inputs
        a = t1fs.adjust_domain_val(a)
        b = t1fs.adjust_domain_val(b)
        c = t1fs.adjust_domain_val(c)
        d = t1fs.adjust_domain_val(d)
        #
        t1fs.dom = None
        # Write your code below

        return t1fs

    @classmethod
    def create_triangular(cls,
                          name: str,
                          domain_min: float,
                          domain_max: float,
                          res: int,
                          a: float,
                          m: float,
                          b: float) -> Any:
        """
        TODO:
         Implement triangular membership function, following the formula from `fuzzy_logic_and_fuzzy_set.ipynb`
        :param name: name of the triangular function
        :param domain_min: the minimum value of the triangular function
        :param domain_max: the maximum value of the triangular function
        :param res: the number of steps between the minimum and maximum value
        :param a: the special input
        :param m: the special input
        :param b: the special input
        :return: the triangle membership function
        """
        # initialize the result
        t1fs = cls(name, domain_min, domain_max, res)
        # retrieve the degree-of-membership of the inputs
        a = t1fs.adjust_domain_val(a)
        m = t1fs.adjust_domain_val(m)
        b = t1fs.adjust_domain_val(b)
        #
        t1fs.dom = None
        # write your code below

        return t1fs

    def adjust_domain_val(self, x: float) -> NDArray:
        """
        Retrieve degree-of-membership value in the domain array from the input
        :param x: the input
        :return: degree-of-membership value
        """
        return self.domain[np.abs(self.domain - x).argmin()]

    def clear_set(self) -> None:
        """
        Clear the set (membership function)
        """
        self.dom.fill(0)

    def min_scalar(self, x: float) -> Any:
        """
        Minimum operator between the fuzzy set and the scalar
        :param x: the scalar
        :return: the scalar minimum of current fuzzy set and x
        """
        # initialize the result
        result = FuzzySet(f'({self.name}) min ({x})', self.domain_min, self.domain_max, self.res)
        result.dom = np.minimum(self.dom, x)
        return result

    def union(self, f_set: Any) -> Any:
        """
        TODO:
         Implement the Union operator of FuzzySet.
         It is calculated by maximizing values of this FuzzySet and FuzzySet `f_set`.
        :param f_set: the other fuzzy set to unite with
        :return: the union of current fuzzy set and f_set
        """
        # initialize result
        result = FuzzySet(name=f'({self.name}) union ({f_set.name})',
                          domain_min=self.domain_min,
                          domain_max=self.domain_max,
                          res=self.res)
        result.dom = None
        # Write your code below

        return result

    def intersection(self, f_set: Any) -> Any:
        """
        TODO:
         Implement the Intersection operator of FuzzySet.
         It is calculated by minimizing values of the this FuzzySet and FuzzySet `f_set`.
        :param f_set: the other fuzzy set to intersect with
        :return: the intersection of current fuzzy set and f_set
        """
        # initialize result
        result = FuzzySet(name=f'({self.name}) intersection ({f_set.name})',
                          domain_min=self.domain_min,
                          domain_max=self.domain_max,
                          res=self.res)
        result.dom = None
        # Write your code below

        return result

    def complement(self) -> Any:
        """
        TODO:
         Implement the Completion operator of FuzzySet.
         It is calculated by subtract the degree of membership value from 1.
        :return: the complement of current fuzzy set (self)
        """
        # initialize result
        result = FuzzySet(name=f'not ({self.name})',
                          domain_min=self.domain_min,
                          domain_max=self.domain_max,
                          res=self.res)
        result.dom = None
        # Write your code below

        return result

    def defuzzify_cog(self) -> Any:
        """
        TODO:
         Implement the defuzzification using center-of-area or center-of-gravity
        :return: crisp quantities
        """
        result = None
        # write your code below

        return result

    def get_domain_elements(self) -> NDArray:
        """
        :return: array of domain values
        """
        return self.domain

    def get_dom_elements(self) -> NDArray:
        """
        :return: array of degree-of-membership values
        """
        return self.dom

    def plot_set(self, ax: Any, col: str = '') -> None:
        """
        Visualize the fuzzy set
        """
        ax.plot(self.domain, self.dom, col)
        ax.set_ylim([-0.1, 1.1])
        ax.set_title(self.name)
        ax.grid(True, which='both', alpha=0.4)
        ax.set(xlabel='x', ylabel='$\mu(x)$')
