"""
An abstract base class for mammography datasets, providing a common interface for all datasets in the toolkit.
"""
from abc import ABC, abstractmethod
from typing import Any

from torch.utils.data import Dataset


class MammographyDataset(Dataset, ABC):
    """
    Base class every dataset adapter (MiniMIASDataset, and later e.g. CBISDDSMDataset) should inherit from.
    
    Attributes
    ----------
    label_names : list[str]
        A list of label names with indexes corresponding to the integer labels used in the dataset. For example, if the
        dataset has two classes, "benign" and "malignant", then `label_names` could be `["benign", "malignant"]`, where
        "benign" corresponds to label 0 and "malignant" corresponds to label 1. This attribute should be defined in the
        subclass to provide meaningful label names for the specific dataset being implemented.
    """

    label_names: list[str] = []

    @abstractmethod
    def __len__(self) -> int:
        """Number of samples in the dataset."""
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, idx: int) -> tuple[Any, int]:
        """
        Return (image, label) for sample idx, with any transform already applied to the image.

        Parameters
        ----------
        idx : int
            Index of the sample to retrieve.
        
        Returns
        -------
        tuple[Any, int]
            A tuple containing the image (of any type, depending on the dataset and transforms) and the corresponding
            label as an integer.
        """
        raise NotImplementedError

    @abstractmethod
    def get_metadata(self, idx: int) -> dict:
        """
        Return whatever subgroup/patient info is available for sample idx (patient id, age, scanner, ...). Return {} if
        the dataset provides nothing beyond the label -- this is a valid, deliberate answer, not a placeholder for "not
        implemented yet".
        
        Parameters
        ----------
        idx : int
            Index of the sample to retrieve metadata for.
        
        Returns
        -------
        dict
            A dictionary containing metadata for the sample. The keys and values depend on the dataset and what
            information is available. If no metadata is available, return an empty dictionary.
        """
        raise NotImplementedError

    def get_label(self, idx: int) -> int:
        """
        Return just the label for sample idx.

        The default implementation below is correct but often slow -- it falls back to `__getitem__`, which for an image
        dataset usually means decoding and transforming the full image just to throw it away. Override this in a
        subclass whenever the label is available more cheaply (e.g. straight from an in-memory dataframe, as
        `MiniMIASDataset` can do), since `describe()` calls this once per sample and you don't want that to mean
        decoding your entire dataset just to print a class-balance table.
        
        Parameters
        ----------
        idx : int
            Index of the sample to retrieve the label for.
        
        Returns
        -------
        int
            The label corresponding to the sample at the given index.
        """
        _, label = self[idx]
        return label

    def describe(self) -> dict[str, int]:
        """
        Return a {label_name: count} class-balance summary.

        Built entirely on `__len__` and `get_label`, so it works correctly for any subclass with zero additional code --
        and it automatically gets faster for any subclass that bothers to override `get_label` with a cheap version.
        
        Returns
        -------
        dict[str, int]
            A dictionary where keys are label names and values are the counts of samples for each label in the dataset.
        """
        counts = {name: 0 for name in self.label_names}
        for idx in range(len(self)):
            counts[self.label_names[self.get_label(idx)]] += 1
        return counts
