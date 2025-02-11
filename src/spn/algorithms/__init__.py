from spn.algorithms.MPE import add_node_mpe, mpe_leaf
from spn.structure.leaves.histogram.Expectation import add_histogram_expectation_support
from spn.structure.leaves.histogram.Inference import add_histogram_inference_support
from spn.structure.leaves.parametric.Expectation import add_parametric_expectation_support
from spn.structure.leaves.parametric.Inference import add_parametric_inference_support
from spn.structure.leaves.parametric.MPE import add_parametric_mpe_support
from spn.structure.leaves.parametric.Sampling import add_parametric_sampling_support
from spn.structure.leaves.piecewise.Expectation import add_piecewise_expectation_support
from spn.structure.leaves.piecewise.Inference import add_piecewise_inference_support

add_parametric_sampling_support()
add_parametric_inference_support()
add_parametric_expectation_support()
add_parametric_mpe_support()

add_piecewise_inference_support()
add_piecewise_expectation_support()

add_histogram_inference_support()
add_histogram_expectation_support()
