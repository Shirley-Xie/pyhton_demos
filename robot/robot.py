import numpy as np


class MultinomialDistribution(object):

    def __init__(self, p, rso=np.random):
        """Initialize the multinomial random variable.

        Parameters
        ----------
        p: numpy array of length `k`
            The event probabilities
        rso: numpy RandomState object (default: None)
            The random number generator

        """

        # Check that the probabilities sum to 1. If they don't, then
        # something is wrong! We use `np.isclose` rather than checking
        # for exact equality because in many cases, we won't have
        # exact equality due to floating-point error.
        if not np.isclose(np.sum(p), 1.0):
            raise ValueError("event probabilities do not sum to 1")

        # Store the parameters that were passed in
        self.p = p
        self.rso = rso

        # Precompute log probabilities, for use by the log-PMF, for
        # each element of `self.p` (the function `np.log` operates
        # elementwise over NumPy arrays, as well as on scalars.)
        self.logp = np.log(self.p)

    def sample(self, n):
        """Samples draws of `n` events from a multinomial distribution with
        outcome probabilities `self.p`.

        Parameters
        ----------
        n: integer
            The number of total events

        Returns
        -------
        numpy array of length `k`
            The sampled number of occurrences for each outcome

        """
        x = self.rso.multinomial(n, self.p)
        return x
print(np.random.multinomial(2, [0.3, 0.5, 0.2]))
# MultinomialDistribution()
# 可以查找随机数
rso = np.random.RandomState(230489)
rso.rand()  # 0.5356709186237074
rso.rand()  # 0.6190581888276206
rso.seed(230489)
rso.rand()  # 0.5356709186237074
rso.rand()  # 0.6190581888276206

