import numpy as np
import re

from typing import Dict

from .estimator import Estimator


class Verbalized1S(Estimator):
    def __init__(self, confidence_regex="", name_postfix=""):
        self.confidence_regex = confidence_regex
        self.postfix = name_postfix
        super().__init__(["greedy_texts"], "sequence")

    def __str__(self):
        return f"Verbalized1S{self.postfix}"

    def __call__(self, stats: Dict[str, np.ndarray]) -> np.ndarray:
        ues = []
        conf_re = re.compile(self.confidence_regex)
        for answer in stats["greedy_texts"]:
            match = re.search(conf_re, answer)

            try:
                ue = 1 - float(match.groups()[0])
            except AttributeError:
                ue = np.nan

            ues.append(ue)

        return np.array(ues)
