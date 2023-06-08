# DVSOD-Evaluation
This repository is used to evaluate the model performance on the DViSal dataset.

## Requirement 
* MATLAB 
* Python

## Getting Started

+ **Preparing DViSal dataset**

Download the `DViSal` dataset, which is structured as follows:

```
DViSal_dataset/
├─ data/
│  ├─ video1/
│  │  ├─ RGB/
│  │  │  ├─ 00000001.jpg
│  │  │  ├─ 00000002.png
│  │  ├─ Depth/
│  │  │  ├─ 00000001.png
│  │
│  ├─ video2/
│  │  ├─ RGB/
```

Then you need to convert its format for evaluation, via `GT_convert.py`.
1. Set `DViSal dataset path` and `Output path` in `GT_convert.py`
2. Obtain the restructured dataset for evaluation, with
```
python GT_convert.py
```


+ **Preparing saliency results**

x x x x

+ **Performing evaluation tool**

x x x x



## Acknowledgements
This evaluation toolbox is adapted from [the github repository](https://github.com/jiwei0921/Saliency-Evaluation-Toolbox). 

## References
```
@article{borji2015salient,
	title="Salient Object Detection: A Benchmark",
	author="Ali Borji and Ming-Ming Cheng and Huaizu Jiang and Jia Li",
	journal="IEEE Transactions on Image Processing",
	volume="24",
	number="12",
	pages="5706--5722",
	year="2015"
}
```
```
@inproceedings{fan2017structure,
	title="Structure-Measure: A New Way to Evaluate Foreground Maps",
	author="Deng-Ping Fan and Ming-Ming Cheng and Yun Liu and Tao Li and Ali Borji",
	booktitle="ICCV",
	pages="4558--4567",
	year="2017"
}
```
```
@inproceedings{fan2018enhanced,
	title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
	author="Deng-Ping Fan and Cheng Gong and Yang Cao and Bo Ren and Ming-Ming Cheng and Ali Borji",
	booktitle="IJCAI",
	pages="698--704",
	year="2018"
}
```
```
@misc{author_year,
  title="Evaluation Toolbox for Salient Object Detection",
  author="Wei Ji",
  howpublished="Saliency Evaluation Toolbox",
  url="https://github.com/jiwei0921/Saliency-Evaluation-Toolbox",
  year="2021“,
}
```
