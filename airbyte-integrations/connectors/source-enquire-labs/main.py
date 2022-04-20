#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_enquire_labs import SourceEnquireLabs

if __name__ == "__main__":
    source = SourceEnquireLabs()
    launch(source, sys.argv[1:])
