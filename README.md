# DeepRecommender

 以下是本例的简要目录结构及说明： 

```
├── data # 文档
		├── train #训练数据
			├── train_data.txt
		├── test  #测试数据
			├── test_data.txt
├── __init__.py 
├── README.md #文档
├── config.yaml # sample数据配置
├── config_bigdata.yaml # 全量数据配置
├── DeepRecommender_Reader.py # 数据读取程序
├── net.py # 模型核心组网（动静统一）
├── dygraph_model.py # 构建动态图
```

注：在阅读该示例前，建议您先了解以下内容：

[paddlerec入门教程](https://github.com/PaddlePaddle/PaddleRec/blob/master/README.md)

## 内容

- [模型简介](#模型简介)
- [数据准备](#数据准备)
- [运行环境](#运行环境)
- [快速开始](#快速开始)
- [模型组网](#模型组网)
- [效果复现](#效果复现)
- [进阶使用](#进阶使用)
- [FAQ](#FAQ)

## 模型简介


## 数据准备
我们在作者处理过的开源数据集Netflix上验证模型效果,在模型目录的data目录下为您准备了快速运行的示例数据，若需要使用全量数据可以参考下方[效果复现](#效果复现)部分.
数据的格式如下：
生成的格式以\t为分割点

```
116	341	3.7
```

## 运行环境
PaddlePaddle 2.2

python 3.8

os : windows

## 快速开始
本文提供了样例数据可以供您快速体验，在任意目录下均可执行。在deeprecommender模型目录的快速执行命令如下： 
```bash
# 进入模型目录
# cd models/?/deeprecommender # 在任意目录均可运行
# 动态图训练
python -u ../../../tools/trainer.py -m config.yaml # 全量数据运行config_bigdata.yaml 
# 动态图预测
python -u ../../../tools/infer.py -m config.yaml 

# 静态图训练
python -u ../../../tools/static_trainer.py -m config.yaml # 全量数据运行config_bigdata.yaml 
# 静态图预测
python -u ../../../tools/static_infer.py -m config.yaml 
```

## 模型组网
DeepRecommender 。模型的主要组网结构如下：
[DeepRecommender]()


### 效果复现
为了方便使用者能够快速的跑通每一个模型，我们在每个模型下都提供了样例数据。如果需要复现readme中的效果,请按如下步骤依次操作即可。 
在全量数据下模型的指标如下：

| 模型 | rmse   | layer_sizes             | batch_size | epoch_num | Time of each epoch |
| :------| :------ | :------ | :------| :------ | -------|
| DeepRecommender | 0.9103 | [17768, 512, 512, 1024] | 128        | 45        | 约1分半 |

在其他数据下模型的指标如下：
| 数据集 | rmse   | layer_sizes            | batch_size | epoch_num | Time of each epoch |
| :----- | :----- | :--------------------- | :--------- | :-------- | ------------------ |
| N3M    |        | [17736, 128, 256, 256] | 128        |           | 约40秒             |
| N6M    | 0.9206 | [17757, 256, 256, 512] | 128        | 60        | 约1分半            |
| N1Y    | 0.9220 | [16907, 256, 256, 512] | 128        | 42        | 约55秒             |

1. 确认您当前所在目录为PaddleRec/models/?/deeprecommender
2. 进入paddlerec/datasets/Netflix目录下，执行该脚本，会从国内源的服务器上下载我们预处理完成的Netflix全量数据集，并解压到指定文件夹。

``` bash
cd ../../../datasets/Netflix
sh run.sh
```
3. 切回模型目录,执行命令运行全量数据
```bash
cd - # 切回模型目录
# 动态图训练
python -u ../../../tools/trainer.py -m config_bigdata.yaml # 全量数据运行config_bigdata.yaml 
python -u ../../../tools/infer.py -m config_bigdata.yaml # 全量数据运行config_bigdata.yaml 
```

## 进阶使用

## FAQ
