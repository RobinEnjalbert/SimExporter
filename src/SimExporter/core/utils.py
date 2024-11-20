from numpy import stack
from k3d.helpers import get_bounding_box_point, get_bounding_box_points


def bounding_box(o):

    if hasattr(o, 'vertices'):
        return get_bounding_box_points(o.vertices['0'], o.model_matrix)
    elif hasattr(o, 'positions'):
        return get_bounding_box_points(o.positions['0'], o.model_matrix)
    elif hasattr(o, 'position'):
        return get_bounding_box_point(o.position['0'])
    elif hasattr(o, 'origins') and hasattr(o, 'vectors'):
        return get_bounding_box_points(stack([o.origins['0'], o.vectors['0']]), o.model_matrix)
