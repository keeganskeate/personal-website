# Tailored Metropolis-Hastings Algorithm

Business are often confronted with situations where one of two possibilities may occur, and may find it strategic to estimate the probability of each outcome. The Metropolis-Hastings algorithm, an advanced Markov chain Monte Carlo method that simulates draws from a Bayesian posterior distribution, is a powerful tool that can be applied for this purpose. Given observed data and a proposed model, the method generates a probability distribution for the model parameters. An example is provided that fits a logit model, which can be used to model binary choices. Business may find this model useful for its power in predicting the likelihood of each of two alternatives occuring.

								<p>The Metropolis-Hastings algorithm simulates draws from a posterior distribution $$\pi(\beta\vert\boldsymbol{y},\boldsymbol{x}).$$ The algorithm iterates the following steps.</p>
								<p>First, draw $$\beta^*\sim q(\beta \vert y).$$
								Second, accept the draw with probability $$\alpha=\text{min}\big\{1,\frac{f(y\vert\beta^*)\pi(\beta^*)q(\beta\vert y)}{f(y\vert\beta)\pi(\beta)q(\beta^*\vert y)}\big\}.$$
								Third, if the draw is accepted, then set $\beta=\beta^*$ and repeat. Otherwise, keep $\beta$. The Tailored Metropolis-Hastings algorithm uses a multivariate $t$-distribution proposal density
								$$q(\beta \vert y) \sim T_{\nu}(\hat{\beta}_{MLE},\hat{\Sigma}_{MLE}).$$
								Below is the algorithm written in Python 2.7. Attached is an example that fits a logit model to sample data, and returns the realized posterior distribution from $i$ iterations.</p>
							</div>
						<div id="snipcode">
<pre class="prettyprint">
import numpy as np
from math import *

def MV_t_pdf(x, mu, Sigma, df):
    """
    Inputs:
        x - kx1 Random variables.
        mu - kx1 Mean values.
        Sigma - kxk Scale matrix.
        df - Degrees of freedom.
    Returns:
    	The density of the given element.
    """
    p = len(x)
    numerator = gamma(1. * (p + df) / 2)
    denomenator = (gamma(1. * df / 2) * 
    		  pow(df * pi, 1. * p / 2) *
                  pow(
                  np.linalg.det(Sigma),
                  1. / 2) *
                  pow(1 + (1. / df) *
                  np.dot(np.dot(
                  (x - mu), 
                  np.linalg.inv(Sigma)),
                  (x - mu)), 
                  1. * (p + df) / 2))
    density = 1. * numerator / denomenator
    return density
    
def MV_t_random_var(mu, Sigma, df):
    """
    Inputs:
        mu - kx1 Means of the random variables.
        Sigma - kxk Scale matrix.
        df - Degrees of freedom.
    Returns:
    	Independent draws from
    	a MV-t distribution.
    """
    mu = np.asarray(mu)
    p = len(mu)
    u = np.random.chisquare(df)
    y = np.random.multivariate_normal(
        np.zeros(p), Sigma)
    return mu + y * np.sqrt(df / u)
    
def Tailored_MH(
    f, prior, beta0, Sigma0,
    y, X, iters, df):
    """
    Inputs:
        f - a likelihood function.
        prior - Your Bayesian prior.
        beta0 - kx1 initial values
        Sigma0 - kxk initial values
        y - nx1 dependent variable.
        X - nxk independent variables.
        iters - iterations.
        df - degrees of freedom.
    Returns:
        The acceptance rate and i
        draws of beta from the posterior.
    """
    beta = np.zeros((iters, len(beta0)))
    beta[0] = beta0
    acceptance = np.zeros(iters)
    for i in range(iters):
        beta_star = MV_t_random_var(
                    beta0, Sigma0, df)
        Numerator = f(beta_star, y, X) *\
        	    prior(beta_star,
        	    beta0, Sigma0) *\
                    MV_t_pdf(beta[i - 1],
                    beta0, Sigma0, df)
        Denomenator = f(beta[i - 1], y , X) *\
        	      prior(beta[i - 1], 
        	      beta0, Sigma0) *\
                      MV_t_pdf(beta_star, 
                      beta0, Sigma0, df)
        alpha = min(
                1., 1. * Numerator / Denomenator)
        acceptance[i] = np.random.binomial(
                        1, alpha)
        if acceptance[i] == 1:
            beta[i] = beta_star
        else:
            beta[i] = beta[i - 1]
    acceptance_rate = np.mean(acceptance)
    return beta, acceptance_rate
</pre>
