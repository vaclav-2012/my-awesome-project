# -*- coding: utf-8 -*-

import importlib_metadata as metadata

distribution_name = "my-awesome-project"


def version() -> str:
    """Returns the package version."""
    return metadata.version(distribution_name)
