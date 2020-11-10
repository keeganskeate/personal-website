# Gibbs Sampling Algorithm

People often face hierarchical choices, such as products of varying quality, but are contrained by their resources. Given observed choices between three ranked alternatives, you can use Gibbs sampling with data augmentation to fit an ordered probit model. This Bayesian procedure generates a probability distribution for the model parameters. Businesses may find this model useful for predicting the likelihood of customers choosing low, medium, or premium grade products.

				<a name="gibbs-probit"></a>
					<div class="snip">
						<h5>
						<div class="blogicon"><a href="code/gibbs-probit.zip" download title="Download example"><span aria-hidden="true" data-icon="&#xe9c4;"></span></a></div>
						<div id="sniptitle">Using Gibbs Sampling with Data Augmentation to Fit an Ordered Probit Model</div>
						</h5>
						<div id="snipdescrip">
							<p>Given observed choices between three ranked alternatives, you can use Gibbs sampling with data augmentation to fit an ordered probit model where $y_i \in \{1,2,3\}$. The latent variable
							$$y_i^* = x_i'\beta + \epsilon_i,$$
							where $\epsilon_i \sim \mathcal{N}(0,\sigma^2),$ but you observe
							$$y_i = \begin{cases} 1, & \text{if} \hspace{1ex}\gamma_0 < y_i^*\leq\gamma_1 \\ 2, & \text{if}\hspace{1ex}\gamma_1 < y_i^*\leq\gamma_2 \\ 3, & \text{if}\hspace{1ex}\gamma_2 < y_i^*\leq\gamma_3.\end{cases}$$
							You can impose scale and location restrictions on the model parameters such that $\gamma_1=0$ and $\gamma_2=1$. It is standard to let $\gamma_0=-\infty$ and $\gamma_J = \infty$. This allows for estimation of the posterior using the following Gibbs recursion.</p>
							<p>First, draw $$\boldsymbol{y}^*\vert \beta,\sigma^2,\boldsymbol{y} \sim TN_{\gamma_{i-1},\gamma_i}(x_i'\beta,\sigma^2).$$
							Second, draw $$\sigma^2\vert \boldsymbol{y}^*,\beta,\boldsymbol{y} \sim IG\big(\frac{\nu_0+N}{2},\frac{\delta_0 + (\boldsymbol{y}^* - \boldsymbol{x}\beta)'(\boldsymbol{y}^* - \boldsymbol{x}\beta)}{2}\big).$$
							Third, draw $$\beta\vert \boldsymbol{y}^*, \sigma^2, \boldsymbol{y} \sim N(\hat{\beta},\hat{B}),$$
							where$$\hat{B}= (B_0^{-1}+\frac{\boldsymbol{x}'\boldsymbol{x}}{\sigma^2})^{-1},$$ $$\hat{\beta}= \hat{B}(B_0^{-1}\beta_0+\frac{\boldsymbol{x}'\boldsymbol{y}^*}{\sigma^2}).$$
							This method simulates draws from the posterior distribution $\pi(\beta\vert\boldsymbol{y},\boldsymbol{x})$. An example that fits an ordered probit model to sample data using Gibbs sampling is attached. The example reports the means and standard deviations of 10,000 draws of model parameters, as well as plots the drawn estimates.</p>
						</div>
						<div id="snipcode">
<pre class="prettyprint">
import numpy as np
import scipy.stats as ss

def gibbs(beta0, B0, v0, d0, y, X, iters):
    """
    Inputs:
        Priors - beta0, B0, v0, d0.
        Data - y and X.
        Desired iterations - iters.
    Returns:
    	A posterior distribution.
    """
    beta = np.zeros((iters, len(beta0)))
    sigma_sq = np.ones(iters)
    B0_inv = np.linalg.inv(B0)  
    for i in range(iters):
        y_star = y
        XB = np.dot(X, beta[i - 1])
        s = sigma_sq[i - 1]
        for n in range(len(y)):
            if y[n] == 1:
                y_star[n] = ss.truncnorm.rvs(
                	    - np.infty, 0.0,
                	    loc = XB[n],
                	    scale = s)
            if y[n] == 2:
                y_star[n] = ss.truncnorm.rvs(
                	    0.0, 1.0,
                	    loc = XB[n],
                	    scale = s)
            if y[n] == 3:
                y_star[n] = ss.truncnorm.rvs(
                	    1., np.infty,
                	    loc = XB[n],
                	    scale = s)
        v0_hat = v0 + (len(y) / 2)
        d0_hat = 1. / ((1 / d0) + 
        	.5 * (np.dot(
        	(y_star-XB).T,
        	y_star-XB)))
        sigma_sq[i] = ss.invgamma.rvs(
        	      v0_hat, d0_hat) 
        B_hat = np.linalg.inv(
        	np.dot(X.T, X) /
        	sigma_sq[i] + B0_inv)
        beta_hat = np.dot(
        	   B_hat, 
        	   (np.dot(B0_inv, beta0).T +
                   (np.dot(X.T, y_star) / 
                   sigma_sq[i])).T)
        beta[i] = np.random.multivariate_normal(
        	  np.hstack(beta_hat), B_hat)      
    return beta, sigma_sq
						</pre>