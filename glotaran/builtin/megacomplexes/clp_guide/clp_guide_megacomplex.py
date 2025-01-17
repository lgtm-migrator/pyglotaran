from __future__ import annotations

import numpy as np
import xarray as xr

from glotaran.model import DatasetModel
from glotaran.model import Megacomplex
from glotaran.model import megacomplex


@megacomplex(exclusive=True)
class ClpGuideMegacomplex(Megacomplex):
    type: str = "clp-guide"
    target: str

    def calculate_matrix(
        self,
        dataset_model: DatasetModel,
        global_axis: np.typing.ArrayLike,
        model_axis: np.typing.ArrayLike,
        **kwargs,
    ):
        clp_label = [self.target]
        matrix = np.ones((1, 1), dtype=np.float64)
        return clp_label, matrix

    def finalize_data(
        self,
        dataset_model: DatasetModel,
        dataset: xr.Dataset,
        is_full_model: bool = False,
        as_global: bool = False,
    ):
        pass
