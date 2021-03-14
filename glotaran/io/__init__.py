"""Functions for data IO

Note:
-----
Since Io functionality is purely plugin based this package mostly
reexports functions from the pluginsystem from a common place.
"""

from glotaran.plugin_system.data_io_registration import get_dataloader
from glotaran.plugin_system.data_io_registration import get_datawriter
from glotaran.plugin_system.data_io_registration import load_dataset
from glotaran.plugin_system.data_io_registration import register_data_io
from glotaran.plugin_system.data_io_registration import write_dataset
from glotaran.plugin_system.project_io_registration import load_model
from glotaran.plugin_system.project_io_registration import load_parameters
from glotaran.plugin_system.project_io_registration import load_result
from glotaran.plugin_system.project_io_registration import load_scheme
from glotaran.plugin_system.project_io_registration import register_project_io
from glotaran.plugin_system.project_io_registration import write_model
from glotaran.plugin_system.project_io_registration import write_parameters
from glotaran.plugin_system.project_io_registration import write_result
from glotaran.plugin_system.project_io_registration import write_scheme

from .interface import DataIoInterface
from .interface import ProjectIoInterface
from .prepare_dataset import prepare_time_trace_dataset
