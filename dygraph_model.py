# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle
import paddle.nn as nn
import net
import math


class DygraphModel():
    # define model
    def create_model(self, config):
        layer_sizes = config.get("hyper_parameters.layer_sizes")
        dp_drop_prob = config.get("hyper_parameters.dp_drop_prob")

        deeprecommender_model = net.DeepRecommenderLayer(
            layer_sizes, dp_drop_prob)

        return deeprecommender_model

    # define feeds which convert numpy of batch data to paddle.tensor
    def create_feeds(self, batch_data, config):
        return paddle.to_tensor(batch_data)

    # define loss function by predicts and label
    def create_loss(self, inputs, targets):
        mask = paddle.where(targets != 0, paddle.ones(targets.shape),
                            paddle.zeros(targets.shape))
        num_ratings = paddle.sum(mask)
        criterion = nn.MSELoss()
        loss = criterion(inputs * mask, targets) / num_ratings
        return loss

    # define optimizer
    def create_optimizer(self, dy_model, config):
        lr = config.get("hyper_parameters.optimizer.learning_rate", 0.001)
        momentum = config.get("hyper_parameters.optimizer.momentum", 0.9)
        weight_decay = config.get("hyper_parameters.optimizer.weight_decay",
                                  0.0)
        scheduler = paddle.optimizer.lr.MultiStepDecay(
            learning_rate=lr, milestones=[24, 36, 48, 66, 72], gamma=0.5)
        optimizer = paddle.optimizer.Momentum(parameters=dy_model.parameters(),
                                              learning_rate=scheduler,
                                              momentum=momentum,
                                              weight_decay=weight_decay)
        return optimizer

    def create_metrics(self):
        metrics_list_name = []
        metrics_list = []
        return metrics_list, metrics_list_name

    # construct train forward phase
    def train_forward(self, dy_model, metrics_list, batch_data, config):
        sparse_tensor = self.create_feeds(batch_data, config)
        outputs = dy_model.forward(sparse_tensor)
        loss = self.create_loss(outputs, sparse_tensor)
        # update metrics

        # print_dict format :{'loss': loss}
        print_dict = {'loss': loss}
        return loss, metrics_list, print_dict

    def infer_forward(self, dy_model, metrics_list, batch_data, config):
        inputs = self.create_feeds(batch_data, config)
        prediction = dy_model.forward(inputs)
        # update metrics

        # print_dict format :{'loss': loss}
        print_dict = {}
        return metrics_list, print_dict