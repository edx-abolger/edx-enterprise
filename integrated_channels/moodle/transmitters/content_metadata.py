# -*- coding: utf-8 -*-
"""
Class for transmitting content metadata to Moodle.
"""
import logging

from integrated_channels.integrated_channel.transmitters.content_metadata import ContentMetadataTransmitter
from integrated_channels.moodle.client import MoodleAPIClient

LOGGER = logging.getLogger(__name__)


class MoodleContentMetadataTransmitter(ContentMetadataTransmitter):
    """
    This transmitter transmits exported content metadata to Moodle.
    """

    def __init__(self, enterprise_configuration, client=MoodleAPIClient):
        """
        Use the ``MoodleAPIClient`` for content metadata transmission to Moodle.
        """
        super(MoodleContentMetadataTransmitter, self).__init__(
            enterprise_configuration=enterprise_configuration,
            client=client
        )

    def _prepare_items_for_transmission(self, channel_metadata_items):
        """
        Takes items from the exporter and formats the keys in the way required for
        course creation in Moodle.
        Note: It is *only* used for course creation, no other end point.
        """
        items = {}
        for _, item in enumerate(channel_metadata_items):
            for key in item:
                new_key = 'courses[0][{0}]'.format(key)
                items[new_key] = item[key]
        return items

    def _serialize_items(self, channel_metadata_items):
        """
        Overrides base serialize function because we do not want a JSON dump here.
        We need to modify and append data and change it into a query string,
        so a binary string is not useful.
        """
        return self._prepare_items_for_transmission(channel_metadata_items)
