# Conditional Logit Model 

Businesses may find it useful to model and predict how customers will choose among available products. A conditional logit model can be used for modeling choices between many alternatives. This flexible model allows for attributes to vary over individuals and alternatives. This model can be used to predict customers' willingness to pay for each available choice.

<div id="snipdescrip">
							<p>Estimation of a conditional logit begins with the likelihood function 
							$$\mathscr{L}(\beta)=\prod_{n=1}^N\prod_{j=1}^J(P_{nj})^{y_{nj}},$$
							that has log-likelihood
							$$\text{ln}\mathscr{L}(\beta)=\sum_{n=1}^N\sum_{j=1}^Jy_{nj}\text{ln}(P_{nj}),$$
							where
							$$y_{ni} =\begin{cases}1, & \text{if } n \text{ choses }j \\ 0, & \text{otherwise,}\end{cases}$$
							and the probability $n$ chose $j$ is
							$$P_{nj} = \tfrac{exp(x_{nj}'\beta)}{\sum_{j=1}^Jexp(x_{ni}'\beta)}.$$
							Exclusively for the conditional logit, the first order condition is
							$$\frac{\partial\text{ln}\mathscr{L}(\beta)}{\partial\beta} = \sum_{n=1}^N\sum_{j=1}^J(y_{nj}-P_{nj})x_{nj} = 0,$$
							and the hessian, which is negative semi-definite, is given by
							$$\frac{\partial^2\text{ln}\mathscr{L}(\beta)}{\partial\beta\partial\beta'} = -\sum_{n=1}^N\sum_{j=1}^JP_{nj}(d_{nj}-\bar{x}_n)(d_{nj}-\bar{x}_n)',$$
							where
							$$\bar{x}_n = \sum_{j=1}^JP_{nj}x_{nj}$$
							$$d_{nj}= \begin{cases}1, & \text{if } i \text{ chose }j \\ 0, & \text{otherwise} .\end{cases}$$
							The asymptotic variance of the conditional logit model is
							$$I^{-1}= \bigg(-E\bigg[\frac{\partial^2l(\beta)}{\partial \beta \partial \beta'}\bigg]\bigg)^{-1}.$$
							The conditional logit model is estimated with maximum likelihood using the Newton-Rhapson algorithm. Below is the algorithm written in Python 2.7. Attached is an example that uses data from a stated preference experiment to gauge demand for a new mag-lev rail system in Switzerland called Swiss Metro. The example fits a conditional logit model of the choice between car, rail, and Swiss Metro, controlling for travel time, travel cost, alternative specific constants, and if the respondent has purchased an annual pass for Swiss trains. In general, the program can be run with $N$ individuals and $J$ choices. The results are identical to those produced in Stata 14.1 and MATLAB 9.0.</p>
						</div>
							
						<div id="snipcode">
<pre class="prettyprint">
import numpy as np
import pylab as py
    
def Cond_Logit(Y, X, N, J):
    """
    Estimates a conditional logit
    given Y, X, # of N, and # of J.
    """
    initial_beta = np.dot(np.linalg.inv(
    		   np.dot(X.T, X)),
    		   np.dot(X.T, Y))
    beta_MLE = newton_method(
    	       cond_score, cond_hessian,
    	       initial_beta, Y, X, N, J)
    cov = - np.linalg.inv(
    	    cond_hessian(
    	    beta_MLE, Y, X, N, J))
    se = np.diag(np.sqrt(cov))    
    return beta_MLE, se, cov

def cond_Pr(x,beta):
    """
    Conditional Logit Choice Probability
    """
    J = len(x)
    probabilities = []
    for i in range(J):
        Num = np.exp(np.dot(x[i], beta))
        Denom = 0.0
        for j in range(J):
            Denom += np.exp(np.dot(x[j], beta))
        probabilities.append(1.0 * Num / Denom)
    return probabilities
    
def cond_score(beta, Y, X, N, J):
    """Conditional Logit Score Function"""
    score = 0.0
    for n in range(N):
        X_n = X[(n) * J : J + J * n]
        y_n = Y[(n) * J : J + J * n]
        for j in range (J):
            score += (y_n[j] - 
            	      cond_Pr(X_n, beta)[j]) *\
                      X_n[[j],:].T
    return score

def cond_hessian(beta, Y, X, N, J):
    """
    Conditional Logit Hessian Function
    """
    hessian = 0.0
    for n in range(N):
        X_n = X[(n) * J : J + J * n]
        x_bar_n = 0.0
        for j in range(J):
            x_bar_n += X_n[[j],:] * 
            	       cond_Pr(X_n, beta)[j]
        for j in range(J):
            hessian -= np.dot((
            	       X_n[[j],:].T - x_bar_n.T),
                       (X_n[[j],:] - x_bar_n)) *
                       cond_Pr(X_n, beta)[j]
    return hessian
    
def newton_method(gradient, hessian, beta0,
    		  Y, X, N, J, tol, maxIter):
    """
    The Newton-Raphson Algorithm
    """
    beta_old = beta0
    for i in range(maxIter):
        beta_new = beta_old - 
        	   np.dot(
        	   np.linalg.inv(
        	   hessian(beta_old, Y, X, N, J)),
        	   gradient(beta_old, Y, X, N, J))
        if (py.norm(beta_new - beta_old) < tol):
            break
        beta_old = beta_new
    return beta_new
</pre>