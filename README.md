# Resources:

+ README.md: this file.
+ result.csv:  The performance for different classifers and features. Measured in F1, Precision, Recall, Specificity, Accuracy, and AUC.

###  Source codes:
+ utils.py: provides functions of (1) extracting 'closeness centrality' for graphs: **get_closeness_centrality**, (2) evaluating classification performance: **evaluate**, and (3) converting graphs of continuous weights to ajacency graphs: **to_adjacency_G**
+ PAN.ipynb: creates PAN graphs and returns their graph properties
+ LIONESS.ipynb: gets graph properties for LIONESS graphs returned by pypanda (https://github.com/davidvi/pypanda)
+ PPI.ipynb: creates PPI graphs and returns their graph properties
+ classification.ipynb: provides two classifers, SVM and LogisticRegression, with gene expression and graph propeties as features.
+ PAN.html, LIONESS.html, PPI.html, and classification.html: html files for PAN.ipynb, LIONESS.ipynb, PPI.ipynb, and classification.ipynb, respectively.

### Folder input_data/:
+ UK207.csv: UK207 dataset. Other two datasets will be provided upon request.
+ hgncToKEGG.csv, hgncToDO.csv, hgncToHPO.csv: 3 ontologies.
+ COMBINED.DEFAULT_NETWORKS.BP_COMBINING.txt: gene interaction, from GeneMania (http://genemania.org/data/current/Rattus_norvegicus.COMBINED/)
+ ENST-ENSG-HGNC-GO-kegg-map.csv: map ensembl_gene_id in COMBINED.DEFAULT_NETWORKS.BP_COMBINING.txt to hgnc_symbol in gene expression datasets.

# Step-by-step running:

## 0. Installing Python libaries needed
+ Install pypanda, https://github.com/davidvi/pypanda. This creates LIONESS graphs.
+ Install sklearn: pip install scikit-learn
+ Install networkx: pip install networkx

## 1. PAN:
Running
```sh
PAN.ipynb
```
This returns 
+ Top genes selected by VarianceThreshold, saved in output_data/top_genes.txt
+ Gene expression for the top genes and its label, saved in output_data/gene_condition.csv.
+ Label, saved in output_data/y.txt 
+ Non-graph data, or gene expression, save in output_data/non_graph.csv
+ Gene expression, as the transpose of output_data/non_graph.csv, saved in output_data/gene_expression.txt. This is the input to LIONESS.
+ 10fold_idx/: ten-fold splits to be used for all models
+ PAN_KEGG graph (saved in output_data/pan_KEGG_graph.csv) and the feature for this graph (output_data/pan_KEGG_graph_feature.csv) for the dataset.
+ PAN_HPO graph (saved in output_data/pan_HPO_graph.csv) and the feature for this graph (output_data/pan_HPO_graph_feature.csv) for the dataset.
+ PAN_DO graph (saved in output_data/pan_DO_graph.csv) and the feature for this graph (output_data/pan_DO_graph_feature.csv) for the dataset.

## 2. LIONESS:
+ (Please install pypanda, https://github.com/davidvi/pypanda)
+ Running 
```sh
./pypanda  -e output_data/gene_expression.txt -o output_data/gene_expression_panda.txt -q output_data/lioness.txt
```

The output output_data/lioness.txt is the input to LIONESS.ipynb. Running 
```sh
LIONESS.ipynb
```
This returns the feature for LIONESS graph, saved in output_data/lioness_graph_feature.csv

## 3. PPI: 
running 
```sh
PPI.ipynb
```
This returns the feature for PPI graph, saved in output_data/ppi_graph_feature.csv

## 4. Classification:
Now all the graphs and their features are already extracted. They are the input to classification.ipynb. Running 
```sh
classification.ipynb
```
This returns the performance for all the features in two classifers, saved in result.csv.
A visualization on the average of ten-fold running is saved at figs/SVM.png and figs/LR.png, for the two classfiers.
