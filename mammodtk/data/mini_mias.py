"""

"""
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class MiniMIASMetadata:
    """
    Class to represent the metadata for a sample in the Mini-MIAS dataset.
    
    The metadata for each sampple is in the format: REFNUM BG CLASS SEVERITY X Y RADIUS
    
    - REFNUM: The reference number of the sample, which contains information about which breast it is from and the
    resolution of the image.
    - BG: the characteristic of the background tissue:
        - 'F' - fatty.
        - 'G' - fatty-glandular.
        - 'D' - dense-glandular.
    - CLASS: the class of abnormality present:
        - 'CALC' - Calcification.
        - 'CIRC' - Well-defined/circumscribed masses.
        - 'SPIC' - Spiculated masses.
        - 'MISC' - Other, ill-defined masses.
        - 'ARCH' - Architectural distortion.
        - 'ASYM' - Asymmetry.
        - 'NORM' - Normal.
    - SEVERITY: severity of abnormality:
        - 'B' - Benign.
        - 'M' - Malignant.
    - X: the x-axis image coordinate of the centre of abnormality.
    - Y: the y-axis image coordinate of the centre of abnormality.
    - RADIUS: approximate radius in pixels of a circle enclosing the abnomrality.
    
    If a sample has a CLASS equal to NORM, the following columns are empty. Rather than deal with those columns possibly
    being `None`, they are instead initialised to the following:
    
    - SEVERITY = "X"
    - "X", "Y", "RADIUS" = -1
    """
    refnum: str
    bg: str
    class_label: str
    severity: str = "X"
    x: int = -1
    y: int = -1
    radius: int = -1

    def __post_init__(self):
        self.breast = self._set_breast()
        self.resolution = self._set_resolution()

    def _set_breast(self) -> str:
        """
        Determine which breast the sample is of based on the refnum.
        
        Returns
        -------
        str
            "left" if the sample is of the left breast, "right" if it is of the right breast.
        """
        match self.refnum[-2]:
            case 'l':
                return 'left'
            case 'r':
                return 'right'
            case _:
                raise ValueError(f"Unknown breast identifier in refnum: {self.refnum[-2]}")

    def _set_resolution(self) -> tuple[int, int]:
        """
        Determine the resolution of the sample based on the refnum.
        
        Returns
        -------
        tuple[int, int]
            A tuple containing the resolution of the sample in the format (width, height).
        """
        match self.refnum[-1]:
            case 's':  # "small"
                return (1600, 4320)
            case 'm':  # "medium"
                return (2048, 4320)
            case 'l':  # "large"
                return (2600, 4320)
            case 'x':  # "extra large"
                return (5200, 4320)
            case _:
                raise ValueError(f"Unknown resolution identifier in refnum: {self.refnum[-1]}")


def load_info(info_file_path) -> list[MiniMIASMetadata]:
    """
    Load the metadata file and return a list of MiniMIASMetadata objects containing metadata for each sample.

    The metadata file is assumed to have no headers, delimited by whitespace, and be in the following format:
    REFNUM BG CLASS SEVERITY X Y RADIUS. See :class:`MiniMIASMetadata` for a description of each field.

    Parameters
    ----------
    info_file_path : str
        Path to the metadata file.
    
    Returns
    -------
    list of MiniMIASMetadata
        A list where each element is a MiniMIASMetadata object containing metadata for a sample.
    """
    metadata_list = []
    with open(info_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()

            # If CLASS is NORM, only 3 columns will be present
            if len(parts) == 3:
                metadata = MiniMIASMetadata(
                    refnum=parts[0],
                    bg=parts[1],
                    class_label=parts[2]
                )
            # Otherwise initialise the full sample metadata
            elif len(parts) == 7:
                metadata = MiniMIASMetadata(
                    refnum=parts[0],
                    bg=parts[1],
                    class_label=parts[2],
                    severity=parts[3],
                    x=int(parts[4]),
                    y=int(parts[5]),
                    radius=int(parts[6])
                )
            else:
                logger.warning(f"Unexpected number of columns in line: {line.strip()}")
                continue
            metadata_list.append(metadata)
    return metadata_list
