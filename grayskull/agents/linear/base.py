# -*- coding: utf-8 -*-
import logging

import gym.spaces.discrete
import numpy as np

import grayskull.agents.base

log = logging.getLogger(name=__name__)


class LinearAgent(grayskull.agents.base.Agent):
    def __init__(self,
                 action_space,
                 observation_space,
                 learning_rate=0.1,
                 *args,
                 **kwargs):
        super(LinearAgent, self).__init__(action_space, *args, **kwargs)

        # get the input size
        self.n_params = np.prod(observation_space.shape)

        # set up the model
        self.model = np.zeros(self.n_params, dtype=np.float)

    def act(self, observation):
        """
        Return an action based on the last observed state

        Parameters
        ----------
        observation : a game state (usually an image)

        Returns
        -------
        an action from self.actions
        """
        return self.actions[
            0 if np.dot(self.model, observation.ravel()) < 0 else 1
        ]
