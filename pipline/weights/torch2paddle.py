import numpy as np
from torch import load
import paddle


def transfer():
    input_fp = "model_save/model.last"
    output_fp = "model_save/DeepRecommendr_paddle.pdparams"
    torch_dict = load(input_fp)
    paddle_dict = {}
    fc_names = torch_dict.keys
    for key in torch_dict:
        weight = torch_dict[key].cpu().detach().numpy()
        flag = [i in key for i in fc_names]
        if any(flag):
            print("weight {} need to be trans".format(key))
            weight = weight.transpose()
        paddle_dict[key] = weight
    paddle.save(paddle_dict, output_fp)


if __name__ == '__main__':
    transfer()