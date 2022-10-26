# Phylogenetically Informed Pollen Pipeline
Code for a variety of pollen recognition tasks, including classification, novelty detection, and phylogenetic placement. 

# Abstract
Phylogenetic interpretation of pollen morphology is hindered by our inability to recognize the evolutionary history embedded in pollen features. Deep learning offers potential tools for connecting morphology to phylogeny. Using deep neural networks, we developed an explicitly phylogenetic toolkit for analyzing the overall shape, internal structure, and texture of a pollen grain. Our analysis pipeline both classifies pollen specimens and determines the optimal threshold of classification uncertainty for identifying a specimen as novel. Features of novel specimens are passed to a multi-layer perceptron network trained to transform these features into predicted phylogenetic distances from known taxa. We used these predicted distances to place the specimen in a phylogeny. We trained and evaluated our models using optical superresolution micrographs of 34 species of the \textit{Bombacoideae} subfamily (Malvaceae) and 30 \textit{Podocarpus} species. With these models, we placed 23 fossil specimens in their respective phylogenies. Our results demonstrate that the phylogenetic history encoded in pollen morphology can be recognized by neural networks and that deep-learned features can be used in phylogenetic placement. Our approach makes cryptic extinction and speciation events - events that are masked by the limited taxonomic resolution of the fossil pollen record - visible with pollen data and allows molecular phylogenies to be calibrated using this extensive microfossil record.

# Significance Statement 
Pollen features have limited homology across clades, which makes interpretating morphology in a phylogenetic framework challenging and circumscribes evolutionary and paleoecological interpretations of this global, abundant, and temporally expansive terrestrial fossil record. Our analysis uses learned features from deep neural networks to quantify morphological differences among pollen taxa, discover novel morphotypes, and place fossil specimens on a phylogeny. Our approach fundamentally changes how fossil pollen morphology can be interpreted, allowing greater evolutionary inference from fossil pollen specimens. Our analysis framework, however, is not specific to pollen and can be generalized to other taxa and other forms of phenotypic data.

# Main Structure 
There are five folders in this repository.
1. Classification pipeline (training and validation)
2. Novelty detection (based on the model's uncertainty when encountering a new pollen specimen) 
3. Phylogenetic placement (training and evaluation) using pseudo-novel taxa 
4. Fossil analaysis 
5. Optimal threshold selection for novelty detection 
