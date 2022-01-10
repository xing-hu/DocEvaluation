# DocEvaluation
This repository is the replication package for the paper titled:  Correlating Automated and Human Evaluation of Code Documentation Generation Quality


## RQ1 
Please run the command 

```python3 evaluate.py```

Note: Code2Seq utilized the AST paths to generate code comments. During the experiment, we find that it fails in some cases. Therefore, the number of the generated cases is less than 5000.

## RQ2

The Correlation can be computed by the scrip ```plot_corr.R```. 
The output is the Figure 7 for RQ2 and RQ3.


## RQ3

Please refer ```pearson_bins.py``` to get Table 6.
