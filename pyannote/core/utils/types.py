from typing import Hashable, Union, Tuple, Iterator, TYPE_CHECKING

from typing_extensions import Literal

if TYPE_CHECKING:
    from ..segment import Segment
    from ..timeline import Timeline
    from ..feature import SlidingWindowFeature
    from ..annotation import Annotation

Label = Hashable
Support = Union['Segment', 'Timeline']
LabelGeneratorMode = Literal['int', 'string']
LabelGenerator = Union[LabelGeneratorMode, Iterator[Label]]
TrackName = Union[str, int]
Key = Union['Segment', Tuple['Segment', TrackName]]
Resource = Union['Segment', 'Timeline', 'SlidingWindowFeature',
                 'Annotation']
CropMode = Literal['intersection', 'loose', 'strict']
Alignment = Literal['center', 'loose', 'strict']
LabelStyle = Tuple[str, int, Tuple[float, float, float]]
