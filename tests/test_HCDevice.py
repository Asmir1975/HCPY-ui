from unittest.mock import Mock, patch

from HCDevice import HCDevice


def test_reconnect_does_not_request_redundant_ro_values():
    device = object.__new__(HCDevice)
    device.services_initialized = True
    device.get = Mock()

    with patch("HCDevice.time.sleep"):
        device.reconnect()

    requested_resources = [call.args[0] for call in device.get.call_args_list]

    assert "/ro/allMandatoryValues" in requested_resources
    assert "/ro/allDescriptionChanges" in requested_resources
    assert "/ro/values" not in requested_resources
